#!/usr/bin/env python

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import Sticker, InlineKeyboardButton, InlineKeyboardMarkup


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hola, dime tu nombre :)')

def foto(update, context):
    if update.message is not None:
        id = update.message.chat_id
    else:
        id = update.callback_query.message.chat_id
    """Send a message when the command /start is issued."""
    context.bot.send_photo(id,"https://cdn.computerhoy.com/sites/navi.axelspringer.es/public"
                                                 "/styles/480/public/media/image/2018/08/fotos-perfil-whatsapp_16.jpg"
                                                 "?itok=aqeTumbO", caption="mira que foto mas xhula")

def ubicacion(update, context):
    if update.message is not None:
        id = update.message.chat_id
    else:
        id = update.callback_query.message.chat_id
    context.bot.send_venue(id,41.6576994,-4.7101465,"BEST Valladolid", "Escuela de Ingenierías Industriales")

def sticker(update, context):
    if update.message is not None:
        id = update.message.chat_id
    else:
        id = update.callback_query.message.chat_id
    context.bot.send_sticker(id, "CAACAgIAAxkBAAMiX4mZESE1_s5L5HQMES1cBc-_BrcAAngLAAIvD_AGjN-7j0tMVIobBA")

def guitarra(update, context):
    if update.message is not None:
        id = update.message.chat_id
    else:
        id = update.callback_query.message.chat_id
    context.bot.send_audio(id, "https://raw.githubusercontent.com/TelegramBots/book/master/src/docs/audio-guitar.mp3")

def send_keyboard(update, context):
    boton1 = InlineKeyboardButton("foto", callback_data="foto")
    boton2 = InlineKeyboardButton("ubicacion", callback_data="ubicacion")
    boton3 = InlineKeyboardButton("sticker", callback_data="sticker")
    boton4 = InlineKeyboardButton("guitarra", callback_data="guitarra")
    teclado = InlineKeyboardMarkup([[boton1,boton2],[boton3,boton4]])
    context.bot.send_message(update.message.chat_id, "Selecciona el comando.", reply_markup=teclado)

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
    updater = Updater("1006343583:AAEPaHBPNk5C0OWiaUTqR3ML1H9mDA_ZB40", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start)) #añadir /presentar
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("foto", foto))
    dp.add_handler(CommandHandler("ubicacion", ubicacion))
    dp.add_handler(CommandHandler("sticker", sticker))
    dp.add_handler(CommandHandler("guitarra", guitarra))
    dp.add_handler(CommandHandler("lista", send_keyboard))
    dp.add_handler(CallbackQueryHandler(foto, pattern="foto"))
    dp.add_handler(CallbackQueryHandler(ubicacion, pattern="ubicacion"))
    dp.add_handler(CallbackQueryHandler(sticker, pattern="sticker"))
    dp.add_handler(CallbackQueryHandler(guitarra, pattern="guitarra"))
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