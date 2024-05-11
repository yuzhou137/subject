#准备工作
import requests
import logging
import  re
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

BASE_URL = 'https://ssr1.scrape.center'
totalpage = 10


def scrape_page(url):
    logging.info('scraping %s...',url)
    try:
        response = requests.get(url)
        if response.status_code==200:
            return response.text
        logging.error('get invalid status code %s while scraping %s',
                      response.status_code,url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s',url,
                      exc_info=True)

def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)

def parse_index(html):
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">')
    items = re.findall(pattern,html)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL, item)
        logging.info('get detail url %s', detail_url)
        yield detail_url

def main():
    for page in range(1,totalpage+1):
        index_html = scrape_index(page)
        detail_urls = parse_index(index_html)
        logging.info('detail urls %s',list(detail_urls))

main()
# 爬取url
# 开始解析
def scrape_detail(url):     #逻辑
    return scrape_page(url)

def parse_detail (html):
    cover_pattern = re.compile('class="item.*?<img.*?src="(.*?)".*?class="cover">',re.S)
    name_pattern = re.compile('<h2.*?>(.*?)</h2>')
    categories_pattern = re.compile('<button.*?category.*?<span>(.*?)</span>.*?</button>',re.S)
    published_pattern = re.compile('(\d{4}-\d{2}-\d{2})\s?上映')
    cover = re.search(cover_pattern,html).group(1).strip() if re.search(cover_pattern,html) else None
    name = re.search(name_pattern, html).group(1).strip() if re.search(name_pattern, html) else None
    return {
        'cover': cover,
        'name': name
    }
def main():
    for page in range(1,totalpage+1):
        index_html = scrape_index(page)
        detail_urls = parse_index(index_html)
        for detail_url in detail_urls:
            detail_html = scrape_detail(detail_url)
            data = parse_detail(detail_html)
            logging.info('get detail data %s',data)

main()
import json
from os import makedirs
from os.path import exists
result = 'results'
exists(result) or makedirs(result)

def save_data(data):
    name = data.get("name")
    data_path = f'{result}/{name}.json'
    json.dump(data, open(data_path,'w',encoding='utf-8'),ensure_ascii=False, indent=2)