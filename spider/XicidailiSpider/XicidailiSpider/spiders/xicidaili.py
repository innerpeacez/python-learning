# -*- coding: utf-8 -*-
import random
from time import sleep

import scrapy


class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/nn']

    def parse(self, response):
        selector = response.xpath('//tr')
        for record in selector:
            ip = record.xpath('./td[2]/text()').get()
            port = record.xpath('./td[3]/text()').get()

            with open('xicidaili.txt', 'a') as f:
                '{"ipaddr": "182.35.83.170:9999"},'
                f.write('{"ipaddr": "%s:%s"},\n' % (ip, port))

        next_page = response.xpath('//a[@class="next_page"]/@href').get()

        if next_page:
            next_url = response.urljoin(next_page)
            try:
                yield scrapy.Request(next_url, callback=self.parse)
                sleep(random.randint(1, 3))
            except:
                print("next----------------->")
