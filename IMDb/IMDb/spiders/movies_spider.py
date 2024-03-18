import scrapy
from IMDb.items import MovieItem

class MoviesSpiderSpider(scrapy.Spider):
    name = "movies_spider"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/?ref_=nv_mv_250"]

    def parse(self, response):
        movies = response.css('li.ipc-metadata-list-summary-item')
        for movie in movies:
            # yield{
            #     'name' : movie.css('div.ipc-metadata-list-summary-item__c div div div a.ipc-title-link-wrapper h3::text').get()
            # }
            relative_url = movie.css('div.ipc-metadata-list-summary-item__c div div div a.ipc-title-link-wrapper::attr(href)').get()
            movie_url = 'https://www.imdb.com/' + relative_url
            yield response.follow(movie_url, callback=self.parse_movie_page)

    def parse_movie_page(self,response):
        bandeau = response.css('div:has(span.hero__primary-text)')
        # informations = response.css("table tr")
        movie_item = MovieItem()

        movie_item["title"] = bandeau.css("div h1 span.hero__primary-text::text").get()
        # movie_item["score"] = informations[1].css("td::text").get()
        # movie_item["genre"] = response.css("p.price_color::text").get()
        # movie_item["year"] = informations[2].css("ul.ipc-inline-list").get()
        # movie_item["duration"] = informations[3].css("td::text").get()
        # movie_item["description"] = informations[4].css("td::text").get()
        # movie_item["actors"] = informations[5].css("td::text").get()
        # movie_item["public"] = informations[6].css("td::text").get()
        # movie_item["country"] = response.css("p.star-rating").attrib["class"]
        
        yield movie_item