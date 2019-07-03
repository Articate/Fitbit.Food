import requests
from contextlib import closing
from bs4 import BeautifulSoup

def get_json(url):
    content = get_content(url)
    return content.json()

def get_raw(url):
    content = get_content(url)
    return content.text()

def get_content(url):
    try:
        with closing(requests.get(url, stream=True)) as response:
            if response.status_code != 200:
                return None
            return response
    except requests.RequestException as e:
        print('Error during requests to {0}: {1}'.format(url, str(e)))
        return None

def parse_html(raw_html):
    html = BeautifulSoup(raw_html, 'html.parser')
    return html