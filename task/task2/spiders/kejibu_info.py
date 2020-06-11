# -*- coding: utf-8 -*-
import scrapy
import time
import re
from task2.items import ToolsItem


class KeJiBuSpider(scrapy.Spider):
    name = 'kejibu_info'
    start_urls = ['http://www.most.gov.cn/mostinfo/xinxifenlei/zjgx/index.htm#']

    def parse(self, response):
        url = "http://www.most.gov.cn/mostinfo/xinxifenlei/zjgx/index.htm#"
        yield response.follow(url, self.parse_pre)

        for i in range(1, 55):
            url = "http://www.most.gov.cn/mostinfo/xinxifenlei/zjgx/index_" + str(i) + ".htm#"
            print(url)
            yield response.follow(url, self.parse_pre)

    def parse_pre(self, response):
        """爬取科技信息列表"""
        keji_urls = response.xpath('//a[@class="STYLE30"]/@href').getall()
        """得到20个形如“../fgzc/gfxwj/gfxwj2020/202003/t20200327_152661.htm” 后面加工，只要/fgzc/gfxwj/gfxwj2020/202003/t20200327_152661.htm，然后拼接http://www.most.gov.cn/mostinfo/xinxifenlei，得到详情页的URL。"""
        print(keji_urls)
        for kj_url in keji_urls:
            kj_url = "http://www.most.gov.cn/mostinfo/xinxifenlei" + kj_url[2:]
            yield response.follow(kj_url, self.parse_detail)

    def parse_detail(self, response):
        """爬取详情页"""
        item = ToolsItem()
        item['name'] = response.xpath('//td[@colspan]/../../tr[1]/td[2]/text()').get()
        item['suoyin'] = response.xpath('//td[@colspan]/../../tr[2]/td[2]/text()').get()
        item['wenhao'] = response.xpath('//td[@colspan]/../../tr[4]/td[2]/text()').get()
        item['start_time'] = response.xpath('//td[@colspan]/../../tr[3]/td[4]/text()').get()
        item['url'] = response.url
        yield item