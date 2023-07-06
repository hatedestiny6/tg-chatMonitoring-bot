from telegram import Update
from telegram.ext import ContextTypes


async def add_keywords(update: Update, context: ContextTypes):
    keyword = update.message.text

    context.user_data['groups'][context.user_data['cur_group']].append(keyword)

    await update.message.reply_text(
        f"Ключевое слово '<b>{keyword}</b>' успешно добавлено! "
        "По окончанию нажмите на кнопку <b>Готово</b> на клавиатуре.",
        parse_mode="HTML"
    )

    return "ADD"
