from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler


async def save_groups(update: Update, context: ContextTypes):
    await update.message.reply_text(
        "Группы успешно сохранены. "
        "Используйте /manage для управления ими.",
        reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END
