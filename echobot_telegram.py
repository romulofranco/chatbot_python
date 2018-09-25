#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to Telegram messages.
This is built on the API wrapper, see echobot2.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""
import logging
import telegram
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from telegram.error import NetworkError, Unauthorized
from time import sleep


update_id = None

botLearn = ChatBot("Romulo Bot")

conversa = ['Oi', 'Ola', 'Tudo bem?', 'Eu estou bem']
botLearn.set_trainer(ListTrainer)
botLearn.train(conversa)

def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot('561832171:AAEqnmFS1W-yVDFdkUFSmRyY70OTQ_vqXMg')

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def echo(bot):
    """Echo the message the user sent."""
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            print('Voce ', update.message.text)
            resposta = botLearn.get_response(update.message.text)
            print('Bot ', resposta)
            update.message.reply_text(resposta.text)
            
if __name__ == '__main__':
    main()