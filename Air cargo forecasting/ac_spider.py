import scrapy

class AirCargoScraper(scrapy.Spider):
    name = 'air-cargo-table'
    start_urls = ['https://www.transtats.bts.gov/freight.asp']
    
    def start_requests(self):
        url = 'https://www.transtats.bts.gov/freight.asp'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        headers = response.xpath('//*[@class="largeTABLE"]//th[@class="libraryTHY2" and not(@colspan="5")]')
        columns = [h.xpath('text()').extract_first() for h in headers]
        columns = columns[:2] + columns[3:] + [columns[2]]
        
        data = response.xpath('//*[@class="largeTABLE"]//tr[not(@style="background-color:#fafed6;")]//td[contains(@class, "dataTD")]')[2:]
        for i in range(0, len(data), len(columns)):
            d = {}
            for j in range(len(columns)):
                d[columns[j]] = str.replace(data[i+j].xpath('text()').extract_first(), ',', '')
            yield d