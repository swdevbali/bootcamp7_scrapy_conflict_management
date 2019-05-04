# -*- coding: utf-8 -*-
import scrapy


class MostpopularDetikcomWrSpider(scrapy.Spider):
    name = 'mostpopular_detikcom_wr'
    allowed_domains = ['https://www.detik.com/']
    start_urls = ['http://https://www.detik.com//']

    def parse(self, response):


        pass
