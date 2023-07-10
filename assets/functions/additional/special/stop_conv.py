from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler


async def stop_conv(update: Update, context: ContextTypes):
    return ConversationHandler.END
