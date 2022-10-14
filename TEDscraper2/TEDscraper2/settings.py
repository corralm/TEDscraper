# Scrapy settings for TEDscraper2 project

BOT_NAME = 'TEDscraper2'

SPIDER_MODULES = ['TEDscraper2.spiders']
NEWSPIDER_MODULE = 'TEDscraper2.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Add 250ms wait before downloading consecutive pages
DOWNLOAD_DELAY = 0.25