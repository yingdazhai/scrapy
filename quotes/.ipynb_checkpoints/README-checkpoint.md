# Scrapy Spider for Quotes
This is a illustrative Scrapy project to scrape quotes from http://books.toscrape.com. See a step-by-step tutorial in [scrapy tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html) and other similar example of quote bots are availabile in ([github repo](https://github.com/scrapinghub/spidyquotes)).

This project is only meant for educational purposes.


## Extracted data

This project extracts quotes, combined with the respective text, author, tags and author's details etc.
The extracted data looks like this sample:

    {
        'text': 'The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.',
        'author': 'Albert Einstein',
        'tags': ['change', 'deep-thoughts', 'change', 'world']
    }


## Spiders

This project contains two spiders and you can list them using the `list`
command:

    $ scrapy list
    author
    quotes

First spider `author` crawls author information including name, birthday, short bio. The second spider `quotes` crawls on quote text, author and tags.

## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl quotes

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl quotes -o quotes.csv