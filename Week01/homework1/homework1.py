import requests,os
from bs4 import BeautifulSoup as bs
import pandas as pd

User_Agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
cookie='__mta=53787415.1601100562330.1601100562330.1601103099522.2; uuid_n_v=v1; uuid=BFC17FE0FFBE11EA9D59B5BD9A0E62CA888C95276E284025BBB6BB06AF9E28AE; _csrf=27b179588d0d986f1d9a53edf9b99e1829f42609345a44ea0d9ce8f912473e0a; __guid=17099173.1513956798400999700.1601100532172.8398; _lxsdk_cuid=174c9074b98c8-0dec7f70ff01ac-376b4502-1fa400-174c9074b98c8; _lxsdk=BFC17FE0FFBE11EA9D59B5BD9A0E62CA888C95276E284025BBB6BB06AF9E28AE; mojo-uuid=5716ecadada2c896b3d8f383ebe1d9f7; __mta=53787415.1601100562330.1601100562330.1601100562330.1; monitor_count=2; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1601103099; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1601103099; _lxsdk_s=174c94aa59b-9db-b5d-d3e%7C%7C1'
header={'User-Agent':User_Agent,'cookie':cookie}

url='https://maoyan.com/films?showType=3'

res=requests.get(url,headers=header)

soup=bs(res.text,'html.parser')
#电影隐藏信息
movie_hover_info=soup.find_all('div',class_='movie-hover-info',limit=10)

movies=[['电影名称','电影类型','上映时间']]

for each in movie_hover_info:
    #电影名称
    film_name=each.find('span',class_='name').text.strip()
    movie_hover_title=each.find_all('div',class_='movie-hover-title')
    #电影类型
    film_type=movie_hover_title[1].text.strip().split()[1]
    #上映时间
    plan_date=movie_hover_title[3].text.strip().split()[1]

    movies.append([film_name,film_type,plan_date])

movie=pd.DataFrame(data=movies)
file=r'E:\桌面\极客大学Python进阶训练营\Python004-master\Week01\movie_top10.csv'
movie.to_csv(file,encoding='gbk',index=0,header=0)
os.startfile(file)