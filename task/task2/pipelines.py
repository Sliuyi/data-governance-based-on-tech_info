# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os


class ToolsPipeline(object):
	def open_spider(self, spider):
		folder = 'task2_json/'
		if not os.path.exists(folder):
			os.mkdir(folder)

		self.file = open(folder + spider.name + '.json', 'w', encoding='utf-8')

	def close_spider(self, spider):
		self.file.close()

	def process_item(self, item, spider):
		dict = {
			'name': item['name'],
			'document_number': item['document_number'],
			'type': item['type'],
			'issuing_department': item['issuing_department'],
			'effective_level': item['effective_level'],
			'timeliness': item['timeliness'],
			'release_date': item['release_date'],
			'start_date': item['start_date'],
			'content_type': item['content_type'],
			'url': item['url'],
			#'content': item['content'],
			#'start_time': item['start_time'],
			#'suoyin': item['suoyin'],
			#'wenhao': item['wenhao'],
			#'st_num': item['st_num'],
			#'e_name': item['e_name'],
			#'c_name': item['c_name'],
			#'beg_time': item['beg_time'],
			#'apply_num': item['apply_num'],
			#'apply_date': item['apply_date'],
			#'public_num': item['public_num'],
			#'public_date': item['public_date'],
			#'apply_man': item['apply_man'],
			#'invent_man': item['invent_man'],
			#'abstract': item['abstract'],
			#'used_date': item['used_date'],
			#'country': item['country'],
			#'organization': item['organization'],
			#'standard_num': item['standard_num'],
			#'location': item['location'],
			#'project_num': item['project_num'],
			#'public_year': item['public_year'],
			#'organs': item['organs'],
			#'plan_name': item['plan_name'],
			#'key_words': item['key_words'],
			#'author' : item['author'],
		}

		self.file.write(json.dumps(dict, ensure_ascii=False, indent=4))
		self.file.write('\n')
		return item
