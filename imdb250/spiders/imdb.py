import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://m.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
        for anoLancamento in response.css('.unbold+ .unbold'):
            yield {
                'ano': response.css('.unbold+ .unbold::text').get(),
                'nota': response.css('.imdb-rating::text').get()
            }
        pass
