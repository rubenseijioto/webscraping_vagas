"""
@author: Rubens
"""
import scrapy
from unicodedata import normalize

class VagasSpider(scrapy.Spider):
    name = "vagas"

    start_urls = [
        'http://www.pyjobs.com.br/?search=cientista+de+dados'
    ]

    def parse(self, response):
        for vaga in response.css('div.card-body'):
            titulo = vaga.css('h4::text').extract_first()
            if 'cientista' in titulo.lower():
                titulo = normalize('NFKD', titulo).encode('ASCII', 'ignore').decode('ASCII')
                local = vaga.css('h6::text').extract_first()
                local = normalize('NFKD', local).encode('ASCII', 'ignore').decode('ASCII')
                yield {
                   'vaga': titulo,
                   'localizacao': local,
                   'link': 'http://www.pyjobs.com.br' + vaga.css('a::attr(href)').extract()[0],
                      }

            

   
