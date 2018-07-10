# -*- coding: utf-8 -*-
import scrapy

from ..items import MovieItem


class FilmSpider(scrapy.Spider):
    name = 'film'
    allowed_domains = ['www.dytt8.net','www.ygdy8.net']
    start_urls = ['http://www.ygdy8.net/html/gndy/oumei/index.html']

    def parse(self, response):
        tables = response.xpath('//table[@class="tbspan"]')
        for table in tables:
            try:
                item = MovieItem()
                film_type = table.xpath('.//b/a/text()').extract()[0]
                film_name = table.xpath('.//b/a/text()').extract()[1]
                film_info = table.xpath('.//tr[last()]/td/text()').extract_first()
                item['film_type'] = film_type
                item['film_name'] = film_name
                item['film_info'] = film_info
                yield item
            except Exception as e:
                pass
        return