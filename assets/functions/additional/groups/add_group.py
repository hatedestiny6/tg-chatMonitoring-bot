from telethon.tl.functions.channels import JoinChannelRequest

from telegram import Update
from telegram.ext import ContextTypes


async def add_group(update: Update, context: ContextTypes):
    link = update.message.text
    client = context.user_data['client']

    await update.message.reply_text(
        "Идет проверка введенных данных..."
    )

    try:
        await client.start()
        chat = await client.get_entity(link)

        name = link.split('/')[-1]

        if "@" not in name:
            name = f"@{name}"

        if name not in context.user_data['groups'].keys():
            context.user_data['groups'][name] = []

            await client(JoinChannelRequest(chat))

            await update.message.reply_text(
                f"Группа {name} успешно добавлена!\n\n"
                "По окончанию нажмите на кнопку <b>Готово</b> на клавиатуре.",
                parse_mode="HTML"
            )

        else:
            await update.message.reply_text(
                f"Группа {name} уже была добавлена ранее! "
                "Проверьте введенные данные и попробуйте снова.\n\n"
                "По окончанию нажмите на кнопку <b>Готово</b> на клавиатуре.",
                parse_mode="HTML"
            )

        return "ADD"

    except ValueError:
        await update.message.reply_text(
            "Некорректная ссылка! Проверьте введённые данные "
            "и попробуйте еще раз."
        )

        return "ADD"
