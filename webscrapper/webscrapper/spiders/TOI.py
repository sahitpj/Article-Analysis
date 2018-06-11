# -*- coding: utf-8 -*-
import scrapy


class ToiSpider(scrapy.Spider):
    name = 'TOI'
    allowed_domains = ['https://timesofindia.indiatimes.com/archive.cms']
    start_urls = ['http://https://timesofindia.indiatimes.com/archive.cms/']

    def parse(self, response):
        for link in response.css('a.normtxt::atr(href)').extract():
        	yield {
        	'link:' : link
        	}
