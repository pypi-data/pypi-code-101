from bs4 import BeautifulSoup as bs
import requests
import sys
import re

class ResultContainer:
    status = None
    message = None
    title = None
    query = None

    def __init__(self, status, message, title, query):
        self.status = status
        self.message = message
        self.title = title
        self.query = query

    def call_info(self):
        return {
            'status': self.status,
            'message': self.message,
            'title': self.title,
            'query': self.query
        }

def fetch_title(url):
    status = None
    message = None
    title = None
    try:
        soup = bs(requests.get(url).content, 'lxml')
        status = 'OK'
        message = 'fetching title success.'
        try:
            title = soup.title.string
        except AttributeError as err:
            title = re.sub('https?://', '', url)
    except requests.exceptions.MissingSchema as err:
        status = 'ERR'
        message = str(err)        
    result = ResultContainer(status, message, title, url).call_info()
    return result

def main(url):
    content = fetch_title(url)
    print(content)

if __name__ == '__main__':
    url = sys.argv[1]
    content = main(url)
