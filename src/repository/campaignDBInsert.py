#!/usr/bin/python
# Criar a Collection de Campanhas em um banco de dados MongoDB hospedado Nuvem

import sys
import pymongo
from src.conf.settings import TELEGRAM_TOKEN, MONGODB_URI

### Create seed data
SEED_DATA = [
    {
        'campaign': '1',
        'name': 'Descontos',
        'emoticon': '[̲̅$̲̅(ツ)$̲̅]',
        'slogan': 'Aqui tem muitos descontos!!! Aproveite e faça seu pedido online!  http://www.carrefour.com.br',
        'keywords': ['carrefour', 'desc', 'desconto', 'descontos', 'descontao', 'descontão', 'descontinho', 'preco', 'preço', 'precinho'],
        'link': ''
    },
    {
        'campaign': '2',
        'name': 'Cervejas',
        'emoticon': '¯\_(ツ)_/¯',
        'slogan': 'Alguém falou em cerveja? Em fds??? Vem pro Carrefour buscar a sua!',
        'keywords': ['fds', 'beer', 'breja', 'brejas', 'cerva', 'cervas', 'cerveja', 'cervejas', 'cerveza', 'cevada', 'sextou', 'sextamos', 'happyhour'],
        'link': 'https://www.carrefour.com.br/cervejas?crfint=hm-tlink|mercado|bebidas-alcoolicas-e-nao-alcoolicas|2|cervejas|2'
    },
    {
        'campaign': '3',
        'name': 'Infantil',
        'emoticon': '=^._.^=',
        'slogan': 'Tudo de melhor para a sua Fofura! Confira as promoções incríveis no site!  http://www.carrefour.com.br',
        'keywords': ['bebe', 'bebê', 'baby', 'filhota', 'filhote', 'fofa', 'fofo', 'fofura', 'fofuras', 'fofolete'],
        'link': ''
    },
    {
        'campaign': '4',
        'name': 'Churrasco',
        'emoticon': 'ᕦ(ツ)ᕤ',
        'slogan': 'Pensou em churras, pensou Carrefour!!! Faça seu pedido online e aproveite as melhores ofertas!',
        'keywords': ['churra', 'churras', 'churrasco', 'churrascao', 'churrascão', 'carvao', 'carvão', 'brasa', 'picanha', 'carne', 'carnes'],
        'link': 'https://www.carrefour.com.br/cf-promo-churrasco-em-casa-0620?crfimt=home|carrefour|bn|bnd|churrasco-em-casa_churrasco-em-casa-com-ate-25off_oferta_mercado_carrefour-e_300720|&cfrict=churrasco-em-casa'
    },
    {
        'campaign': '5',
        'name': 'Padaria',
        'emoticon': '( ͡° ͜ʖ ͡°)',
        'slogan': 'Quer pãozinho sempre fresquinho? Aqui tem! Vem pro Carrefour!  http://www.carrefour.com.br',
        'keywords': ['pao', 'pão', 'padaria', 'paozinho', 'pãozinho', 'bisnaga', 'bisnaguinha', 'cacetinho', 'bolo'],
        'link': ''
    },
    {
        'campaign': '6',
        'name': 'Aniversário',
        'emoticon': '♪♫*•♪',
        'slogan': 'Parabéns! Parabéns para você! E muitas felicidades!!! Aproveite o seu dia e venha comemorar com a gente!  http://www.carrefour.com.br',
        'keywords': ['niver', 'parabens', 'parabéns', 'felicidade', 'felicidades', 'aniversario', 'aniversário'],
        'link': ''
    },
    {
        'campaign': '7',
        'name': 'Dia dos Pais',
        'emoticon': 'ლ(´ڡ`ლ)',
        'slogan': 'Seu Pai merece tudo de bom!!! Vem comprar um presentão pra ele no Carrefour!',
        'keywords': ['pai', 'papai', 'pais', 'paizao', 'paizão', 'orgulho', 'merece', 'presente', 'presentao',
                     'presentão'],
        'link': 'https://www.carrefour.com.br/dia-dos-pais?crfimt=hm-tlink|carrefour|menu|campanha|dia-dos-pais|5|270720'
    },
    {
        'campaign': '8',
        'name': 'Empréstimo Pessoal',
        'emoticon': '[̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅]',
        'slogan': 'Coloque os seus projetos em prática, sem burocracia, com uma das taxas mais competitivas do mercado!',
        'keywords': ['emprestimo', 'empréstimo', 'credito', 'crédito', 'sonho', 'sonhos', 'grana', 'dinheiro'],
        'link': 'https://www.carrefoursolucoes.com.br/credito-pessoal'
    }
]

### Inserir a URI que está armazenada no arquivo conf/.env
uri = MONGODB_URI

######################################################################
### main
######################################################################

def main():
    ### Estabelecer conexão com o banco de dados
    client = pymongo.MongoClient(uri)
    db = client.get_default_database()
    campaign = db['campaign']

    ### Drop para utilização na fase de desenvolvimento da aplicação
    ### db.drop_collection('campaign')

    ### Inserir os dados na coleção "campaign" no banco de dados MongoDB
    campaign.insert_many(SEED_DATA)

    ### Fechar a conexão com o banco de dados
    client.close()

######################################################################

if __name__ == '__main__':
    print("\nInserindo dados na Coleção Campaign...\n")
    main()
