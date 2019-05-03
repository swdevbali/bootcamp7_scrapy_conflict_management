# -*- coding: utf-8 -*-
import scrapy


class AirportCodesSpider(scrapy.Spider):
    name = 'airport_codes'
    allowed_domains = ['https://www.world-airport-codes.com/alphabetical/airport-name/a.html']
    start_urls = ['https://www.world-airport-codes.com/alphabetical/airport-name/a.html']

    def parse(self, response):
        data = []
        table = response.css('.stack2')
        row_selector = ".// tr[ @class ='light-row']|.// tr[@ class ='dark-row']"
        for row in table.xpath(row_selector):
            name = row.xpath('.th/a/text()').extract_first()
            type_ = row.xpath('.td[1]/text()[2]').extract_first().strip()
            data.append({
            'name': name,
            'type': type_,
                })
        return data