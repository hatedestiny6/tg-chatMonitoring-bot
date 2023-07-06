from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler


async def confirm_del_keywords(update: Update, context: ContextTypes):
    query = update.callback_query

    await query.answer()

    await query.edit_message_text(
        text="Ключевые слова успешно удалены."
    )

    return ConversationHandler.END
