from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler


async def confirm_del_groups(update: Update, context: ContextTypes):
    query = update.callback_query

    await query.answer()

    await query.edit_message_text(
        text="Группы успешно удалены."
    )

    return ConversationHandler.END
