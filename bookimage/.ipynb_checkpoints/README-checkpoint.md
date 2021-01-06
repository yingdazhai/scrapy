# Scrapy CrawlSpider for Book Cover Images
This is a illustrative Scrapy project to scrape books information on a fake online bookstore from http://books.toscrape.com.
This project demonstrates how Scrapy can be used to scrape book cover images from websites by scraping the cover images  Image scraping in scrapy is similar to data scraping with just a few lines of code added to `settings.py` file where we utilize scrapy's out-of-box image pipeline.

This project is only meant for educational purposes.

## Spiders

This project contains one crawl spider and you can list them using the `list`
command:

    $ scrapy list
    crawlspider-image

`crawlspider-image` crawls all the book cover image urls stored in JSON file and captures all JPEG cover images in a subfolder.

## Running the spiders

You can run the crawl spider using the `scrapy crawl` command, such as:

    $ scrapy crawl crawlspider-image -o crawlspider-image.json
