import scrapy
import re
from ..items import PlayerItem

class FifaSpider(scrapy.Spider):
    name = 'spider-fifa'
    allowed_domains = ['sofifa.com']
    start_urls = ['https://sofifa.com/?offset=0']
    
    custom_settings = {
    # specifies exported fields and order, especially for csv
    'FEED_EXPORT_FIELDS': ['name','country','position','age','overall_rating','potential','club','value','wage','total_stats','hits'],
    }
    
    def parse(self, response):
        # select and crawl each player in the table 
        for player in response.css('tbody.list tr'):            
            item = PlayerItem()
            item['name'] = player.css('.col-name .tooltip .bp3-text-overflow-ellipsis::text').get().strip()
            item['country'] = player.css('.col-name .tooltip .bp3-text-overflow-ellipsis img::attr(title)').get()
            # watch out for position, we need to iterate on `nth-child()`:,e.g. 10n+1: 1,11,21,..; 1n+1, 1,2,3,...
            item['position'] = player.css('tr:nth-child(1n+1) .pos::text').getall()
            item['age'] = player.css('td.col-ae::text').get()
            item['overall_rating'] = player.css('td.col-oa ::text').get()
            item['potential'] = player.css('td.col-pt ::text').get()
            item['club'] = player.css('.bp3-text-overflow-ellipsis a::text').get()
            item['value'] = player.css('td.col-vl ::text').get()
            item['wage'] = player.css('td.col-wg::text').get()
            item['total_stats'] = player.css('td.col-tt ::text').get()
            item['hits'] = player.css('td.col-comment ::text').re_first(r'[\w.]+')
            yield item
            
        next_page = response.xpath('//span[@class="bp3-button-text" and text()="Next"]/parent::a/@href').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))