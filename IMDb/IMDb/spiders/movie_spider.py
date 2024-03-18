import scrapy


class MovieSpiderSpider(scrapy.Spider):
    name = 'movie_spider'
    allowed_domains = ['www.imdb.com']
    start_urls = ['http://www.imdb.com/']

    def parse(self, response):
        pass
