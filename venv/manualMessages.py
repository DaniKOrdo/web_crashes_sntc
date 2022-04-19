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


    if hc.connection(dk.RER_W) == True:
        message = '✅ Web ' + dk.RER_N + ' Ok'
        update.message.reply_text(message)
    else:
        message = '⚠️Web ' + dk.RER_N + ' Caida⚠️ ' + local_time
        print('Web ' + dk.RER_N + ' Caida ' + local_time)
        update.message.reply_text(message)


def check_s(update: Update, context: CallbackContext):
    local_time = time.asctime(time.localtime(time.time()))


    if hc.connection(dk.SNT_W) == True:
        message = '✅ Web ' + dk.SNT_N + ' Ok'
        update.message.reply_text(message)
    else:
        message = '⚠️Web ' + dk.SNT_N + ' Caida⚠️ ' + local_time
        print('Web ' + dk.SNT_N + ' Caida ' + local_time)
        update.message.reply_text(message)


def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater(dk.TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("bot", bot))
    dispatcher.add_handler(CommandHandler(dk.RER_N, check_r))
    dispatcher.add_handler(CommandHandler(dk.SNT_N, check_s))

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()