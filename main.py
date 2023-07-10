import logging

from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler, CallbackQueryHandler

from assets.functions.additional.keywords.add_keywords import add_keywords
from assets.functions.additional.keywords.add_keywords_info import add_keywords_info
from assets.functions.additional.keywords.del_keywords_info import del_keywords_info
from assets.functions.additional.keywords.del_keywords import del_keywords
from assets.functions.additional.keywords.confirm_del_keywords import confirm_del_keywords
from assets.functions.additional.keywords.save_keywords import save_keywords
from assets.functions.additional.keywords.show_dialog import show_dialog

from assets.functions.additional.groups.add_group import add_group
from assets.functions.additional.groups.add_groups_info import add_groups_info
from assets.functions.additional.groups.confirm_del_groups import confirm_del_groups
from assets.functions.additional.groups.del_group import del_group
from assets.functions.additional.groups.del_groups_info import del_groups_info
from assets.functions.additional.groups.save_groups import save_groups

from assets.functions.additional.special.stop_conv import stop_conv

from assets.functions.commands.groups import groups
from assets.functions.commands.manage import manage
from assets.functions.commands.start import start
from assets.functions.commands.stop import stop
from assets.functions.commands.startmonitoring import startmonitoring

from config import BOT_TOKEN


# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


def main():
    # Создаём объект Application.
    application = Application.builder().token(BOT_TOKEN).build()

    manage_keywords_conv = ConversationHandler(
        # Точка входа в диалог.
        entry_points=[CommandHandler('manage', manage)],

        # Состояние внутри диалога.
        states={
            1: [CallbackQueryHandler(show_dialog)],
            2: [CallbackQueryHandler(add_keywords_info, pattern="ADD"),
                CallbackQueryHandler(del_keywords_info, pattern="DEL")],
            "ADD": [MessageHandler(filters.Text("Готово") & ~filters.COMMAND,
                                   save_keywords),
                    MessageHandler(filters.TEXT & ~filters.COMMAND, add_keywords)],
            "DEL": [CallbackQueryHandler(confirm_del_keywords, pattern="SAVE"),
                    CallbackQueryHandler(del_keywords)]
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[MessageHandler(filters.COMMAND,
                                  stop_conv)]
    )

    manage_groups_conv = ConversationHandler(
        # Точка входа в диалог.
        entry_points=[CommandHandler('groups', groups)],

        # Состояние внутри диалога.
        states={
            1: [CallbackQueryHandler(add_groups_info, pattern="ADD"),
                CallbackQueryHandler(del_groups_info, pattern="DEL")],
            "ADD": [MessageHandler(filters.Text("Готово") & ~filters.COMMAND,
                                   save_groups),
                    MessageHandler(filters.TEXT & ~filters.COMMAND, add_group)],
            "DEL": [CallbackQueryHandler(confirm_del_groups, pattern="SAVE"),
                    CallbackQueryHandler(del_group)]
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[MessageHandler(filters.COMMAND,
                                  stop_conv)]
    )

    application.add_handler(manage_keywords_conv)
    application.add_handler(manage_groups_conv)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("stop", stop))
    application.add_handler(CommandHandler("startmonitoring", startmonitoring))

    # Запускаем приложение.
    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
