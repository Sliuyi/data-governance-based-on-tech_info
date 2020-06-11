# -*- coding: utf-8 -*-
import scrapy
import time
import re
from task2.items import ToolsItem

class GongChengYuan(scrapy.Spider):
    name = 'gongchengyuan'

    def start_requests(self):
        gongchengyuan_url = "http://www.cae.cn/cae/html/main/col48/column_48_1.html"

        yield scrapy.Request(gongchengyuan_url, self.parse_gongchengyuan)

    def parse_gongchengyuan(self, response):
        """爬取工程院院士信息"""
        gongchengyuans = response.xpath('//li[@class="name_list"]/a/@href').getall()

        for gfellow in gongchengyuans:
            yield response.follow(gfellow, self.parse_gongchengyuan_detail)
            
    def parse_gongchengyuan_detail(self, response):
        """爬取工程院士简历"""
        item = ToolsItem()
        item['name'] = "工程院院士"
        item['title'] = response.xpath('//div[@class="right_md_name"]/text()').get()
        item['content'] = re.sub(r'\xa0|\u2002', "", "".join(response.xpath('//div[@class="intro"]/p/text()').getall()))
        item['url'] = response.url

        yield item