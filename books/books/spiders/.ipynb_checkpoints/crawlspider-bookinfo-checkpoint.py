import scrapy
# Scrapy's `CrawlSpider` spider class could enable LinkExtractor to crawl pages
from scrapy.linkextractors import LinkExtractor
# more importantly, `CrawlSpider` allows us to define specific crawling rules 
from scrapy.spiders import CrawlSpider, Rule
# scrapy.Item is used for parsed data instead of yielding dictionary directly
from ..items import BooksItem
from word2number import w2n   # (optional) convert num word to int
import re


class BookInfoCrawlSpider(CrawlSpider):
    # Yet another way to crawl exactly same data from each inidividual book page with `CrawlSpider` rather than basic spider.
    name = "crawlspider-bookinfo"
    allowed_domains = ["books.toscrape.com"]
    
    # `CrawlSpider` comes with rules that need to be defined, e.g. here, all pages and subpages `~/catalogue/`
    rules = (Rule(LinkExtractor(allow=r"catalogue/"), callback="parse_books", follow=True),)

    def start_requests(self):
        url = "http://books.toscrape.com/"
        yield scrapy.Request(url)

    def parse_books(self, response):
        # define a helper for extraction
        def css_helper(query):
            return response.css(query).get(default='').strip()

        # select elements using CSS and observe that we only parse on existing pages and avoid "NotFound" error
        book_page_only = response.css('#product_gallery').get()
        if book_page_only:
            title = css_helper('h1::text'),
            price = css_helper('.price_color::text'),
            rating = w2n.word_to_num(css_helper('.star-rating::attr(class)').split(r" ")[-1]),
            desc = css_helper('#product_description + p::text'),
            upc = css_helper('tr:nth-child(1) td::text'),
            avail = response.css('tr:nth-child(6) td::text').re_first(r'([\w\s]+)\s\('),
            stock = response.css('tr:nth-child(6) td::text').re_first(r'\(([^)]+)\)').split(" ")[0],
            nreview = css_helper('tr:nth-child(7) td::text')

            # yield the extracted data as scrapy.Item object.
            item = BooksItem()
            item["title"] = title
            item["price"] = price
            item["rating"] = rating
            item["desc"] = desc
            item["upc"] = upc
            item["avail"] = avail
            item["stock"] = stock
            item["nreview"] = nreview
            yield item
