from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


async def del_keywords_info(update: Update, context: ContextTypes):
    query = update.callback_query

    await query.answer()

    name = context.user_data['cur_group']
    keywords = context.user_data['groups'][name]
    keyboard = []
    temp = []

    message = "Вы запустили процесс удаления ключевых слов " \
        f"для {name.split('/')[-1]}.\n\n" \
        "Чтобы удалить ключевое слово, нажмите на него в списке."

    for index, elem in enumerate(keywords):
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
