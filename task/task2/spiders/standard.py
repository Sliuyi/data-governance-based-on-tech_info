# -*- coding: utf-8 -*-
import scrapy
import time
import re
from task2.items import ToolsItem


class StandardSpider(scrapy.Spider):
    name = 'standard'
    start_urls = ['http://www.gb688.cn/bzgk/gb/std_list_type?r=0.5025632033563541&page=1&pageSize=50&p.p1=1&p.p5=PUBLISHED&p.p90=circulation_date&p.p91=desc']

    def parse(self, response):
        for i in range(1, 44):
            url = "http://www.gb688.cn/bzgk/gb/std_list_type?r=0.09076049106633288&page=" + str(i) + "&pageSize=50&p.p1=1&p.p5=PUBLISHED&p.p90=circulation_date&p.p91=desc"
            print(url)
            yield response.follow(url, self.parse_pre)

    def parse_pre(self, response):
        """爬取标准列表"""
        st_urls = response.xpath('//td[@class="mytxt"]/a/@onclick').getall()
        """得到50个形如“showInfo('C711325EC14978CA59B9D5087A97DE17');” 后面加工，只要C7…，然后拼接http://www.gb688.cn/bzgk/gb/newGbInfo?hcno=，得到详情页的URL。"""
        print(st_urls)
        for st_url in st_urls:
            st_url = "http://www.gb688.cn/bzgk/gb/newGbInfo?hcno=" + st_url[10:42]
            yield response.follow(st_url, self.parse_detail)

    def parse_detail(self, response):
        """爬取详情页"""
        item = ToolsItem()
        item['st_num'] = response.xpath('//td[@width="560"]/h1/text()').get()
        item['e_name'] = response.xpath('//b/text()/../../../../tr[2]/td/text()').get()
        item['c_name'] = response.xpath('//b/text()').get()
        item['beg_time'] = re.sub(r'\D', "", response.xpath('/html/body/div[3]/div/div/div/div/div[3]/div[4]/text()').get())
        item['url'] = response.url
        yield item