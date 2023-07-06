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
        # context.user_data['groups'] = {
        #     "@mygroup2007": ["hello", "goodbye"]}
        context.user_data['groups'] = {}
        context.user_data['launched'] = True
        client = TelegramClient('bot', API_ID, API_HASH)
        context.user_data['client'] = client

        await update.message.reply_text(
            "Здравствуйте! Бот успешно проинициализирован! "
            "Используйте /manage или /groups для дальнейшей работы."
        )
