import logging
import random
import telegram

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater("1034516978:AAHTZOJ39mZP7b8HEvjBNvVOP3Y4YBP0tHU", use_context=True)
bot = telegram.Bot(token="1034516978:AAHTZOJ39mZP7b8HEvjBNvVOP3Y4YBP0tHU")
   # Get the dispatcher to register handlers
dp = updater.dispatcher

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

Arcanos = [
    ["/img/major00.jpg", "00 - O louco"],
    ["/img/major01.jpg", "01 - O Mago"], 
    ["/img/major02.jpg", "02 - A Sacerdotisa"],
    ["/img/major03.jpg", "03 - A Imperatriz"],
    ["/img/major04.jpg", "04 - O Imperador"],
    ["/img/major05.jpg", "05 - O Hierofante"],
    ["/img/major06.jpg", "06 - Os Amantes"],
    ["/img/major07.jpg", "07 - O Carro"],
    ["/img/major08.jpg", "08 - A Justiça"],
    ["/img/major09.jpg", "09 - O Eremita"],
    ["/img/major10.jpg", "10 - A Roda da Fortuna"],
    ["/img/major11.jpg", "11 - A Força"],
    ["/img/major12.jpg", "12 - O Enforcado"],
    ["/img/major13.jpg", "13 - A Morte"],
    ["/img/major14.jpg", "14 - A Temperança"],
    ["/img/major15.jpg", "15 - O Diabo"],
    ["/img/major16.jpg", "16 - A Torre"],
    ["/img/major17.jpg", "17 - A Estrela"],
    ["/img/major18.jpg", "18 - A Lua"],
    ["/img/major19.jpg", "19 - O Sol"],
    ["/img/major20.jpg", "20 - O Julgamento"],
    ["/img/major21.jpg", "21 - O Mundo"]
    ]

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def dia(update, context):

    random.shuffle(Arcanos)
    update.message.reply_text(Arcanos[0][1])
    #bot.sendPhoto(chat_id, Arcanos[0][0], Arcanos[0][1])
    chat_id = update.message.chat_id
    bot.sendPhoto(chat_id=chat_id, photo="https://github.com/mbione/papas-tarot/blob/master/major00.jpg")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    #updater = Updater("1034516978:AAHTZOJ39mZP7b8HEvjBNvVOP3Y4YBP0tHU", use_context=True)

    # Get the dispatcher to register handlers
    #dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("dia", dia))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__': 
    main()