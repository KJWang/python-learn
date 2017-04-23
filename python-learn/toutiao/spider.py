import json
import re
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup


def request_url_list():
    data = {
        'offset': 0,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': 20,
        'cur_tab': 3
    }
    url = 'http://www.toutiao.com/search_content/?' + urlencode(data)
    resp = requests.get(url)
    if resp.status_code == 200:
        return parse_url_list(resp.text)
    else:
        print("请求列表失败")
        return None;


def parse_url_list(text):
    data = json.loads(text)
    page_list = data.get('data')
    for page in page_list:
        yield page.get('article_url')


def request_page_detail(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return parse_page_detail(resp.text)
    else:
        print("获取详情失败")
        return None


def parse_page_detail(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select_one('title').text;
    images_pattern = re.compile('var gallery = (.*?);', re.S)
    result = re.search(images_pattern, html)
    if result:
        data = json.loads(result.group(1))
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            urls = [item.get('url') for item in sub_images]
            return {
                'title': title,
                'images': urls
            }
    return None


def main():
    url_list = request_url_list()
    for url in url_list:
        detail = request_page_detail(url)
        if detail:
            print(detail)


if __name__ == '__main__':
    main()
