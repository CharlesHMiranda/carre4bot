# carre4bot

## Desafio da Digital Innovation One para a construção de um robô no _Telegram_ para o Carrefour.

**As escolhas:**

Em um ambiente corporativo as decisões são baseadas na fórmula mais ortodoxa possível, ou seja, as pessoas optam por escolher a linguagem de 
programação que sua equipe ou ela própria mais domina, o banco de dados da instalação, e assim por diante.

Já em um cenário acadêmico podemos ser mais ousados e fazer nossas escolhas com o objetivo de ser inovador. Buscar o ineditismo. Enfim, trazer a 
inovação para dentro do seu projeto.

Nesse contexto, escolhi a linguagem de programação que menos tinha intimidade e um tipo de banco de dados (não relacional) que ainda não havia feito 
uso, em minha jornada profissional. Tais escolhas me obrigavam "reinventar" a forma de pensar e agir. E isso é um tremendo combustível para uma 
mente em ebulição.

Minha primeira definição dentro desse projeto foi de que deveria ser uma aplicação hospedada em uma nuvem e que seu funcionamento fosse 24/7.

Por que Python? Basta uma simples pesquisa no Google para verificar que essa linguagem é sempre mencionada quando o assunto é Inteligência Artificial. 
Com um olhar mais adiante, é fácil perceber que a evolução de qualquer projeto de um "robô" deve levar a IA, ou "AI", em consideração, mesmo que isso não 
se concretize no curto prazo.

Tendo essas premissas como um norte, uma direção a ser seguida, as escohas foram **Python**, **MongoDb** (bd e nuvem) e **Heroku** para hospedar o aplicativo. 

carre**4**bot foi desenvolvido tendo em mente a necessidade de performance. Seu código busca a linearidade para oferecer o menor tempo de resposta possível, 
sua estrutura é simples e lastreada em dois conjuntos de _try/catch_ (o último dentro de um _loop_ infinito), faz uso de apenas duas pequenas coleções em um banco de dados **MongoDB** na nuvem - sendo a primeira, uma coleção de campanhas, suas palavras-chave, 
um _emoticon_ e a mensagem/link promocional e a segunda coleção é apenas um registro de campanhas enviadas no dia por _chat_id_ (trata-se de uma coleção que pode 
ser esvaziada diariamente, removendo-se os registros do dia anterior) - e os códigos-fonte estão hospedados no [GitHub](https://github.com/CharlesHMiranda/carre4bot).


## Próximos passos

Estou desenvolvendo o _fullstack CRUD_ para gerenciar a coleção de campanhas, com todas as validações de entrada de dados necessárias, baseado em Angular 8, JavaScript e Node.js.

Pretendo, ainda, e mais para a frente, me aprofundar em Inteligência Artificial e fazer uso do _Deep Learning_ para que o robô ofereça um diálogo ainda mais _humanizado_ com seus usuários.

## APP

O **bot**, após ser inserido no grupo ou no _chat_, restringe o seu funcionamento ao monitoramento das mensagens de texto trocadas entre os participantes daquela conversa. 
Ele descarta todos os demais envios, tais como: imagens, vídeos, figuras animadas e textos com mais de 250 caracteres (os famosos "textões" que quase ninguém lê).

Em seguida, remove todos os caracteres especiais que podem comprometer as _queries_ ao banco de dados, toda a cadeia de palavras é convertida para minúsculas e 
suas palavras separadas e inseridas em um _array_ iterável.

Cada elemento do _array_ fará parte de uma _query_ a ser formulada às palavras-chave das Campanhas. Por questões de performance, o aplicativo limita-se a buscar apenas 
pela primeira pesquisa atendida, envia a mensagem caso ainda não tenha sido exibida naquele dia e naquele _chat_ e retorna ao seu estado de monitoramento.

Tal comportamento é necessário para não incomodar os participantes com um possível excesso de intervenções do "robô" nas conversas ou nos grupos. Evitando, assim, que seja removido pelos seus usuários.
O objetivo a ser alcançado é que sua participação seja **leve** e **divertida**.

O **App** está hospedado como um aplicativo no repositório **Heroku**, encontra-se em execução 24/7 e, portanto,  pode ser adicionado ao seu 
grupo familiar ou profissional no _Telegram_ por meio do nome: **@carre4bot**

Para aferir o desempenho do "robô" é necessário conhecer as palavras-chave monitoradas que estão descritas no arquivo`campaignDBInsert.py`, na pasta `src/repository`, 
responsável pela inserção da massa de testes no banco de dados.

### As coleções utilizadas em banco de dados MongoDB são:

| Nome           | Tipo             | Descrição                                                                                                                                |
| -------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| campaignlog    | log (registro)   | Registra o envio de campanhas para aquele usuário ou grupo. Sua chave de acesso é: "chat_id + data_atual + campanhaId"                   |
| campaign       | descritivo       | Cada documento contém a identificação da campanha, palavras-chave, mensagem e uma URL do e-commerce do Carrefour.|

### Descrição da _Coleção_ `campaign`

| Nome     | Descrição                                   |
| -------- | ------------------------------------------- |
| campaign | `id` Identificador da Campanha                |
| name     | `nome` da Campanha (ex: "Dia dos Pais")       |
| emoticon | `emoticon` da Campanha (ex: '[̲̅$̲̅(ツ)$̲̅]')        |
| slogan   | `slogan` que melhor representa a Campanha     |
| keywords | `palavras-chave` atreladas ao monitoramento   |
| link     | `URL HTTP` Elo de ligação com o e-commerce    |

### Descrição da _Coleção_ `campaignlog`

| Nome     | Descrição                                   |
| -------- | ------------------------------------------- |
| id       | chat_id + dataInvertida + CampanhaId        |


#### Exemplo de consumo da execução da aplicação na nuvem do `Heroku`

Free dyno hours quota remaining this month: 549h 54m (99%)
Free dyno usage for this app: 0h 3m (0%)
For more information on dyno sleeping and how to upgrade, see:
https://devcenter.heroku.com/articles/dyno-sleeping

=== worker (Free): python src/core.py (1)
worker.1: up 2020/07/30 15:04:00 -0300 (~ 2h ago)
