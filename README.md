## Web Scraping with Python Scrapy

[Python Scrapy](https://scrapy.org) is the "go-to" end-to-end framework for flexible web data colletion from data scraping and cleaning to saving and preparation, where popular utility packages such as [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) could be easily integrated. 

[Scrapy Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html) provides a comprehensive guide on how to build scrapy web crawlers for data collection with easy-to-follow examples. 

This scrapy project contains 5 example scrapy projects written in Python scrapy, demonstrating how scrapy works for web data collection.

1. **Scraping multiple quotes**: extract text data of famous quotes - [quotes](https://github.com/yingdazhai/scrapy.git/tree/master/quotes).
2. **Scraping a bookstore** extract book details and cover images from a dummy online book store - [books](https://github.com/yingdazhai/scrapy.git/tree/master/books) and [bookimage](https://github.com/yingdazhai/scrapy.git/tree/master/bookimage).
3. **Scraping soccer players** - extract player's information and photos registered on `sofifa.com` website - [fifa](https://github.com/yingdazhai/scrapy.git/tree/master/fifa) and [fifaimage](https://github.com/yingdazhai/scrapy.git/tree/master/fifaimage).
   
To run these examples, [Scrapy](https://docs.scrapy.org/en/latest/) needs to be installed. Scrapy can be installed either through anaconda or pip.

```bash
$ conda install -c conda-forge scrapy
```
or

```bash
$ pip install Scrapy
```

For installing on other OS and any other installation queries, please click [here](https://docs.scrapy.org/en/latest/intro/install.html).

Details on how to run individual examples are provided in dedicated README.md files inside these 5 projects.