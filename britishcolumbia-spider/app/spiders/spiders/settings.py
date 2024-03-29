# import os
# from dotenv import find_dotenv, load_dotenv
# dotenv_path = find_dotenv()
# load_dotenv(dotenv_path)
# # Scrapy settings for spiders project
# #
# # For simplicity, this file contains only settings considered important or
# # commonly used. You can find more settings consulting the documentation:
# #
# #     https://docs.scrapy.org/en/latest/topics/settings.html
# #     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# #     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# BOT_NAME = "spiders"
# SPIDER_MODULES = ["spiders.spiders"]
# NEWSPIDER_MODULE = "spiders.spiders"
# #Scrapeops Settings Configuration
# SCRAPEOPS_API_KEY = os.getenv("SCRAPEOPS_API_KEY")
# SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
# DOWNLOADER_MIDDLEWARES = {
#     'spiders.middlewares.ScrapeOpsFakeUserAgentMiddleware': 400,
#     'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 401,
#     'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 402,
#     'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
#     'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
# }
# HEADERS = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "keep-alive",
#     "Upgrade-Insecure-Requests": "1",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "none",
#     "Sec-Fetch-User": "?1",
#     "Cache-Control": "max-age=0",
# }
# #Logging Settings
# LOG_FILE = './scrapy.logs'
# LOGGING_ENABLED = True
# LOGGING_LEVEL = 'Debug'
# LOG_STDOUT = False
# LOG_FORMAT = "%(levelname)s: %(message)s"
# # Obey robots.txt rules
# ROBOTSTXT_OBEY = False
# # Set settings whose default value is deprecated to a future-proof value
# REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
# # TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
# FEED_EXPORT_ENCODING = "utf-8"
# RETRY_ENABLED = True
# RETRY_TIMES = 5
# RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429, 403]
# RETRY_PRIORITY_ADJUST = -1
# RETRY_EXCEPTIONS = [
#     "twisted.internet.defer.TimeoutError",
#     "twisted.internet.error.TimeoutError",
#     "twisted.internet.error.DNSLookupError",
#     "twisted.internet.error.ConnectionRefusedError",
#     "twisted.internet.error.ConnectionDone",
#     "twisted.internet.error.ConnectError",
#     "twisted.internet.error.ConnectionLost",
#     "twisted.internet.error.TCPTimedOutError",
#     "twisted.web.client.ResponseFailed",
#     # OSError is raised by the HttpCompression middleware when trying to
#     # decompress an empty response
#     OSError,
#     "scrapy.core.downloader.handlers.http11.TunnelError",
#     ]
# # Disable cookies (enabled by default)
# COOKIES_ENABLED = False
# # Configure item pipelines
# # See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# # ITEM_PIPELINES = {
# #    "spiders.pipelines.MysqlPipeline": 100,
# # }
# # Enable and configure HTTP caching (disabled by default)
# # See also autothrottle settings and docs
# # Configure a delay for requests for the same website (default: 0)
# # See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# DOWNLOAD_DELAY = 3
# # Crawl responsibly by identifying yourself (and your website) on the user-agent
# #USER_AGENT = "spiders (+http://www.yourdomain.com)"
# # Configure maximum concurrent requests performed by Scrapy (default: 16)
# #CONCURRENT_REQUESTS = 32
# # The download delay setting will honor only one of:
# #CONCURRENT_REQUESTS_PER_DOMAIN = 16
# #CONCURRENT_REQUESTS_PER_IP = 16
# # Disable Telnet Console (enabled by default)
# #TELNETCONSOLE_ENABLED = False
# # Override the default request headers:
# #DEFAULT_REQUEST_HEADERS = {
# #    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
# #    "Accept-Language": "en",
# #}
# # Enable or disable spider middlewares
# # See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# #SPIDER_MIDDLEWARES = {
# #    "spiders.middlewares.SpidersSpiderMiddleware": 543,
# #}
# # Enable or disable downloader middlewares
# # See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# #DOWNLOADER_MIDDLEWARES = {
# #    "spiders.middlewares.SpidersDownloaderMiddleware": 543,
# #}
# # Enable or disable extensions
# # See https://docs.scrapy.org/en/latest/topics/extensions.html
# #EXTENSIONS = {
# #    "scrapy.extensions.telnet.TelnetConsole": None,
# #}
# # Enable and configure the AutoThrottle extension (disabled by default)
# # See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# #AUTOTHROTTLE_ENABLED = True
# # The initial download delay
# #AUTOTHROTTLE_START_DELAY = 5
# # The maximum download delay to be set in case of high latencies
# #AUTOTHROTTLE_MAX_DELAY = 60
# # The average number of requests Scrapy should be sending in parallel to
# # each remote server
# #AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# # Enable showing throttling stats for every response received:
# #AUTOTHROTTLE_DEBUG = False
# # See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# #HTTPCACHE_ENABLED = True
# #HTTPCACHE_EXPIRATION_SECS = 0
# #HTTPCACHE_DIR = "httpcache"
# #HTTPCACHE_IGNORE_HTTP_CODES = []
# #HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"
