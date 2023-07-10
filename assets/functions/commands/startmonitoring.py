from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler


from telethon.sync import events


async def startmonitoring(update: Update, context: ContextTypes):
    client = context.user_data['client']

    if not context.user_data['monitoring']:
        @client.on(events.NewMessage(chats=list(context.user_data['groups'].keys())))
        async def msg_handler(event):
            # получаем имя юзера
            sender = await event.get_sender()

            # получаем имя группы
            chat_from = event.chat if event.chat else (await event.get_chat())

            if [word for word in
                context.user_data['groups'][f"@{chat_from.username}"]
                    if word.strip().lower() in event.text.lower()]:
                await update.message.reply_text(
                    f"🚨 Пользователь @{sender.username} в группу "
                    f"@{chat_from.username} отправил сообщение, "
                    "содержащее ключевые слова. Вот его текст:\n\n"
                    f"{event.text}"
                )

        context.user_data['monitoring'] = True

    await client.connect()
    await update.message.reply_text(
        "Мониторинг запущен! Используйте /stop."
    )

    return ConversationHandler.END
