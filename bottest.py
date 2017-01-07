# coding=utf-8
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


updater = Updater(token='287220380:AAExRqpfVIAhkcbpSZZBguTdQ9WD8oIoVRM')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.NOTSET)

updater.start_polling()


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Ich bin ein Bot, rede mit mir!")


def test(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Dkmkfgjroij ghrjk ruhiuehr rhilghrguilhruighdkj grhg rrhjdhg r 🖕")


start_handler = CommandHandler('start', start)
test_handler = CommandHandler('test', test)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(test_handler)


def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)


echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
