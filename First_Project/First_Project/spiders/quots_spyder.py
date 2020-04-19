import scrapy

class Quots_spyder(scrapy.Spider):
    name = 'quots'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        title = response.css('title').extract()
        yield {'titletext': title}