# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:00:00 2018
@author: Jonathan Ferreira
"""

import scrapy


class infojobsSpider(scrapy.Spider):
    name = 'vagas'
    start_urls = ['http://www.infojobs.com.br/vagas-de-emprego-cientista+de+dados.aspx/']

    def parse(self, response):
        vagas =  response.xpath('//div[contains(@class, "js_detailGrid") and not(contains(@class, "premiumLimited"))]')
        for vagas in vagas:
            url = vagas.xpath('./div[2]/a/@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_detail)

        proxima_pagina = response.xpath('//a[contains(@id, "ctl00_phMasterPage_cGrid_Paginator1_lnkNext")]/@href').extract_first()

        if proxima_pagina:
            proxima_pagina = 'http://www.infojobs.com.br/'+proxima_pagina
            yield scrapy.Request(
                url=proxima_pagina, callback=self.parse
            )

    def parse_detail(self, response):

        titulo = response.xpath('//span[contains(@id, "ctl00_phMasterPage_cVacancySummary_litVacancyTitle")]/text()').extract_first()

        descricao = response.xpath('//ol[contains(@class, "descriptionItems")]/li/text()').extract()
        descricao_total = ' '.join(descricao)

        url = response.url
        empresa = response.xpath('//a[contains(@id, "ctl00_phMasterPage_cVacancySummary_aCompany")]/@title').extract_first()

        if empresa == None:
            empresa = 'Confidencial'

        localidade = response.xpath('//span[contains(@id, "ctl00_phMasterPage_cVacancySummary_litLocation")]/text()').extract_first()

        # tipo = response.xpath('//span[contains(@id, "ctl00_phMasterPage_cVacancySummary_litContractType")]/text()').extract_first()
        # salario = response.xpath('//span[contains(@id, "tl00_phMasterPage_cVacancySummary_litSalary")]/text()').extract_first()

        yield {
            'titulo': titulo,
            'descricao': descricao_total,
            'url': url,
            'empresa': empresa,
            'localidade': localidade,

            # 'tipo': tipo,
            # 'salário': salario,
        }