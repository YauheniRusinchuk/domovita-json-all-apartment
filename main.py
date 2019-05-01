#python 3.7

import requests
from bs4 import BeautifulSoup
import json


def get_page(count):
    url:str = f'https://domovita.by/minsk/flats/rent?page={count}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


def write_list_dict(info):
    d = json.loads(info)
    with open('data.json', 'a') as f:
        json.dump(d, f, ensure_ascii=False)


def find_script_from_page(page):
    all_div = page.findAll(class_='found_item')
    for i in all_div:
        script_info = i.find('script').get_text()
        write_list_dict(script_info)


def main():
    for i in range(1,83):
        print(i)
        html_page = get_page(i)
        find_script_from_page(html_page)

if __name__ == '__main__':
    main()
