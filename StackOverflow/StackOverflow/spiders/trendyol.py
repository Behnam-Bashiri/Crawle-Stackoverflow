import scrapy

import json


class TrendyolSpider(scrapy.Spider):
    name = 'trendyol'
    start_urls = ['https://www.trendyol.com/adidas-x-b33']

    def parse(self, response):
        name_product = response.css('span.prdct-desc-cntnr-name::text').extract()
        price_product = response.xpath("//div[@class='prc-box-dscntd']/text()").extract()

        total = []

        for product in range(len(name_product)):
            temp_json = {"name": name_product[product], "price": price_product[product]}
            total.append(temp_json)

        with open('trendyol.json', 'a') as f:
            f.write(json.dumps(total))
            f.close()
            