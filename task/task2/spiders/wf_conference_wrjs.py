# -*- coding: utf-8 -*-
import scrapy
import re
from task2.items import ToolsItem

class WrjsConferenceSpider(scrapy.Spider):
    name = 'wf_conference_wrjs'

    def start_requests(self):
        for i in range(1, 38):
            url = "http://s.wanfangdata.com.cn/Paper.aspx?q=%E6%97%A0%E4%BA%BA%E9%A9%BE%E9%A9%B6+DBID%3aWF_HY&f=top&p=" + str(i)
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        """爬取会议论文号列表"""
        pt_urls = response.xpath('//div[@class = "record-title"]/a/@href').getall()
        for pt_url in pt_urls:
            number = pt_url[43:]
            url = "http://www.wanfangdata.com.cn/details/detail.do?_type=conference&id=" + number
            print(url)
            yield response.follow(url, self.parse_detail)

    def parse_detail(self, response):
        """爬取详情页"""
        item = ToolsItem()
        item['name'] = response.xpath('//head/title/text()').get()
        item['key_words'] = response.xpath('//div[text()="关键词："]/../div[2]/a[@title]/text()').getall()
        item['author'] = response.xpath('//div[text()="作者："]/../div[2]/a/text()').getall()
        item['conference_name'] = response.xpath('//div[text()="会议名称："]/../div[2]/a[@onclick]/text()').get()
        item['conference_time'] = re.sub(r'\D', "", response.xpath('//div[text()="会议时间："]/../div[2]/text()').get())
        item['conference_local'] = response.xpath('//div[text()="会议地点："]/../div[2]/text()').get()
        item['conference_organ'] = response.xpath('//div[text()="主办单位："]/../div[2]/a/text()').get()
        item['url'] = response.url
        yield item