from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes


async def add_groups_info(update: Update, context: ContextTypes):
    query = update.callback_query

    await query.answer()

    await query.edit_message_text(
        text="Введите группы в формате ссылки или username. Вводите их, "
        "отправляя каждое по одному.\n\n"
        "Пример ввода: https://t.me/examplegroup ИЛИ @examplegroup"
    )

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="По окончанию нажмите "
        "на кнопку 'Готово' на клавиатуре.",
        reply_markup=ReplyKeyboardMarkup([["Готово"]])
    )

    return "ADD"
