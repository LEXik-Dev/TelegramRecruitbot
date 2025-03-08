Инструкция по использованию
Предварительные требования:

Установите Python 3.7 или выше.
Установите необходимые библиотеки: aiogram.
Получите токен Telegram-бота у BotFather.
Узнайте ID Telegram-группы, в которую будут публиковаться посты.
Заполните файл config.py полученными данными.
Запуск бота:

Сохраните предоставленный код в файлы: config.py, main.py, utils/utils.py, handlers/autopost.py. Убедитесь, что структура каталогов соответствует указанной.
Установите необходимые зависимости, выполнив команду pip install aiogram.
Запустите бота, выполнив команду python main.py.
Использование бота:

Добавьте бота в администраторы Telegram-группы.
Запустите бота и отправьте ему команду /autopost.
Следуйте инструкциям бота:
Введите ID Telegram-группы, в которую нужно публиковать посты.
Введите интервал между автоматическими публикациями в секундах.
Для немедленной публикации отправьте команду /publish_now.
Следуйте инструкциям бота:
Введите ID Telegram-группы, в которую нужно опубликовать пост.
Введите время публикации (в формате ЧЧ:ММ).
Описание и инструкция на русском языке
Описание:

Этот бот в Telegram помогает автоматизировать постинг в ваших группах. Вы можете настроить автоматическую публикацию по расписанию или опубликовать что-то прямо сейчас.

Возможности:

Автоматический постинг: Бот будет сам публиковать посты с текстом и картинкой через заданные интервалы времени.
Ручная публикация: Можно в любой момент опубликовать пост в нужной группе.
Управление: Только админы могут управлять настройками бота.
Настройки: Можно указать ID группы для постинга и время между постами.
Как пользоваться:

Поставьте Python 3.7 или выше.
Установите aiogram.
Получите токен для бота у BotFather.
Узнайте ID вашей группы в Telegram.
В файле config.py укажите токен бота и ID админов.
Запуск:

Сохраните код в файлы config.py, main.py, utils/utils.py и handlers/autopost.py. Важно, чтобы файлы лежали в правильных папках.
В командной строке выполните pip install aiogram.
Запустите бота командой python main.py.
Использование:

Добавьте бота в админы вашей группы.
Начните с команды /autopost.
Бот спросит:
ID группы для публикации.
Интервал между постами в секундах.
Чтобы опубликовать пост сразу, используйте /publish_now.
Бот запросит:
ID группы.
Время публикации (в формате ЧЧ:ММ).
Description and instructions in English
Description:

This Telegram bot is designed to automate content posting to your Telegram groups. It allows administrators to schedule regular posts or publish a post immediately.

Key features:

Automatic posting: The bot publishes generated content (text and image) at set intervals.
Manual posting: Administrators can publish a post immediately by specifying the group ID and time of publication.
Management: Only administrators specified in the settings have access to bot management functions.
Flexible configuration: Administrators can configure the group ID for publications and the interval between automatic posts.
Instructions for use:

Prerequisites:

Install Python 3.7 or higher.
Install the necessary libraries: aiogram.
Obtain a Telegram bot token from BotFather.
Find out the ID of the Telegram group where posts will be published.
Fill in the config.py file with the received data.
Running the bot:

Save the provided code to files: config.py, main.py, utils/utils.py, handlers/autopost.py. Make sure the directory structure matches the specified one.
Install the necessary dependencies by running the command pip install aiogram.
Run the bot by executing the command python main.py.
Using the bot:

Add the bot to the administrators of the Telegram group.
Start the bot and send it the command /autopost.
Follow the bot’s instructions:
Enter the Telegram group ID where you want to publish posts.
Enter the interval between automatic publications in seconds.
To publish immediately, send the command /publish_now.
Follow the bot’s instructions:
Enter the Telegram group ID where you want to publish the post.
Enter the time of publication (in HH:MM format).
