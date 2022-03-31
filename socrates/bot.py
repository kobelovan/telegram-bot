
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


#Command Handlers
def start(update, context):
    update.message.reply_text('The unexamined life is not worth living.')


#function to respond to help cmd
def help(update, context):
    update.message.reply_text('I cannot teach anybody anything. I can only make them think')
    
#function to respond to wisdom cmd
def wisdom(update, context):
    update.message.reply_text('Wonder is the beginning of wisdom.')
    
#function to respond to happy cmd
def happy(update, context):
    update.message.reply_text('The secret of happiness, you see, is not found in seeking more, but in developing the capactiy to enjoy less.')
    
#function to respond to rip cmd
def rip(update, context):
    update.message.reply_text('The wise man seeks death all his life, and for this reason death is not terrifying to him.')
        
#function to respond to knowledge cmd
def knowledge(update, context):
    update.message.reply_text('There is only one good, knowledge, and one evil, ignorance.')
    
#function to echo the users message
def echo(update, context):
    update.message.reply_text(update.message.text + '?' + ' focus on knowing thyself, my dear boy.')

#function to log errors and display
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("5031323628:AAGtB7JPd8QOtzY5cU9iAZ-DzKjgZsQ9M4U", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("wisdom", wisdom))
    dp.add_handler(CommandHandler("knowledge", knowledge))
    dp.add_handler(CommandHandler("rip", rip))
    dp.add_handler(CommandHandler("happy", happy))
    
    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()