# -*- coding: utf-8 -*-
import scrapy
import re
from task2.items import ToolsItem

class WrjsPeriodicalSpider(scrapy.Spider):
    name = 'wf_periodical_wrjs'

    def start_requests(self):
        for i in range(1, 510):
            url = "http://s.wanfangdata.com.cn/Paper.aspx?q=%E6%97%A0%E4%BA%BA%E9%A9%BE%E9%A9%B6+DBID%3aWF_QK&f=top&p=" + str(i)
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        """爬取期刊号列表"""
        pt_urls = response.xpath('//div[@class = "record-title"]/a[@class="title"]/@href').getall()
        for pt_url in pt_urls:
            number = pt_url[43:]
            url = "http://www.wanfangdata.com.cn/details/detail.do?_type=perio&id=" + number
            print(url)
            yield response.follow(url, self.parse_detail)

    def parse_detail(self, response):
        """爬取详情页"""
        item = ToolsItem()
        item['name'] = response.xpath('//head/title/text()').get()
        item['key_words'] = response.xpath('//div[text()="关键词："]/../div[2]/a[@title]/text()').getall()
        item['author'] = response.xpath('//div[text()="作者："]/../div[2]/a/text()').getall()
        item['author_organ'] = response.xpath('//div[text()="作者单位："]/../div[2]/*/text()').getall()
        item['periodical_name'] = response.xpath('//div[text()="刊名："]/../div[2]/a[@onclick]/text()').get()
        item['periodical_section'] = response.xpath('//div[text()="所属期刊栏目："]/../div[2]/a[@onclick]/text()').get()
        item['periodical_year_issue'] = response.xpath('//div[text()="年，卷(期)："]/../div[2]/a/text()').get()
        item['fund_project'] = response.xpath('//div[text()="基金项目："]/../div[2]/a[@onclick]/text()').get()
        item['page_number'] = response.xpath('//div[text()="页码："]/../div[2]/text()').get()
        item['url'] = response.url
        yield item