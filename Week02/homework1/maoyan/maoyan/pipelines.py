# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from scrapy.utils.project import get_project_settings

class MaoyanPipeline:

    def process_item(self, item, spider):
        film_name = item['film_name']
        film_type = item['film_type']
        plan_date = item['plan_date']
        movies = [(film_name, film_type, plan_date)]
        # 配置文件中读取MySQL配置信息
        settings = get_project_settings()
        dbInfo = settings.get('MYSQL_CONFIG')
        conn = pymysql.connect(
            host=dbInfo['host'],
            port=dbInfo['port'],
            user=dbInfo['user'],
            password=dbInfo['password'],
            db=dbInfo['db']
        )
        cur = conn.cursor()
        sqls = ['create table if not exists maoyanmovies(film_name varchar(255),film_type varchar(255),plan_date varchar(255))']
        try:
            for s in sqls:
                cur.execute(s)
            cur.executemany('insert into maoyanmovies values(%s,%s,%s)', movies)
            cur.close()
            conn.commit()
        except:
            conn.rollback()
            raise Exception('数据插入失败')
        finally:
            conn.close()
