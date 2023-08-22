import requests
from bs4 import BeautifulSoup
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import re

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('lunch.html')

r = re.compile('\d+(?=\.).')

lunch = []
date = datetime.today().strftime("%m/%d")

try:
    url = 'https://sunrint.sen.hs.kr/index.do'
    
    response = requests.get(url=url)
    
    if response.status_code == 200:
        html = response.text
        
    soup = BeautifulSoup(html, 'html.parser')
    lunchdata = soup.select_one('#index_board_mlsv_03_195699 > div > div > div > div > ul:nth-child(1) > li > dl > dd > p.menu').text.strip().split('\r\n')
    date = soup.select_one('#index_board_mlsv_03_195699 > div > div > div > div > ul:nth-child(1) > li > dl > dd > p.date').text.strip()[5:-2]

    for menu in lunchdata:
        menu = re.sub(r, '', menu).strip()
        if menu[0] == '&':
            lunch[-1] += menu
        else:
            lunch.append(menu)

except:
    pass

finally:
    with open('./lunch.html', 'w', encoding='utf-8') as fh:
        fh.write(template.render(date=date, lunch=lunch))
