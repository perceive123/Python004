# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class MaoyanPipeline:
    def process_item(self, item, spider):
        film_name = item['film_name']
        film_type = item['film_type']
        plan_date = item['plan_date']
        movies = [(film_name, film_type, plan_date)]
        movie = pd.DataFrame(data=movies)
        file = r'E:\桌面\极客大学Python进阶训练营\Python004-master\Week01\movie_top10_xpath2.csv'
        movie.to_csv(file, encoding='utf_8_sig', index=0, header=0, mode='a')
