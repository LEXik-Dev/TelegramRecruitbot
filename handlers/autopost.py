# handlers/autopost.py
import asyncio
import logging
from aiogram import Router, types, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import InputMediaPhoto
import random
from config import ADMINS #Получим список админов
from aiogram.fsm.state import State, StatesGroup
from datetime import datetime, timedelta

router = Router()
logging.basicConfig(level=logging.INFO)

class AutoPostState(StatesGroup):
    waiting_group_id = State()
    waiting_time = State()
    waiting_post_time = State() #состояние для ввода времени
    waiting_group_id_now = State() # Состояние для ручной публикации

# --- Функции генерации контента (замените на свои)

async def generate_post():
    """Генерирует текст и изображение для поста."""
    texts = [
"Скоро нейросети будут писать за нас эти посты.",
"ИИ уже среди нас, готовьтесь к сингулярности!",
"Будущее уже здесь, но не для всех."
    ]
    images = [
        "https://i.pinimg.com/736x/74/16/1b/74161b0883a33b4b7cc403ba396da93f.jpg",
        "https://i.pinimg.com/736x/23/36/c5/2336c5453f46df6a94efc7df7144107f.jpg",
        "https://i.pinimg.com/736x/c6/e7/d6/c6e7d6a50d13cfedc50ce61e0c6724fd.jpg",
    ]

    text = random.choice(texts)
    image = random.choice(images)
    return text, image

# --- Функции публикации постов

async def publish_post(bot: Bot, group_id: int, text: str, image: str):
    """Публикует пост в группе."""
    try:
        await bot.send_photo(
            chat_id = group_id,
             photo = image,
             caption = text
         )
        logging.info(f"Post published in group {group_id}")
    except Exception as e:
        logging.error(f"Error publishing post: {e}")


@router.message(Command("autopost"))
async def autopost_handler(message: types.Message, bot: Bot, state: FSMContext):
    if message.from_user.id not in ADMINS:
        await message.answer("Вы не являетесь администратором.")
        return
    await message.answer("Введите ID группы, куда нужно постить")
    await state.set_state(AutoPostState.waiting_group_id)

@router.message(AutoPostState.waiting_group_id)
async def set_group_id(message: types.Message, bot: Bot, state: FSMContext):
    try:
       group_id = int(message.text)
       await state.update_data(group_id=group_id)
       await state.set_state(AutoPostState.waiting_time)
       await message.answer("Укажите время между публикациями (в секундах) ")
    except ValueError:
       await message.answer("Неверный формат id")

@router.message(AutoPostState.waiting_time, lambda message: message.text and message.text.isdigit())
async def set_posting_time(message: types.Message, bot: Bot, state: FSMContext):
     posting_time = int(message.text)
     data = await state.get_data()
     group_id = data.get("group_id")
     await state.update_data(posting_time=posting_time)
     await message.answer(f"Бот начнет постить каждые {posting_time} секунд")
     await state.clear()
     await start_auto_posting(bot, group_id, posting_time)


@router.message(Command("publish_now"))
async def publish_now_handler(message: types.Message, bot: Bot, state: FSMContext):
    """Публикует один пост немедленно."""
    if message.from_user.id not in ADMINS:
        await message.answer("Вы не являетесь администратором.")
        return
    await message.answer("Введите ID группы, куда нужно опубликовать сообщение:")
    await state.set_state(AutoPostState.waiting_group_id_now)


@router.message(AutoPostState.waiting_group_id_now)
async def process_group_id_now(message: types.Message, bot: Bot, state: FSMContext):
    try:
       group_id = int(message.text)
       await state.update_data(group_id=group_id)
       await message.answer("Укажите время публикации (в формате ЧЧ:ММ)")
       await state.set_state(AutoPostState.waiting_post_time)
    except ValueError:
         await message.answer("Неверный формат id")

@router.message(AutoPostState.waiting_post_time)
async def set_post_time(message: types.Message, bot: Bot, state: FSMContext):
    try:
       post_time = datetime.strptime(message.text, "%H:%M").time() # Парсим время из сообщения
       data = await state.get_data()
       group_id = data.get("group_id")
       now = datetime.now().time()
       post_datetime = datetime.combine(datetime.now().date(), post_time)
       if post_time < now: #если время поста меньше текущего - добавляем день
         post_datetime += timedelta(days=1)

       await state.clear()
       await schedule_post(bot, group_id, post_datetime)
       await message.answer(f"Сообщение будет опубликовано в {post_datetime.strftime('%d-%m-%Y %H:%M')}")
    except ValueError:
      await message.answer("Неправильный формат времени, используйте формат ЧЧ:ММ")



async def schedule_post(bot, group_id, post_datetime):
  """Ожидает наступления времени и публикует сообщение"""
  now = datetime.now()
  if now < post_datetime:
    delta_seconds = (post_datetime-now).total_seconds()
    text, image = await generate_post()
    await asyncio.sleep(delta_seconds)
    await publish_post(bot, group_id, text, image)
  else:
    logging.info("Время публикации уже прошло")

async def start_auto_posting(bot, group_id, posting_time):
   """Запускает цикл автоматической публикации"""
   while True:
       text, image = await generate_post()
       await publish_post(bot, group_id, text, image)
       await asyncio.sleep(posting_time)
