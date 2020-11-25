import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://scienti.minciencias.gov.co/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0001366840',
    ]

    def parse(self, response):
        
        content = response.xpath("//td[a[@name='datos_generales']]")
        cols = content.xpath('table//tr//td//text()').extract()

        for td in cols:
            self.log(' '.join(td.split()))

        #content = response.xpath("//table/tbody/tr[contains(td/h3/text(), 'Líneas de investigación')]/td/text()").extract()

        #self.log(content)

    

