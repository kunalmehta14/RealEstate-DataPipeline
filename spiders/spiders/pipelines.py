import mysql
import os
from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# # useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# class SpidersPipeline:
#     def process_item(self, item, spider):
#         return item

