from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


async def del_group(update: Update, context: ContextTypes):
    query = update.callback_query

    await query.answer()

    group = query.data

    del context.user_data['groups'][group]

    groups = context.user_data['groups'].keys()
    keyboard = []
    temp = []

    message = "Вы запустили процесс удаления групп. " \
        "Чтобы удалить группу, нажмите на нее в списке."

    for index, elem in enumerate(groups):
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

    keyboard.append([
        InlineKeyboardButton(
            "Готово",
            callback_data="SAVE"
        )
    ])

    await query.edit_message_text(
        text=message,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

    return "DEL"
