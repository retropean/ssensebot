import scrapy

class SsensebotItem(scrapy.Item):
    name = Field()
	price = Field()
	brand = Field()
	imgname = Field()
	material = Field()
	description = Field()
    pass