import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.spider import Spider
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from datetime import date, time
import json
import datetime
import time
from ssensebot.items import SsensebotItem
import image

#selenium dependencies
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.support import expected_conditions as EC
from scrapy.loader.processors import Join, MapCompose
import logging
from selenium.webdriver.remote.remote_connection import LOGGER

class ssensebot(Spider):
	name = "ssensebot"
	allowed_domains = ["ssense.com"]
	start_urls = ["https://www.ssense.com/en-us/men/designers/acne-studios"]

	def __init__(self):
		LOGGER.setLevel(logging.WARNING)
		opts = ChromeOptions()
		opts.add_experimental_option("detach", True)
		self.driver = webdriver.Chrome(chrome_options=opts, service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
		self.driver.set_window_size(1500, 768)
		
	def parse(self, response):
		self.driver.get(response.url)
		self.wait = WebDriverWait(self.driver, 500)
		items = []
		productlist = []
		productlist = self.driver.find_elements_by_xpath('//div[@class="browsing-product-list"]/figure/a')
		i = 1
		page = 1
		totalpages = 2 #temporary amount to be overwritten
		image_urls = []
		while (page < totalpages):
			while (i < len(productlist)):
				item = SsensebotItem()
				elem = self.driver.find_element_by_xpath("//div[@class='browsing-product-list']/figure["+str(i)+"]/a")
				elem.click()
				self.driver.implicitly_wait(10)	
				#scrape it  
				item['brand'] = self.driver.find_element_by_xpath('//h1[@class="product-brand"]/a').text
				item['name'] = self.driver.find_element_by_xpath('//h2[@class="product-name"]').text
				item['price'] = self.driver.find_element_by_xpath('//h3/span[@class="price"]').text
				item['description'] = self.driver.find_element_by_xpath('//p[@class="vspace1 product-description-text"]/span[1]').text
				item['material'] = self.driver.find_element_by_xpath('//p[@class="vspace1 product-description-text"]/span[2]').text
				item['origin'] = self.driver.find_element_by_xpath('//p[@class="vspace1 product-description-text"]/span[3]').text
				imglist = self.driver.find_elements_by_xpath('//div[@class="image-wrapper"]/div/picture')
				item['image_urls'] = []
				for img in imglist:
					image_urls.append(img.find_element_by_xpath('.//img').get_attribute('data-srcset'))
					item['image_urls'].append(img.find_element_by_xpath('.//img').get_attribute('data-srcset'))
				#and get out  
				self.driver.execute_script("window.history.go(-1)")
				i = i + 1
				items.append(item)
			
			#page control
			i = 1
			self.driver.implicitly_wait(3)
			self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			elem = self.driver.find_element_by_xpath('//ul[@class="nav"]/li[last()]/a')
			totalpages = int(self.driver.find_element_by_xpath('//ul[@class="nav"]/li[last()-1]/a').text)
			elem.click()
			page = page + 1
			self.driver.implicitly_wait(3)
			productlist = self.driver.find_elements_by_xpath('//div[@class="browsing-product-list"]/figure/a')
		return items
		return image_urls