BOT_NAME = 'ssensebot'
SPIDER_MODULES = ['ssensebot.spiders']
NEWSPIDER_MODULE = 'ssensebot.spiders'
DOWNLOAD_DELAY = 1
ROBOTSTXT_OBEY = False

USER_AGENT = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"

HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = [503]
REDIRECT_ENABLED=False

ITEM_PIPELINES = {'ssensebot.pipelines.SsensebotPipeline': 300, 
				  'scrapy.pipelines.images.ImagesPipeline': 1}
IMAGES_STORE = 'imagestore'