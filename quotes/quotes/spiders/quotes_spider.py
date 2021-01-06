#!/usr/bin/env python
# coding: utf-8

# In[2]:


import scrapy
import os

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    # Approcch A: use the default `start_request` by passing urls to `start_urls` class attributes
    start_urls = ['http://quotes.toscrape.com/page/1/']
    
    """
    # Approach B: define `start_request` method using self-defined generators
    def start_requests(self):
        urls = ['http://quotes.toscrape.com/page/1/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)      
    """
    
    def parse(self, response):
        # create file names and save the HTML files for all 10 page in subfolder
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        #os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
        # Approach A: select and extract quote's text, author and tags as dict using CSS selector
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        """
        # Approach B: select and extract quote's text, author and tags as dict using XPath selector
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                'text': quote.xpath('./span[@class="text"]/text()').extract_first(),
                'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
                'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
            }
        """
        # schedule request for the "Next" page for pagination   
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            

class AuthorSpider(scrapy.Spider):
    name = 'author'

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        author_page_links = response.css('.author + a')
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.css('li.next a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }




