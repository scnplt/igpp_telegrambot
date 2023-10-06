import os
import telegram

from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from igpphd import get_pp_hd_link as pplink

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Hi! I'm a bot that can get Instagram profile picture in HD quality. Just send me an Instagram username (eg. @cpsertan) and I'll send you the HD profile picture link.")

def get_pp_hd_link(update, context):
    username = update.message.text.split('@')[1]
    link = pplink(username)
    update.message.reply_text(link)

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, get_pp_hd_link))
updater.start_polling(
    listen='0.0.0.0',
    port=int(os.environ.get('PORT', '5000')),
    url_path=TELEGRAM_BOT_TOKEN,
    webhook_url= + TELEGRAM_BOT_TOKEN
)
