#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import pymongo
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
from conf.settings import TELEGRAM_TOKEN, MONGODB_URI

update_id = None

# Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname
uri = MONGODB_URI

def main():
    global update_id, promos

    # Telegram Bot Authorization Token
    bot = telegram.Bot(TELEGRAM_TOKEN)

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    client = pymongo.MongoClient(uri)
    db = client.get_default_database()
    promos = db['promos']


    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1

    ### Only close the connection when your app is terminating

    client.close()


def echo(bot):
    global update_id, promos

    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            user = update.message.from_user
            chat_id = update.message.chat_id
            if update.message.text != None:
                newStr = charRemoveAndLower(update.message.text, "(!@#$%&*-_=+),.;/?|[]{}")
                words = filter(None, newStr.split(" "))
                for word in words:
                    cursor = promos.find_one({'keywords': word})
                    if cursor != None:
                        slogan = cursor['slogan']
                        shortMessage = cursor['message']
                        link = cursor['link']
                        update.message.reply_text(shortMessage)
                        update.message.reply_text(slogan)
                        # update.message.reply_text(link)
                        return



def charRemoveAndLower(old, to_remove):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string.lower()


if __name__ == '__main__':
    main()
