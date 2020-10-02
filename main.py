#!/usr/bin/env python

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hola, dime tu nombre :)')

def foto(update, context):
    """Send a message when the command /start is issued."""
    context.bot.send_photo(update.message.chat_id,"https://cdn.computerhoy.com/sites/navi.axelspringer.es/public"
                                                 "/styles/480/public/media/image/2018/08/fotos-perfil-whatsapp_16.jpg"
                                                 "?itok=aqeTumbO", caption="mira que foto mas xhula")

def ubicacion(update, context):
    context.bot.send_venue(update.message.chat_id,41.6576994,-4.7101465,"BEST Valladolid", "Escuela de Ingenierías Industriales")

def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Tan solo escribe tu nombre ;)')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text('Hola ' + update.message.text + ' !')


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1006343583:AAEMxoZrVaQcPA4oSjkbS7gNBkWaMmxLgdM", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start)) #añadir /presentar
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("foto", foto))
    dp.add_handler(CommandHandler("ubicacion", ubicacion))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()