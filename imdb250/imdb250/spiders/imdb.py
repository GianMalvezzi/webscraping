import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):

        for value in response.css('.titleColumn'):
            yield{

                'movie' : value.css('.titleColumn a::text').get(),
                'year' : value.css('.secondaryInfo::text').get(),
                'rate' : response.css('strong::text').get()
            }
            pass



