#!/usr/bin/python
# Criar a Collection de Promoções em um banco de dados MongoDB hospedado em mongodb.com

import sys
import pymongo
from conf.settings import TELEGRAM_TOKEN, MONGODB_URI

### Create seed data

SEED_DATA = [
    {
        'campaign': '1',
        'name': 'Padaria',
        'message': '( ͡° ͜ʖ ͡°)',
        'slogan': 'Quer pãozinho sempre fresquinho? Aqui tem! Vem pro Carrefour!  http://www.carrefour.com.br',
        'keywords': ['pão', 'pao', 'padaria', 'paozinho', 'bisnaga', 'bolo'],
        'link': 'https://www.carrefour.com.br/Pao-de-Forma-com-Graos-Frutas-e-Castanhas-Nutrella-550g/p/9498419'
    },
    {
        'campaign': '2',
        'name': 'Cervejas',
        'message': '¯\_(ツ)_/¯',
        'slogan': 'Alguém falou em cerveja? Em fds??? Vem pro Carrefour buscar a sua!  http://www.carrefour.com.br',
        'keywords': ['breja', 'brejas', 'cerva', 'cerveja', 'cervejas', 'sextou', 'sextamos', 'happyhour'],
        'link': 'https://www.carrefour.com.br/Cerveja-Eisenbahn-Pilsen-350ml/p/9942815'
    },
    {
        'campaign': '3',
        'name': 'Infantil',
        'message': '=^._.^=',
        'slogan': 'Tudo de melhor para a sua Fofura! Confira as promoções incríveis no site!  http://www.carrefour.com.br',
        'keywords': ['bebe', 'bebê', 'baby', 'filhote', 'fofo', 'fofa', 'fofura'],
        'link': 'https://www.carrefour.com.br/Lenco-Umedecido-Dove-Baby-Hidratacao-Enriquecida-com-50-unidades/p/9778586'
    },
    {
        'campaign': '4',
        'name': 'Churrasco',
        'message': 'ᕦ(ツ)ᕤ',
        'slogan': 'Pensou em churras, pensou Carrefour!!! Faça seu pedido online e aproveite as melhores ofertas!  http://www.carrefour.com.br',
        'keywords': ['churras', 'churrasco', 'carvão', 'carvao', 'brasa', 'picanha', 'carne', 'carnes'],
        'link': 'https://www.carrefour.com.br/Peca-de-Picanha-Bovina-Resfriada-Montana-1Kg/p/5283884'
    },
    {
        'campaign': '5',
        'name': 'Descontos',
        'message': '[̲̅$̲̅(ツ)$̲̅]',
        'slogan': 'Aqui tem muitos descontos!!! Aproveite e faça seu pedido online!  http://www.carrefour.com.br',
        'keywords': ['desc', 'desconto', 'descontão', 'descontinho', 'preco', 'preço', 'precinho'],
        'link': 'https://www.carrefour.com.br/Peca-de-Picanha-Bovina-Resfriada-Montana-1Kg/p/5283884'
    }
]

### Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname

uri = MONGODB_URI

###############################################################################
# main
###############################################################################

def main(args):
    client = pymongo.MongoClient(uri)
    db = client.get_default_database()

    promos = db['promos']

    # Note that the insert method can take either an array or a single dict.
    promos.insert_many(SEED_DATA)

    ### Since this is an example, we'll clean up after ourselves.
    # db.drop_collection('promos')

    ### Only close the connection when your app is terminating
    client.close()


if __name__ == '__main__':
    main(sys.argv[1:])
