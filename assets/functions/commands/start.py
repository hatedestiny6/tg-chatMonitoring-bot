from telegram import Update
from telegram.ext import ContextTypes

from telethon.sync import TelegramClient


from config import API_HASH, API_ID


async def start(update: Update, context: ContextTypes):
    try:
        if context.user_data['launched']:
            await update.message.reply_text(
                "Используйте /manage или /groups."
            )

    except KeyError:
        context.user_data['groups'] = {}
        context.user_data['launched'] = True
        client = TelegramClient('bot', API_ID, API_HASH,
                                device_model="iPhone 13 Pro Max",
                                system_version="14.8.1",
                                app_version="8.4",
                                lang_code="en",
                                system_lang_code="en-US")
        # запускался ли мониторинг
        context.user_data['monitoring'] = False
        context.user_data['client'] = client

        await update.message.reply_text(
            "Здравствуйте! Бот успешно проинициализирован! "
            "Используйте /manage или /groups для дальнейшей работы."
        )
