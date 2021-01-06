# Scrapy Spider for FIFA Players
This is a illustrative Scrapy project to scrape soccer player's avatar images registered on the website (http://sofifa.com)[http://sofifa.com]. Given this is an operating commercial webiste, please be polite regarding your scraping activity. In `settings.py`, 

```python 
# Obey robots.txt rules
ROBOTSTXT_OBEY = True
# Prolong waitng time between downloads
DOWNLOAD_DELAY = 3
```
This project is only meant for educational purposes.

## Spiders

This project contains one basic spider and you can list them using the `list`
command:

    $ scrapy list
    spider-fifaimage

The basic spider `spider-fifa` crawls player's images in the tabulated player's panel from (http://sofifa.com)[http://sofifa.com] and continues on the following pages. The images will be saved in the subfolder `/avatars`.

## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl spider-fifaimage

If you want to save image urls to a file, you can pass the `-O` option (Feed Export and replace):
    
    $ scrapy crawl spider-image -O avatar_urls.json