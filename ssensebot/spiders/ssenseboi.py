import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from datetime import date, time
import json
import datetime
import time
from ssensebot.items import SsensebotItem

class ssensebot(CrawlSpider):
	name = "ssensebot"
	allowed_domains = ["ssense.com"]
	start_urls = ["https://www.ssense.com/en-us/men/designers/acne-studios"]
	handle_httpstatus_list = [301, 302]
	rules = (
		# rule to find products
        Rule(LinkExtractor(), callback='parse_item', follow=True),
	)
	
	#def __init__(self):


	def parse_item(self, response):
		print('Got a response from %s.' % response.url)
		print(response.xpath('//h1[@class="product-brand"]/a/text()').extract())
		print(response.xpath('//h2[@class="product-name"]/text()').extract())
		print(response.xpath('//span[@class="price"]/text()').extract()[1])
		print(response.xpath('//div[@class="image-wrapper"]/div/picture/img/@src').extract())