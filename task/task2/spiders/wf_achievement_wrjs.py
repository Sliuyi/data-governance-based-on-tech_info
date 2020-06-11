# -*- coding: utf-8 -*-
import scrapy
import time
import re
from task2.items import ToolsItem


class WrjsAchievementSpider(scrapy.Spider):
    name = 'wf_achievement_wrjs'

    def start_requests(self):
        for i in range(1, 21):
            url = "http://s.g.wanfangdata.com.cn/Cstad.aspx?q=%E6%97%A0%E4%BA%BA%E9%A9%BE%E9%A9%B6&f=top&p=" + str(i)
            print(url)
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        """爬取专利号列表"""
        pt_urls = response.xpath('//li[@class="greencolor"]/text()').getall()
        for pt_url in pt_urls:
            if pt_url[8].isdigit():
                number = pt_url[0:10]
            else:
                number = pt_url[0:8]
            url = "http://www.wanfangdata.com.cn/details/detail.do?_type=techResult&id=" + number
            yield response.follow(url, self.parse_detail)

    def parse_detail(self, response):
        """爬取详情页"""
        item = ToolsItem()
        item['name'] = response.xpath('//font/text()').get()
        item['project_num'] = response.xpath('//div[text()="项目年度编号："]/../div[2]/text()').get()
        item['public_year'] = response.xpath('//div[text()="公布年份："]/../div[2]/text()').get()
        orgs = response.xpath('//div[text()="完成单位："]/../div[2]/a/@onclick').getall()
        """得到列表元素为wfAnalysis('tech_result','山东时风(集团)有限责任公司','unit_name_teachResult')的列表"""
        organs = []
        while orgs:
            i = orgs.pop()
            current_org = i[26:-26]
            organs.append(current_org)
        item['organs'] = organs
        item['key_words'] = response.xpath('//div[text()="关键词："]/../div[2]/a[@title]/text()').getall()
        item['author'] = response.xpath('//div[text()="完成人："]/../div[2]/a[@id]/text()').getall()
        item['url'] = response.url
        yield item