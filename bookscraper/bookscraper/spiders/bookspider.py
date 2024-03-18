import scrapy
from bookscraper.items import BookItem

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css('article.product_pod')
        for book in books:
            relative_url = book.css('h3 a ::attr(href)').get()

            if 'catalogue/' in relative_url:
                book_url = 'https://books.toscrape.com/' + relative_url
            else:
                book_url = 'https://books.toscrape.com/catalogue/' + relative_url
            yield response.follow(book_url, callback=self.parse_book_page)

        next_page = response.css("li.next a ::attr(href)").get()
        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url = 'https://books.toscrape.com/' + next_page
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
            yield response.follow(next_page_url, callback=self.parse)

    def parse_book_page(self,response):
        
        informations = response.css("table tr")
        book_item = BookItem()

        book_item["title"] = response.css(".product_main h1::text").get()
        book_item["product_type"] = informations[1].css("td::text").get()
        book_item["price"] = response.css("p.price_color::text").get()
        book_item["price_excl_tax"] = informations[2].css("td::text").get()
        book_item["price_incl_tax"] = informations[3].css("td::text").get()
        book_item["tax"] = informations[4].css("td::text").get()
        book_item["availability"] = informations[5].css("td::text").get()
        book_item["number_of_reviews"] = informations[6].css("td::text").get()
        book_item["stars"] = response.css("p.star-rating").attrib["class"]
        
        yield book_item
        