# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ToolsItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	name = scrapy.Field()           # 事物职称，性质
	document_number = scrapy.Field()
	type = scrapy.Field()
	issuing_department = scrapy.Field()
	effective_level = scrapy.Field()
	timeliness = scrapy.Field()
	release_date = scrapy.Field()
	start_date = scrapy.Field()
	content_type = scrapy.Field()
	url = scrapy.Field()            # 详情链接
	#content = scrapy.Field()        #  简历
	#start_time = scrapy.Field()     # 发布时间
	#suoyin = scrapy.Field()         # 索引号（科技部信息）
	#wenhao = scrapy.Field()         # 文号（科技部信息)
	#st_num = scrapy.Field()         # 标准号（标准）
	#e_name = scrapy.Field()         # 英文名 （标准）
	#c_name = scrapy.Field()         # 中文名 （标准）
	#beg_time = scrapy.Field()       # 实施时间 （标准）
	#apply_num = scrapy.Field()       # 申请号（专利）
	#apply_date = scrapy.Field()      # 申请日期（专利）
	#public_num = scrapy.Field()      # 公开号（专利）
	#public_date = scrapy.Field()     # 公开日期（专利）
	#apply_man = scrapy.Field()       # 申请人
	#invent_man = scrapy.Field()      # 发明人
	#abstract = scrapy.Field()        # 摘要
	#used_date = scrapy.Field()        #实施日期
	#country = scrapy.Field()          # 国家
	#organization = scrapy.Field()     #发布机构
	#standard_num = scrapy.Field()     #专利号
	#location = scrapy.Field()			#地区
	#project_num = scrapy.Field()		#项目号
	#public_year = scrapy.Field()       #公布年份
	#organs = scrapy.Field()            #完成单位
	#plan_name = scrapy.Field()         #计划名称
	#key_words = scrapy.Field()         # 关键词
	#author = scrapy.Field()            #作者
