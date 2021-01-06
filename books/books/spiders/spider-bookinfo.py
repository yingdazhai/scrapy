import scrapy    # `scrapy` library in Python
import re    # regular expression (RegEx)
from word2number import w2n   # (optional) convert num word to int


class BookInfoSpider(scrapy.Spider):
    # An alternative spider for more detailed book info crawling on pages of each book with CrawlRules
    name = 'spider-bookinfo'
    
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    
    """
    # customize setting at spider-level
    custom_settings = {
        # wait 1 sec before next download 
        "DOWNLOAD_DELAY": 1,
        "RANDOMIZE_DOWNLOAD_DELAY": False,
        # other settings ... 
    }
    """
    
    def parse(self, response):
        book_page_links = response.css('.image_container a')
        yield from response.follow_all(book_page_links, self.parse_book)
        
        pagination_links = response.css('li.next a')
        yield from response.follow_all(pagination_links, self.parse)
            
    def parse_book(self, response):
        # define a helper for extraction
        def css_helper(query):
            return response.css(query).get(default='').strip()
        # extract book info, including titles, price, stock#, UPC, prod_type, #review and prod_desc, etc.
        yield {
            'title': css_helper('h1::text'),
            'price': css_helper('.price_color::text'),
            'rating': w2n.word_to_num(css_helper('.star-rating::attr(class)').split(r" ")[-1]),
            'desc': css_helper('#product_description + p::text'),
            'upc': css_helper('tr:nth-child(1) td::text'),
            'avail': response.css('tr:nth-child(6) td::text').re_first(r'([\w\s]+)\s\('),
            'stock': response.css('tr:nth-child(6) td::text').re_first(r'\(([^)]+)\)').split(" ")[0],
            'nreview': css_helper('tr:nth-child(7) td::text'),
        }

