# coding: utf-8

import scrapy    # `scrapy` library in Python
import re    # regular expression (RegEx)

class BooksSpider(scrapy.Spider):
    name = "spider-books"
    
    # use the default `start_request` by passing urls to `start_urls` class attributes
    start_urls = ['http://books.toscrape.com/catalogue/page-1.html']
    
    def parse(self, response):
        """
        # create file names and save the HTML files for all 10 page in subfolder
        page = re.search(r'page-(\d+.html)', response.url).group(1)
        filename = f'books-{page}'
        with open(filename, 'wb') as f:
            f.write(response.body)
        """
        # select and extract book's title, rating, price and availability as dict using CSS selector
        for book in response.css('.col-lg-3'):
            yield {
                'title': book.css('.product_pod a::text').get(),
                'rating': book.css('.star-rating::attr(class)').get().split(r" ")[-1] + ', out of Five',
                'price': book.css('.price_color::text').get(),
                'avail': " ".join(book.css(".availability::text")[1].re(r'\w+')),
            }
        # schedule request for the "Next" page for pagination   
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            






