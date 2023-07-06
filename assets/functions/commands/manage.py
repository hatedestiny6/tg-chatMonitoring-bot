from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler


async def manage(update: Update, context: ContextTypes):
    links = context.user_data['groups']
    message = "Текущие заданные группы для мониторинга:\n\n"

    if not links:
        message += "❌ <b>Не задано!</b>\n\n"
        message += "Добавьте группы, используя /groups."

        await update.message.reply_text(
            message,
            parse_mode="HTML"
        )

        return ConversationHandler.END

    else:
        for elem in links.keys():
            message += f"• {elem.split('/')[-1]}"

    message += "\n\nВыберите группу для редактирования."

    keyboard = []
    temp = []

    for index, elem in enumerate(list(links.keys())):
        if index % 3 == 0:
            keyboard.append(temp)
            temp = []

        temp.append(
            InlineKeyboardButton(
                elem,
                callback_data=elem
            )
        )

    if temp:
        keyboard.append(temp)

    markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        message,
        reply_markup=markup
    )

    return 1
