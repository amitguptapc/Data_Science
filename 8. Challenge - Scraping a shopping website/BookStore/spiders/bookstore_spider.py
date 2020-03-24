import scrapy
import pandas as pd

class BookSpider(scrapy.Spider):
    name = "bookstore"

    book_details={}

    def start_requests(self):
        urls = [
            'http://books.toscrape.com/'
        ]

        global book_details
        book_details={
            'image_url':[],
            'book_title':[],
            'product_price':[]
        }

        # Generator Function
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for q in response.css("article.product_pod"):
            img = q.css('a img::attr(src)').get()
            title = q.css('h3 a::attr(title)').get()
            price = q.css('div p.price_color::text').get()
            book_details['image_url'].append(img)
            book_details['book_title'].append(title)
            book_details['product_price'].append(price)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page=response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)
        else:
            df = pd.DataFrame(book_details)
            df.to_csv('../../book_details.csv',index=False)
