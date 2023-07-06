from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler


async def save_keywords(update: Update, context: ContextTypes):
    await update.message.reply_text(
        "Ключевые слова успешно сохранены.",
        reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END
