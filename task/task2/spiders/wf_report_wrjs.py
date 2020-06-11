# -*- coding: utf-8 -*-
import scrapy
from task2.items import ToolsItem

class WrjsReportSpider(scrapy.Spider):
    name = 'wf_report_wrjs'

    def start_requests(self):
        url = "http://s.wanfangdata.com.cn/NSTR.aspx?q=%E6%97%A0%E4%BA%BA%E9%A9%BE%E9%A9%B6&f=top"
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        """爬取科技报告号列表"""
        pt_urls = response.xpath('//div[@class = "record-title"]/a/@href').getall()
        for pt_url in pt_urls:
            number = pt_url[37:]
            url = "http://www.wanfangdata.com.cn/details/detail.do?_type=tech&id=" + number
            print(url)
            yield response.follow(url, self.parse_detail)

    def parse_detail(self, response):
        """爬取详情页"""
        item = ToolsItem()
        item['name'] = response.xpath('//head/title/text()').get()
        item['key_words'] = response.xpath('//div[text()="关键词："]/../div[2]/a[@title]/text()').getall()
        item['author'] = response.xpath('//div[text()="作者："]/../div[2]/a/text()').getall()
        item['author_organ'] = response.xpath('//div[text()="作者单位："]/../div[2]/a/text()').getall()
        item['report_type'] = response.xpath('//div[text()="报告类型："]/../div[2]/text()').get()
        item['plan_name'] = response.xpath('//div[text()="计划名称："]/../div[2]/text()').get()
        item['plan_year'] = response.xpath('//div[text()="立项批准年："]/../div[2]/text()').get()
        item['id_number'] = response.xpath('//div[text()="馆藏号："]/../div[2]/text()').get()
        item['url'] = response.url
        yield item