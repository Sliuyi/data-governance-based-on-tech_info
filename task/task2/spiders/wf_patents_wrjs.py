# -*- coding: utf-8 -*-
import scrapy
import time
import re
from task2.items import ToolsItem


class WrjsSpider(scrapy.Spider):
    name = 'wf_patents_wrjs'

    def start_requests(self):
        for i in range(1, 458):
            url = "http://s.g.wanfangdata.com.cn/Patent.aspx?q=%E6%97%A0%E4%BA%BA%E9%A9%BE%E9%A9%B6&f=c.Patent&p=" + str(i)
            print(url)
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        """爬取专利列表"""
        pt_urls = response.xpath('//li[@class="title_li"]/a[3]/@href').getall()
        print(pt_urls)
        for pt_url in pt_urls:
            yield response.follow(pt_url, self.parse_detail)

    def parse_detail(self, response):
        """爬取详情页"""
        item = ToolsItem()
        item['name'] = response.xpath('//div[@id="detail_leftcontent"]/div/h1/text()').get()
        item['apply_num'] = response.xpath('//th/../../tr[2]/td/text()').get()
        item['apply_date'] = response.xpath('//th/../../tr[3]/td/text()').get()
        item['public_num'] = response.xpath('//th/../../tr[5]/td/text()').get()
        item['public_date'] = response.xpath('//th/../../tr[4]/td/text()').get()
        item['apply_man'] = response.xpath('//th/../../tr[8]/td/text()').get()
        item['invent_man'] = response.xpath('//th/../../tr[9]/td/text()').get()
        item['abstract'] = response.xpath('//*[@id="detail_leftcontent"]/div/div[2]/text()').get()
        item['url'] = response.url
        yield item