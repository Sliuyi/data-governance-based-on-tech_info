# -*- coding: utf-8 -*-
import scrapy
import time
import re
from task2.items import ToolsItem

class KeXueYuan(scrapy.Spider):
    name = 'kexueyuan'

    def start_requests(self):
        kexueyuan_url = "http://casad.cas.cn/ysxx2017/ysmdyjj/qtysmd_124280/"

        yield scrapy.Request(kexueyuan_url, self.parse_kexueyuan)

    def parse_kexueyuan(self, response):
        """爬取科学院院士信息"""
        kexueyuans = response.xpath('//span/a[@target="_blank"]/@href').getall()
        for kfellow in kexueyuans:
            yield response.follow(kfellow, self.parse_kexueyuan_detail)

    def parse_kexueyuan_detail(self, response):
        """爬取科学院士简历"""
        item = ToolsItem()
        item['name'] = "科学院院士"
        item['title'] = response.xpath('//h1/text()').get()
        item['content'] = re.sub(r'\s+','', "".join(response.xpath('//p//text()').getall()))
        item['url'] = response.url

        yield item