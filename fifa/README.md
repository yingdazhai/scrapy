# Scrapy Spider for FIFA Players
This is a illustrative Scrapy project to scrape soccer player's information registered on the website (http://sofifa.com)[http://sofifa.com]. Given this is an operating commercial webiste, please be polite regarding your scraping activity. In `settings.py`, 

```python 
# Obey robots.txt rules
ROBOTSTXT_OBEY = True
# Prolong waitng time between downloads
DOWNLOAD_DELAY = 3
```
This project is only meant for educational purposes.

## Extracted data

This project extracts player's name, country, age, club, stats, etc.
The extracted data looks like this sample:

    {
         'age': '20',
         'club': 'Olympique de Marseille',
         'country': 'France',
         'hits': '123',
         'name': 'B. Kamara',
         'overall_rating': '79',
         'position': ['CDM', 'CB'],
         'potential': '85',
         'total_stats': '1902',
         'value': '€25M',
         'wage': '€29K'
    }


## Spiders

This project contains one basic spider and you can list them using the `list`
command:

    $ scrapy list
    spider-fifa

The basic spider `spider-fifa` crawls player's information in the tabulated player's panel from (http://sofifa.com)[http://sofifa.com] and continues on the following pages.

## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl spider-fifa

If you want to save the scraped data to a file, you can pass the `-O` option (Feed Export and replace):
    
    $ scrapy crawl spider-fifa -O players.csv