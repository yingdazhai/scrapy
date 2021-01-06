import scrapy
import re
from ..items import ImagesItem

class FifaImageSpider(scrapy.Spider):
    name = 'spider-fifaimage'
    allowed_domains = ['sofifa.com']
    start_urls = ['https://sofifa.com/?offset=0']
    
    def parse(self, response):
        # select and crawl each player in the table 
        for player in response.css('tbody.list tr'):            
            # `data-src` gives the absolute image path
            img_url = player.css('.avatar img::attr(data-src)').get()
            image = ImagesItem()
            image["image_urls"] = [img_url] 
            yield image
            
        next_page = response.xpath('//span[@class="bp3-button-text" and text()="Next"]/parent::a/@href').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
