from spiders.spiders.wikicityspider import WikiCitySpider
from spiders.spiders.zillowspider import ZillowcaSpider
from spiders.spiders.realestatespider import RealEstateSpider
from spiders.spiders.mortgagespider import MortgageRatesSpider
from spiders.spiders.airbnbspider import AirbnbSpider
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
from scrapy import signals
from twisted.internet import reactor, defer
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
import warnings, os
from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
from supportingfunctions.avg_price import city_avg_price_calculator
from supportingfunctions.yelp_data_cleaner_script import data_cleaner

def real_estate_spider():
  warnings.filterwarnings("ignore")
  wikicity_output = []

  def crawler_results(item, spider):
    if spider.name == 'wikicity':
      wikicity_output.append(item)

  dispatcher.connect(crawler_results, signal=signals.item_scraped)
  #The settings are required to override the default settings used
  #by the spiders.
  settings = {
    'SCRAPEOPS_API_KEY': os.getenv("SCRAPEOPS_API_KEY"),
    'SCRAPEOPS_FAKE_USER_AGENT_ENABLED': True,
    'DOWNLOADER_MIDDLEWARES': {
      'spiders.middlewares.ScrapeOpsFakeUserAgentMiddleware': 400,
      'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 401,
      'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 402,
      'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
      'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
    },
    'HEADERS': {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
      "Accept-Language": "en-US,en;q=0.5",
      "Accept-Encoding": "gzip, deflate",
      "Connection": "keep-alive",
      "Upgrade-Insecure-Requests": "1",
      "Sec-Fetch-Dest": "document",
      "Sec-Fetch-Mode": "navigate",
      "Sec-Fetch-Site": "none",
      "Sec-Fetch-User": "?1",
      "Cache-Control": "max-age=0",
    },
    'RETRY_ENABLED': True,
    'RETRY_TIMES': 1,
    'RETRY_HTTP_CODES': [500, 502, 503, 504, 522, 524, 408, 429, 403],
    'RETRY_PRIORITY_ADJUST': -1,
    'RETRY_EXCEPTIONS': [
      "twisted.internet.defer.TimeoutError",
      "twisted.internet.error.TimeoutError",
      "twisted.internet.error.DNSLookupError",
      "twisted.internet.error.ConnectionRefusedError",
      "twisted.internet.error.ConnectionDone",
      "twisted.internet.error.ConnectError",
      "twisted.internet.error.ConnectionLost",
      "twisted.internet.error.TCPTimedOutError",
      "twisted.web.client.ResponseFailed",
    # OSError is raised by the HttpCompression middleware when trying to
    # decompress an empty response
      OSError,
      "scrapy.core.downloader.handlers.http11.TunnelError",
    ],
    #Logging Settings
    'LOG_FILE': f'/var/log/scrapy.log',
    'LOGGING_ENABLED': True,
    'LOGGING_LEVEL': 'Debug',
    'LOG_STDOUT': True,
    'LOG_FORMAT': "%(levelname)s: %(message)s",
    # Obey robots.txt rules
    'ROBOTSTXT_OBEY': False,
    # Set settings whose default value is deprecated to a future-proof value
    'REQUEST_FINGERPRINTER_IMPLEMENTATION': "2.7",
    # TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
    'FEED_EXPORT_ENCODING': "utf-8",
    'ITEM_PIPELINES': {
      "spiders.pipelines.MysqlPipeline": 100
    },
    'COOKIES_ENABLED': False,
    'DOWNLOAD_DELAY': 1
  }
  configure_logging(settings)
  #To add the city names from the city data collected from Wikipedia
  list_cities = []
  configure_logging(settings)
  runner = CrawlerRunner(settings)
  @defer.inlineCallbacks
  def crawl():    
    yield runner.crawl(WikiCitySpider)
    for item in wikicity_output:
      # This filters the city names and append them to the list_cities array. 
      # By default the list contains two entries with the name "Hamilton". 
      # Zillow and RealEstate only has data for the Hamilton city, not the township.
      if item['cityname'] == 'Hamilton' and item['cityType'] == 'Township':
        pass
      else:
        list_cities.append(item['cityname'])
    yield runner.crawl(MortgageRatesSpider)
    yield runner.crawl(ZillowcaSpider, cities=list_cities)
    yield runner.crawl(AirbnbSpider, cities=list_cities)
    yield runner.crawl(RealEstateSpider, cities=list_cities)
    reactor.stop()
    city_avg_price_calculator()
  crawl()
  reactor.run()
  
if __name__ == '__main__':
  real_estate_spider()