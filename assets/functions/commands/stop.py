from telegram import Update
from telegram.ext import ContextTypes


async def stop(update: Update, context: ContextTypes):
    context.user_data['client'].disconnect()
    await update.message.reply_text(
        "Мониторинг остановлен!"
    )
