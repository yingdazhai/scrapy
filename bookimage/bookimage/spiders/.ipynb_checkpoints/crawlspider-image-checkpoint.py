import scrapy
# Scrapy's `CrawlSpider` spider class could enable LinkExtractor to crawl pages
from scrapy.linkextractors import LinkExtractor
# more importantly, `CrawlSpider` allows us to define specific crawling rules 
from scrapy.spiders import CrawlSpider, Rule
# scrapy.Item is used for parsed data instead of yielding dictionary directly
from ..items import ImagesItem


class BookImageCrawlSpider(CrawlSpider):
    # This CrawlSpider captures all book covers and store images in a subfolder `/covers`
    name = "crawlspider-bookimage"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"] 
    # `CrawlSpider` comes with rules that need to be defined, e.g. here, only crawl `~/catalogue/page-\d+.html`
    rules = (Rule(LinkExtractor(allow=r"catalogue/page-\d+.html"), callback="parse_bookimage", follow=True),)
    
    def parse_bookimage(self, response):
        # `parse_bookmage` captures 
        if response.css('.thumbnail').getall() is not None:
            for book in response.css('.thumbnail'):
                img = book.css('.thumbnail::attr(src)').get()
                # `imagere_urls` in ImageItems pipeline needs absolute image path
                img_url = response.urljoin(img)
            
                image = ImagesItem()
                # "image_urls" must be a list
                image["image_urls"] = [img_url]  
                yield image
            

