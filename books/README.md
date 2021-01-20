# Scrapy Spider for Books
This is a illustrative Scrapy project to scrape books information on a fake online bookstore from http://books.toscrape.com. Another example of scrapy spider on http://quotes.toscrape.com, see details in ([github repo].(https://github.com/scrapinghub/spidyquotes)).

This project is only meant for educational purposes.


## Extracted data

This project extracts book information, combined with the respective titles, price, ratings, etc.
The extracted data looks like this sample:

    {
        'title': 'Libertarianism for Beginners',
        'price': '£51.33',
        'rating': '2',
        'desc': 'Libertarianism isn't about winning elections; it is first and foremost a political philosophy--a description of how, ... more',
        'upc': 'a18a4f574854aced',
        'avail': 'In stock',
        'stock': '19',
        'nreview': '0',
    }


## Spiders

This project contains three spiders and you can list them using the `list`
command:

    $ scrapy list
    spider-books
    spider-bookinfo
    crawlspider-bookinfo

First basic spider `spider-books` crawls basic book information on pagination while the second basic spider `spider-bookinfo` crawls on individual book page and extracts more information. The third crawl spider `crawlspider-bookinfo` extracts exactly the same information as in the second spider, with defined crawling rules enabled by `CrawlSpider` type in scrapy and Item pipeline.

## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl spider-books

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl spider-books -o books.csv
