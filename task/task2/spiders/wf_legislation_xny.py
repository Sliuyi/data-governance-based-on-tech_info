# -*- coding: utf-8 -*-
import scrapy
import re
from task2.items import ToolsItem

class XnyLegislationSpider(scrapy.Spider):
    name = 'wf_legislation_xny'

    def start_requests(self):
        for i in range(1, 1514):
            url = "http://s.wanfangdata.com.cn/Claw.aspx?q=%E6%96%B0%E8%83%BD%E6%BA%90&f=top&p=" + str(i)
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        """爬取法规号列表"""
        pt_urls = response.xpath('//div[@class = "record-title"]/a[@class="title"]/@href').getall()
        for pt_url in pt_urls:
            number = pt_url[37:]
            url = "http://www.wanfangdata.com.cn/details/detail.do?_type=legislations&id=" + number
            print(url)
            yield response.follow(url, self.parse_detail)

    def parse_detail(self, response):
        """爬取详情页"""
        item = ToolsItem()
        item['name'] = response.xpath('//head/title/text()').get()
        item['document_number'] = response.xpath('//div[text()="发文文号："]/../div[2]/text()').get()
        item['type'] = response.xpath('//div[text()="库别名称："]/../div[2]/text()').get()
        item['issuing_department'] = response.xpath('//div[text()="颁布部门："]/../div[2]/text()').get()
        item['effective_level'] = response.xpath('//div[text()="效力级别："]/../div[2]/text()').get()
        item['timeliness'] = response.xpath('//div[text()="时效性："]/../div[2]/text()').get()
        item['release_date'] = re.sub(r'\D', "", response.xpath('//div[text()="颁布日期："]/../div[2]/text()').get())
        item['start_date'] = re.sub(r'\D', "", response.xpath('//div[text()="实施日期："]/../div[2]/text()').get())
        item['content_type'] = response.xpath('//div[text()="内容分类："]/../div[2]/text()').get()
        item['url'] = response.url
        yield item