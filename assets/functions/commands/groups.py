from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


async def groups(update: Update, context: ContextTypes):
    links = context.user_data['groups']
    message = "Текущие заданные группы для мониторинга:\n\n"

    if not links:
        message += "❌ <b>Не задано!</b>"

    else:
        for elem in links.keys():
            message += f"• {elem.split('/')[-1]}"

    message += "\n\nВыберите действие на клавиатуре."

    keyboard = [[InlineKeyboardButton(
        "Добавить группы",
        callback_data="ADD"
    ), InlineKeyboardButton(
        "Удалить группы",
        callback_data="DEL"
    )]]
    markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        message,
        reply_markup=markup,
        parse_mode="HTML"
    )

    return 1
