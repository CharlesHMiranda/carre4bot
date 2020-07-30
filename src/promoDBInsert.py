#!/usr/bin/python
# Criar a Collection de Promoções em um banco de dados MongoDB hospedado em mongodb.com

import sys
import pymongo
from conf.settings import TELEGRAM_TOKEN, MONGODB_URI

### Create seed data

SEED_DATA = [
    {
        'campaign': '1',
        'name': 'Descontos',
        'emoticon': '[̲̅$̲̅(ツ)$̲̅]',
        'slogan': 'Aqui tem muitos descontos!!! Aproveite e faça seu pedido online!  http://www.carrefour.com.br',
        'keywords': ['desc', 'desconto', 'descontão', 'descontinho', 'preco', 'preço', 'precinho'],
        'link': ''
    },
    {
        'campaign': '2',
        'name': 'Cervejas',
        'emoticon': '¯\_(ツ)_/¯',
        'slogan': 'Alguém falou em cerveja? Em fds??? Vem pro Carrefour buscar a sua!',
        'keywords': ['breja', 'brejas', 'cerva', 'cerveja', 'cervejas', 'sextou', 'sextamos', 'happyhour'],
        'link': 'https://www.carrefour.com.br/Cerveja-Eisenbahn-Pilsen-350ml/p/9942815'
    },
    {
        'campaign': '3',
        'name': 'Infantil',
        'emoticon': '=^._.^=',
        'slogan': 'Tudo de melhor para a sua Fofura! Confira as promoções incríveis no site!  http://www.carrefour.com.br',
        'keywords': ['bebe', 'bebê', 'baby', 'filhote', 'fofo', 'fofa', 'fofura', 'fofolete'],
        'link': ''
    },
    {
        'campaign': '4',
        'name': 'Churrasco',
        'emoticon': 'ᕦ(ツ)ᕤ',
        'slogan': 'Pensou em churras, pensou Carrefour!!! Faça seu pedido online e aproveite as melhores ofertas!',
        'keywords': ['churras', 'churrasco', 'carvão', 'carvao', 'brasa', 'picanha', 'carne', 'carnes'],
        'link': 'https://www.carrefour.com.br/cf-promo-churrasco-em-casa-0620?crfimt=home|carrefour|bn|bnd|churrasco-em-casa_churrasco-em-casa-com-ate-25off_oferta_mercado_carrefour-e_300720|&cfrict=churrasco-em-casa'
    },
    {
        'campaign': '5',
        'name': 'Padaria',
        'emoticon': '( ͡° ͜ʖ ͡°)',
        'slogan': 'Quer pãozinho sempre fresquinho? Aqui tem! Vem pro Carrefour!  http://www.carrefour.com.br',
        'keywords': ['pão', 'pao', 'padaria', 'paozinho', 'bisnaga', 'bisnaguinha', 'cacetinho', 'bolo'],
        'link': ''
    },
    {
        'campaign': '6',
        'name': 'Dia dos Pais',
        'emoticon': '٩(♡ε♡ )۶',
        'slogan': 'Seu Pai merece tudo de bom!!! Vem comprar um presentão pra ele no Carrefour!',
        'keywords': ['pai', 'pais', 'paizão', 'paizao', 'orgulho', 'merece', 'presente', 'presentão', 'presentao'],
        'link': 'https://www.carrefour.com.br/dia-dos-pais?crfimt=hm-tlink|carrefour|menu|campanha|dia-dos-pais|5|270720'
    }
]

### Inserir a URI que está armazenada no arquivo conf/.env
uri = MONGODB_URI

#----------------------------------------------------------------------------#
# main
#----------------------------------------------------------------------------#

def main():
    client = pymongo.MongoClient(uri)
    db = client.get_default_database()

    promos = db['promos']

    # Inserir os dados na coleção "promos" no banco de dados MongoDB
    promos.insert_many(SEED_DATA)

    ### Drop para utilização na fase de desenvolvimento da aplicação
    ### db.drop_collection('promos')

    ### Fechar a conexão com o banco de dados
    client.close()


if __name__ == '__main__':
    print("Inserindo dados no banco de dados...\n")
    main()
