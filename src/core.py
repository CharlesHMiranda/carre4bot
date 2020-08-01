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
    global update_id, campaign, campaignLog

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
    campaign = db['campaign']
    campaignLog = db['campaignlog']

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
    global update_id, campaign, campaignLog

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
                    ### Filtrar caracteres indesejados e transformar texto em minúsculas
                    newStr = charRemoveAndLower(update.message.text, "(!@#$%&*-_=+),.;/?|[]{}")
                    words = filter(None, newStr.split(" "))
                    ### Efetuar uma busca no banco de dados de Campanhas para cada palavra da mensagem
                    for word in words:
                        cursorCampaign = campaign.find_one({'keywords': word})
                        if cursorCampaign is not None:
                            ### Palavra encontrada nas palavras-chave da Campanha
                            ### Verificar se Campanha já foi enviada hoje
                            campaignId = cursorCampaign['campaign']
                            queryCampaignLog = {'id': datetime.datetime.now().strftime("%Y%m%d") + campaignId + str(chat_id)}
                            cursorCampaignLog = campaignLog.find_one(queryCampaignLog)
                            if cursorCampaignLog is None:
                                ### Apresentar a Campanha e retornar
                                sloganCampaign = cursorCampaign['slogan']
                                emoticonCampaign = cursorCampaign['emoticon']
                                linkCampaign = cursorCampaign['link']
                                update.message.reply_text(emoticonCampaign)
                                update.message.reply_text(sloganCampaign)
                                ### Apresentar o link, caso preenchido
                                if linkCampaign is not "":
                                    update.message.reply_text(linkCampaign)
                                ### Registrar que a campanha já foi enviada hoje
                                ### Query = dataInvertida + campanhaId + chat_id
                                campaignLog.insert_one(queryCampaignLog)
                                return



def charRemoveAndLower(old, to_remove):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string.lower()



if __name__ == '__main__':
    main()
