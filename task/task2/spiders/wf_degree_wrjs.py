# -*- coding: utf-8 -*-
import scrapy
from task2.items import ToolsItem

class WrjsDegreeSpider(scrapy.Spider):
    name = 'wf_degree_wrjs'

    def start_requests(self):
        for i in range(1, 116):
            url = "http://s.g.wanfangdata.com.cn/Paper.aspx?q=%E6%97%A0%E4%BA%BA%E9%A9%BE%E9%A9%B6+DBID%3aWF_XW&p=" + str(i)
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        """爬取学位论文号列表"""
        pt_urls = response.xpath('//a[@class="exportLink"]/@id').getall()
        for pt_url in pt_urls:
            number = pt_url[7:]
            url = "http://www.wanfangdata.com.cn/details/detail.do?_type=degree&id=" + number
            yield response.follow(url, self.parse_detail)

    def parse_detail(self, response):
        """爬取详情页"""
        item = ToolsItem()
        item['name'] = response.xpath('//head/title/text()').get()
        item['doi'] = response.xpath('//div[text()="doi："]/../div[2]/a/text()').get()
        item['key_words'] = response.xpath('//div[text()="关键词："]/../div[2]/a[@title]/text()').getall()
        item['author'] = response.xpath('//div[text()="作者："]/../div[2]/a/text()').get()
        item['organ'] = response.xpath('//div[text()="学位授予单位："]/../div[2]/a/text()').get()
        item['degree'] = response.xpath('//div[text()="授予学位："]/../div[2]/text()').get()
        item['subject'] = response.xpath('//div[text()="学科专业："]/../div[2]/a/text()').get()
        item['instructor'] = response.xpath('//div[text()="导师姓名："]/../div[2]/a/text()').get()
        item['time'] = response.xpath('//div[text()="学位年度："]/../div[2]/text()').get()
        item['url'] = response.url
        yield item