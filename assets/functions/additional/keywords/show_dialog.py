from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


async def show_dialog(update: Update, context: ContextTypes):
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    await query.answer()

    name = query.data
    context.user_data['cur_group'] = name

    keywords = context.user_data['groups'][name]
    message = f"Текущие ключевые слова для {name}:\n\n"

    if not keywords:
        message += "❌ <b>Не задано!</b>"

    for elem in keywords:
        message += f"• <b>{elem}</b>\n"

    keyboard = [[InlineKeyboardButton(
                "Добавить ключевые слова",
                callback_data="ADD"
                ),
        InlineKeyboardButton(
        "Удалить ключевые слова",
        callback_data="DEL"
    )]]

    markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text=message,
        reply_markup=markup,
        parse_mode="HTML"
    )

    return 2
