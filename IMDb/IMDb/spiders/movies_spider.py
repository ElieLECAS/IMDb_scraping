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
        ulul = bandeau.css('ul.ipc-inline-list.ipc-inline-list--show-dividers:has(li.ipc-inline-list__item)')
        informations = response.css("section:has(div.ipc-chip-list--baseAlt.ipc-chip-list)")
        movie_item = MovieItem()

        movie_item["title"] = bandeau.css("div h1 span.hero__primary-text::text").get()
        movie_item["score"] = bandeau.css("span.ipc-btn__text div div div span::text").get()
        movie_item["genre"] = informations.css("div.ipc-chip-list--baseAlt.ipc-chip-list div a.ipc-chip.ipc-chip--on-baseAlt span::text").get()
        movie_item["year"] = ulul[1].css("li.ipc-inline-list__item a.ipc-link.ipc-link--baseAlt.ipc-link--inherit-color::text").get()
        movie_item["public"] = ulul[1].css("li.ipc-inline-list__item:nth-of-type(2) a.ipc-link.ipc-link--baseAlt.ipc-link--inherit-color::text").get()
        movie_item["duration"] = ulul[1].css("li.ipc-inline-list__item:nth-of-type(3)::text").get()
        movie_item["description"] = informations.css('div p span::text').get()
        movie_item["creator"] = informations.css("div:has(li.ipc-metadata-list__item) ul li.ipc-metadata-list__item a.ipc-metadata-list-item__list-content-item.ipc-metadata-list-item__list-content-item--link::text").get() 
        movie_item["actors"] = informations.css("li.ipc-metadata-list__item.ipc-metadata-list-item--link:has(a.ipc-metadata-list-item__list-content-item.ipc-metadata-list-item__list-content-item--link) div ul.ipc-inline-list.ipc-inline-list--show-dividers.ipc-inline-list--inline.ipc-metadata-list-item__list-content li.ipc-inline-list__item a.ipc-metadata-list-item__list-content-item.ipc-metadata-list-item__list-content-item--link::text").getall()
        movie_item["country"] = response.css("ul.ipc-inline-list.ipc-inline-list--show-dividers.ipc-inline-list--inline.ipc-metadata-list-item__list-content base li.ipc-inline-list__item a.ipc-metadata-list-item__list-content-itemipc-metadata-list-item__list-content-item--link::text").get()
        
        yield movie_item