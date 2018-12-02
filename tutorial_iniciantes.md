# Tutorial para iniciantes
Esse é um tutorial bem básico sobre o uso do Scrapy. Cada site a ser raspado tem as sua peculiaridades, por isso é importante ficar atento.  
Boa parte do que aprendi eu vi nessa playlist, que é bem didádica: [Learn Scrapy](https://www.youtube.com/playlist?list=PLZyvi_9gamL-EE3zQJbU5N3nzJcfNeFHU)

**Passo a passo:**
1. A instalação, não tem muito segredo. Basta seguir a [documentação oficial](https://doc.scrapy.org/en/latest/intro/install.html).
2. Como instalei o scrapy em outro environment, a primeira coisa a fazer é ativar o environment
![Ativar Environment](https://i.imgur.com/K9qgu3A.png)  
Se você não sabe o que é um environment e quer saber, leia esse artigo: [Why you need Python environments and how to manage them with Conda](https://medium.freecodecamp.org/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c)
3. Em seguida você pode iniciar um projeto usando o comando: `scrapy startproject spider_name`. Substituindo `spider_name` pelo nome que você quer dar para sua spider.
![Criar Projeto](https://i.imgur.com/xIDYfW8.png)
4. Assim, será gerado um conjunto de pastas e arquivos próprios do scrapy. Como na imagem abaixo:
![Diretório do projeto](https://i.imgur.com/vWDjHHC.png)
5. Utilizamos o comando `cd nome_pasta` para entrarmos no diretório do projeto. Onde `nome_pasta` é o nome da pasta do projeto.
6. Em seguida podemos gerar nossa primeira spider usando o comando `scrapy genspider FirstSpider example.com`. Substituindo `FirstSpider` pelo nome da sua spider e `example.com` pelo site que você deseja raspar.
![Criar primeira spider](https://i.imgur.com/VlMq5bK.png)
7. Agora vem o trabalho propriamente dito. Você tem que procurar no código do site os elementos que queira encontrar e usá-los corretamente no código. 
Como essa parte é mais complexa de colocar aqui, eu recomendo que você assita a [playlist indicada](https://www.youtube.com/playlist?list=PLZyvi_9gamL-EE3zQJbU5N3nzJcfNeFHU) em conjunto com esse tutorial: [Using Scrapy to Build your Own Dataset](https://towardsdatascience.com/using-scrapy-to-build-your-own-dataset-64ea2d7d4673).  
O motivo de estudar os dois em conjunto é que a playlist fornece uma base e o tutorial complementa explicando sobre o uso do arquivo `items.py`.
8. Quando o código estiver pronto você pode usar o terminal para navegar até a pasta spiders e gerar um arquivo `.csv` com os dados raspados.
Basta usar o comando `scrapy crawl FirstSpider example.csv`, substituindo `FirstSpider` pelo nome da sua spider e `example.csv` pelo nome que queira dar para o arquivo.  
**Obs.:** O meu arquivo .csv gerado está deixando uma linha em branco após cada linha com conteúdo. Até o presente momento não consegui resolver esse problema, então se você souber pode me falar ;)

## Bonus - scrapy shell é o seu amigo
Usando o comando `scrapy shell example.com` no terminal, você vai abrir um shell interativo que vai te permitir testar rapidamente se o *css selector* e *xpath* que você usou estão selecionando corretamente os elementos desejados.
Após a execução do código diversas informações serão exibidas e ao final alguns comandos que poderão ser executados no shell.
Pode não fazer muito sentido em um primeiro momento, mas você vai ver que esse recurso é ótimo para verificar se você está usando corretamente os comandos para raspar o que deseja.
![Comando shell do scrapy](https://i.imgur.com/r9Mxjhu.png)

Espero que esse tutorial tenha te ajudado, e qualquer coisa pode entrar em contato comigo. Mas acredito que o *google* e o *stackoverflow* poderão resolver a maioria dos seus problemas.
