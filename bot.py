#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to Telegram messages.

This is built on the API wrapper, see echobot2.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep

from wiki import wiki_search
from weather_condition import weather_search
from geocode import location_search
from exchange import currency_exchange
from btc_exchange import btc_exchange


update_id = None


def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot('587482499:AAG-8F4tFCHJHzP_a5Y1cKJGsBg2bMNklJg')

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

def bot_wiki(bot):
    flag = 0
    while 1:
        global update_id
        for update in bot.get_updates(offset=update_id, timeout=500):
            update_id = update.update_id + 1
            if update.message:
                if (update.message.text) == "/back":
                    flag = 1
                else:
                    text = wiki_search(update.message.text)
                    print ("Wiki")
                    update.message.reply_text(text)
            if flag == 1:
                update.message.reply_text("Back to staring position")
                return

def bot_weather(bot):
    flag = 0
    while 1:
        global update_id
        for update in bot.get_updates(offset=update_id, timeout=500):
            update_id = update.update_id + 1
            if update.message:
                if (update.message.text) == "/back":
                    flag = 1
                else:
                    text = weather_search(update.message.text)
                    print ("Weather")
                    update.message.reply_text(text)
            if flag == 1:
                update.message.reply_text("Back to staring position")
                return

def bot_location(bot):
    flag = 0
    while 1:
        global update_id
        for update in bot.get_updates(offset=update_id, timeout=500):
            update_id = update.update_id + 1
            if update.message:
                if (update.message.text) == "/back":
                    flag = 1
                else:
                    text = location_search(update.message.text)
                    print ("GoogleMap")
                    update.message.reply_text(text)
            if flag == 1:
                update.message.reply_text("Back to staring position")
                return

def bot_currency_exchange(bot):
    flag = 0
    while 1:
        global update_id
        for update in bot.get_updates(offset=update_id, timeout=500):
            update_id = update.update_id + 1
            if update.message:
                if (update.message.text) == "/back":
                    flag = 1
                else:
                    text = currency_exchange(update.message.text)
                    print ("bot_currency_exchnge")
                    update.message.reply_text(text)
            if flag == 1:
                update.message.reply_text("Back to staring position")
                return

def echo(bot):
    """Echo the message the user sent."""
    global update_id
    return_text = ""
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=500):
        update_id = update.update_id + 1

        print ("update_id " + str(update) +'\n')
        if update.message:  # your bot can receive updates without messages
            if str(update.message.text) == "/search" :
                print ("/search")
                # Reply to the message
                
                custom_keyboard = [['Wikipedia', 'Weather'], ['Currency Exchange', 'GoogleMap'], ['BTC Exchange']]
                reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard,one_time_keyboard=True)
                bot.send_message(chat_id= update.message.chat.id, text="Search options", reply_markup=reply_markup)
                for update in bot.get_updates(offset=update_id, timeout=500):
                    update_id = update.update_id + 1

                    print ("update_id in searchoption" + str(update) +'\n')
                    if update.message:  # your bot can receive updates without messages

                        if str(update.message.text) == "Wikipedia" :
                            update.message.reply_text("Please give topic for search")
                            bot_wiki(bot)

                        elif update.message.text == "Weather" :
                            update.message.reply_text("Please give the name of a city and you will get weather report of it.")
                            bot_weather(bot)

                        elif update.message.text == "GoogleMap" :
                            update.message.reply_text("Please give any address and you will get long and lat of that location.")
                            bot_location(bot)

                        elif update.message.text == "Currency Exchange" :
                            update.message.reply_text("Currency list : 'USD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY', 'HUF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AUD', 'CHF', 'KRW', 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'EUR', 'NOK', 'RUB', 'INR', 'MXN', 'CZK', 'BRL', 'PLN', 'PHP', 'ZAR', 'BITCOIN'\n\nPlease give input like: USD ZAR 1 \nIt will show 12.5241. That means\n1 USD = 12.5241 ZAR")
                            bot_currency_exchange(bot)

                        elif update.message.text == "BTC Exchange" :
                            update.message.reply_text("Bot will display buying and selling price from different BITCOIN traders in Indian Currency.")
                            update.message.reply_text(btc_exchange())
                            update.message.reply_text("Back to staring position")

                        else:
                            #print ("else")
                            return_text = str(update.message.text)

                update.message.reply_text(return_text)
                print ("after search")
            else:
                update.message.reply_text(update.message.text)

if __name__ == '__main__':
    main()
