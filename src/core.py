#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import logging
import pymongo
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
from conf.settings import TELEGRAM_TOKEN, MONGODB_URI

update_id = None

### Inserir a URI que está armazenada no arquivo src/conf/.env
uri = MONGODB_URI

######################################################################
### main
######################################################################

def main():
    global update_id, promos, campaign

    ### Telegram Bot Authorization Token
    bot = telegram.Bot(TELEGRAM_TOKEN)

    ### get the first pending update_id, this is so we can skip over it in case
    ### we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    ### Estabelecer conexão com o banco de dados
    client = pymongo.MongoClient(uri)
    db = client.get_default_database()
    promos = db['promos']
    campaign = db['campaign']

    while True:
        try:
            listenConversation(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1

    ### Fechar a conexão com o banco de dados
    client.close()


######################################################################


def listenConversation(bot):
    global update_id, promos, campaign

    ### Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            user = update.message.from_user
            chat_id = update.message.chat_id
            ### Tratar somente mensagens de texto
            if update.message.text is not None:
                ### Descartar "textões" - Tratar apenas mensagens com menos de 250 caracteres
                if len(update.message.text) < 250:
                    ### Filtrar caracteres indesejados e transformar em minúsculas
                    newStr = charRemoveAndLower(update.message.text, "(!@#$%&*-_=+),.;/?|[]{}")
                    words = filter(None, newStr.split(" "))
                    ### Efetuar uma busca no banco de dados para cada palavra da mensagem
                    for word in words:
                        cursorPromos = promos.find_one({'keywords': word})
                        if cursorPromos is not None:
                            ### Palavra encontrada! Verificar se campanha já foi enviada hoje
                            campaignPromos = cursorPromos['campaign']
                            queryCampaign = {'id': str(chat_id) + datetime.datetime.now().strftime("%Y%m%d") + campaignPromos}
                            cursorCampaign = campaign.find_one(queryCampaign)
                            ### Apresentar a campanha e retornar
                            if cursorCampaign is None:
                                sloganPromos = cursorPromos['slogan']
                                emoticonPromos = cursorPromos['emoticon']
                                linkPromos = cursorPromos['link']
                                update.message.reply_text(emoticonPromos)
                                update.message.reply_text(sloganPromos)
                                ### Apresentar o link, caso preenchido
                                if linkPromos is not "":
                                    update.message.reply_text(linkPromos)
                                ### Registrar que a campanha já foi enviada hoje
                                ### Query = chat_id + dataInvertida + campanha
                                campaign.insert_one(queryCampaign)
                                return



def charRemoveAndLower(old, to_remove):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string.lower()



if __name__ == '__main__':
    main()
