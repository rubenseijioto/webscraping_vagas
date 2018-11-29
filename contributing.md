# Contribuição

Para contribuir com o projeto você deve seguir algumas guidelines.

1. Faça o fork do repositório para o seu git.
2. Acesse a pasta com o nome do site que irá raspar e construa o código mantendo as estruturas estabelecidas. Contudo é importante que você nomeie as classes/variáveis/arquivos para que corresponda ao site o qual você esteja fazendo scrap.
````py
class VagasItem(scrapy.Item):
    name = scrapy.Field()

class VagasPipeline(object):
    def process_item(self, item, spider):
        return item
````
>No exemplo acima por exemplo substitua **Vagas** pelo nome do site que você irá raspar.
3. Modifique o arquivo **CONTRIBUTORS** com seu nome sobrenome na área indicada pelo nome do site que você tenha raspado. Modifique também o arquivo **Readme.md** acrescendo o *"em progresso"* na frente do nome do site que você realizou o scrap.
4. Faça o *pull request* após as modificações.

## Observações
* Caso queira incluir algum site que não tenhamos considerado abra uma issue para que todos sejam informados.
* Não modifique uma pasta que não seja a do seu time, a menos que o líder dessa pasta conceda permissão para trabalhar nela.
* Caso tenha encontrado algo errado em alguma pasta, código ou arquivo que não esteja sobre a sua resposabilidade por favor abra uma issue.
* Siga a estrutura pre-estabelecida e as guidelines para que tudo fique bem organizado.
