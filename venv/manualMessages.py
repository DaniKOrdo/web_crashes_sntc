import logging
import time
import dk_token as dk
import httpconnection as hc

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(
    filename='manualMessages.log', 
    encoding='utf-8',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def bot(update: Update, context: CallbackContext):
    update.message.reply_text('✅ Bot funcionando')


def check_r(update: Update, context: CallbackContext):
    local_time = time.asctime(time.localtime(time.time()))


    if hc.connection(dk.RER_W) == 200:
        message = '✅ Web ' + dk.RER_N + ' Ok'
        update.message.reply_text(message)
    elif hc.connection(dk.RER_W) == -10:
        message = '❌ Error ' + dk.RER_W + ' (O no existe)'
        print('Error ' + dk.RER_N + ' Error ' + local_time)
        update.message.reply_text(message)
    else:
        message = '⚠️Web ' + dk.RER_N + ' Caida⚠️ ' + local_time
        print('Web ' + dk.RER_N + ' Caida ' + local_time)
        update.message.reply_text(message)
        update.message.reply_text("Código: " + hc.connection(dk.RER_W))


def check_s(update: Update, context: CallbackContext):
    local_time = time.asctime(time.localtime(time.time()))


    if hc.connection(dk.SNT_W) == 200:
        message = '✅ Web ' + dk.SNT_N + ' Ok'
        update.message.reply_text(message)
    elif hc.connection(dk.SNT_W) == -10:
        message = '❌ Error ' + dk.SNT_W + ' (O no existe)'
        print('Error ' + dk.SNT_N + ' Error ' + local_time)
        update.message.reply_text(message)
    else:
        message = '⚠️Web ' + dk.SNT_N + ' Caida⚠️ ' + local_time
        print('Web ' + dk.SNT_N + ' Caida ' + local_time)
        update.message.reply_text(message)
        update.message.reply_text("Código: " + hc.connection(dk.SNT_N))

def check_all_web(update: Update, context: CallbackContext):
    local_time = time.asctime(time.localtime(time.time()))
    web_name = update.message.text.split(' ')[1]

    if hc.connection(web_name) == 200:
        message = '✅ Web ' + web_name + ' Ok'
        update.message.reply_text(message)
    elif hc.connection(web_name) == -10:
        message = '❌ Error ' + web_name + ' (O no existe)'
        print('Error ' + web_name + ' Error ' + local_time)
        update.message.reply_text(message)
    else:
        message = '⚠️Web ' + web_name + ' Caida⚠️ ' + local_time
        print('Web ' + web_name + ' Caida ' + local_time)
        update.message.reply_text(message)
        update.message.reply_text("Código: " + hc.connection(web_name))


def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater(dk.TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("bot", bot))
    dispatcher.add_handler(CommandHandler(dk.RER_N, check_r))
    dispatcher.add_handler(CommandHandler(dk.SNT_N, check_s))
    dispatcher.add_handler(CommandHandler("web", check_all_web))
    dispatcher.add_handler(CommandHandler("www", check_all_web))

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()