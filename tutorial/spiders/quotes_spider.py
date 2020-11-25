import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://scienti.minciencias.gov.co/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0001366840',
    ]

    def parse(self, response):
        
        #content = response.xpath("//td[a[@name='datos_generales']]")
        #cols = content.xpath('table//tr//td//text()').extract()

        #for td in cols:
        #   self.log(' '.join(td.split()))

        content = response.xpath("//table[tr[td[contains(.//text(), 'Líneas de investigación')]]]/tr/td")
        
        for c in content:
            elem = c.xpath("li/text()").get()

            if elem:
                self.log(elem)


    

