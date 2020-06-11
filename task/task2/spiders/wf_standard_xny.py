# -*- coding: utf-8 -*-
import scrapy
import time
import re
from task2.items import ToolsItem


class XnyStandardSpider(scrapy.Spider):
    name = 'wf_standard_xny'

    def start_requests(self):
        for i in range(1, 37):
            url = "http://s.g.wanfangdata.com.cn/Standard.aspx?q=%E6%96%B0%E8%83%BD%E6%BA%90&f=top&p=" + str(i)
            print(url)
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        """爬取标准列表"""
        pt_urls = response.xpath('//li[@class="title_li"]/a[3]/@href').getall()
        print(pt_urls)
        for pt_url in pt_urls:
            yield response.follow(pt_url, self.parse_detail)

    def parse_detail(self, response):
        """爬取详情页"""
        item = ToolsItem()
        item['name'] = response.xpath('//div[@id="detail_leftcontent"]/div/h1/text()').get()
        item['organization'] = response.xpath('//t[text()="发布单位"]/../../td/text()').get()
        item['public_date'] = response.xpath('//t[text()="发布日期"]/../../td/text()').get()
        item['used_date'] = response.xpath('//t[text()="实施日期"]/../../td/text()').get()
        item['standard_num'] = response.xpath('//t[text()="标准编号"]/../../td/text()').get()
        item['country'] = response.xpath('//t[text()="国别"]/../../td/text()').get()
        item['url'] = response.url
        yield item