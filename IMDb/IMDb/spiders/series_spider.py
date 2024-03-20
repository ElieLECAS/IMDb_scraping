import scrapy
from IMDb.items import SerieItem

class SeriesSpiderSpider(scrapy.Spider):
    name = "series_spider"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"]

    def parse(self, response):
        series = response.css('li.ipc-metadata-list-summary-item')
        for serie in series:
            # yield{
            #     'name' : serie.css('div.ipc-metadata-list-summary-item__c div div div a.ipc-title-link-wrapper h3::text').get()
            # }
            relative_url = serie.css('div.ipc-metadata-list-summary-item__c div div div a.ipc-title-link-wrapper::attr(href)').get()
            serie_url = 'https://www.imdb.com/' + relative_url
            yield response.follow(serie_url, callback=self.parse_serie_page)

    def parse_serie_page(self,response):
        bandeau = response.css('div:has(span.hero__primary-text)')
        ulul = bandeau.css('ul.ipc-inline-list.ipc-inline-list--show-dividers:has(li.ipc-inline-list__item)')
        informations = response.css("section:has(div.ipc-chip-list--baseAlt.ipc-chip-list)")
        serie_item = SerieItem()

        serie_item["title"] = bandeau.css("div h1 span.hero__primary-text::text").get()
        serie_item["score"] = bandeau.css("span.ipc-btn__text div div div span::text").get()
        serie_item["genre"] = informations.css("div.ipc-chip-list--baseAlt.ipc-chip-list div a.ipc-chip.ipc-chip--on-baseAlt span::text").get()
        serie_item["year"] = ulul[1].css("li.ipc-inline-list__item:nth-of-type(2) a.ipc-link.ipc-link--baseAlt.ipc-link--inherit-color::text").get()
        serie_item["public"] = ulul[1].css("li.ipc-inline-list__item:nth-of-type(3) a.ipc-link.ipc-link--baseAlt.ipc-link--inherit-color::text").get()
        serie_item["duration"] = ulul[1].css("li.ipc-inline-list__item:nth-of-type(4)::text").get()
        serie_item["episodes"] = response.css("section.ipc-page-section.ipc-page-section--base div.ipc-title.ipc-title--base.ipc-title--section-title.ipc-title--on-textPrimary h3.ipc-title__text span.ipc-title__subtext::text").get()
        serie_item["seasons"] = response.css("span.ipc-simple-select.ipc-simple-select--base.ipc-simple-select--on-accent2 label.ipc-simple-select__label::text").get()
        serie_item["description"] = informations.css('div p span::text').get()
        serie_item["creator"] = informations.css("div:has(li.ipc-metadata-list__item) ul li.ipc-metadata-list__item  a.ipc-metadata-list-item__list-content-item.ipc-metadata-list-item__list-content-item--link::text").get() 
        serie_item["actors"] = informations.css("li.ipc-metadata-list__item.ipc-metadata-list-item--link:has(a.ipc-metadata-list-item__list-content-item.ipc-metadata-list-item__list-content-item--link) div ul.ipc-inline-list.ipc-inline-list--show-dividers.ipc-inline-list--inline.ipc-metadata-list-item__list-content li.ipc-inline-list__item a.ipc-metadata-list-item__list-content-item.ipc-metadata-list-item__list-content-item--link::text").getall()
        serie_item["country"] = response.css('li.ipc-metadata-list__item  div.ipc-metadata-list-item__content-container ul.ipc-inline-list.ipc-inline-list--show-dividers.ipc-inline-list--inline.ipc-metadata-list-item__list-content li.ipc-inline-list__item a[href*="country"]::text').get()
        
        yield serie_item