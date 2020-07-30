# carre4bot

## Desafio para a construção de um robô no _Telegram_ para o Carrefour.

carre**4**bot foi desenvolvido em **Python** tendo em mente a necessidade de performance. O "bot" faz uso de 2 coleções em um banco de dados **MongoDB** hospedado na nuvem. E os códigos-fonte estão hospedados no [GitHub](https://github.com/CharlesHMiranda/carre4bot).

## APP

O **bot** está hospedado como um aplicativo (app) no repositório **Heroku**, encontra-se em execução 24/7 e, portanto,  pode ser adicionado ao seu grupo familiar ou profissional no _Telegram_ por meio do nome: **@carre4bot**

### As coleções utilizadas em um banco de dados "não relacional" (MongoDB) são:

| Nome           | Tipo             | Descrição                                                                                                                              |
| -------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| campaignlog    | log (registro)   | Registra o envio de campanhas para aquele usuário ou grupo. Sua chave de acesso é: "chat_id + data + campanha"                         |
| campaign       | descritivo       | Campanhas cadastradas, cada documento contém a identificação da campanha, palavras-chaves e uma URL do e-commerce do Carrefour.        |


#### Exemplo de consumo da execução da aplicação na nuvem do `Heroku`

Free dyno hours quota remaining this month: 549h 54m (99%)
Free dyno usage for this app: 0h 3m (0%)
For more information on dyno sleeping and how to upgrade, see:
https://devcenter.heroku.com/articles/dyno-sleeping

=== worker (Free): python src/core.py (1)
worker.1: up 2020/07/30 15:04:00 -0300 (~ 2h ago)

### Descrição do CRUD em Angular8 da _Coleção_ `promos`

| Nome   | Descrição                                      |
| ------ | ---------------------------------------------- |
| id     | `id` corresponde ao identificador (se existir) |
| number | `number` atributo para acesso ao campo         |
| status | HTTP status da chamada da API                  |
