from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes


async def add_keywords_info(update: Update, context: ContextTypes):
    query = update.callback_query

    await query.answer()

    await query.edit_message_text(
        text="Введите ключевые слова. Вводите их, "
        "отправляя каждое по одному."
    )

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="По окончанию нажмите "
        "на кнопку на клавиатуре.",
        reply_markup=ReplyKeyboardMarkup([["Готово"]])
    )

    return "ADD"
