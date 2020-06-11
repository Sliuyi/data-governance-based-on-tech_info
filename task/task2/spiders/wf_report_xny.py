# -*- coding: utf-8 -*-
import scrapy
from task2.items import ToolsItem

class XnyReportSpider(scrapy.Spider):
    name = 'wf_report_xny'

    def start_requests(self):
        for i in range(1, 23):
            url = "http://s.wanfangdata.com.cn/NSTR.aspx?q=%E6%96%B0%E8%83%BD%E6%BA%90&f=top&p=" + str(i)
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