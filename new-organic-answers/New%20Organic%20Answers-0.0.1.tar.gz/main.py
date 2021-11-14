import requests, lxml
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_answer(question):
    headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
    }

    params = {
        'q': question,
        'gl': 'us'
    }

    html = requests.get('https://www.google.com/search', headers=headers, params=params)
    soup = BeautifulSoup(html.text, 'lxml')

    answer = soup.select_one('.XcVN5d')

    if answer == None:
        return 'No answer found'
    else:
        return soup.select_one('.XcVN5d').text


def get_snippet(question):
    headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
    }

    params = {
        'q': question,
        'gl': 'us'
    }

    html = requests.get('https://www.google.com/search', headers=headers, params=params)
    soup = BeautifulSoup(html.text, 'lxml')

    snippet = soup.select_one('.hgKElc')

    if snippet == None:
        return 'No answer found'
    else:
        return soup.select_one('.hgKElc').text

def get_link(question):
    headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
    }

    params = {
        'q': question,
        'gl': 'us'
    }

    html = requests.get('https://www.google.com/search', headers=headers, params=params)
    soup = BeautifulSoup(html.text, 'lxml')

    link = soup.select_one('.yuRUbf a')['href']

    return link

def get_title(question):
    headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
    }

    params = {
        'q': question,
        'gl': 'us'
    }
  
    html = requests.get('https://www.google.com/search', headers=headers, params=params)
    soup = BeautifulSoup(html.text, 'lxml')

    title = soup.select_one('.DKV0Md').text

    return title

def get_domain(link):
    domain = urlparse(link).netloc
    return domain


########################################################

# question = 'why is the sky blue'

# print(get_answer(question))
# print(get_snippet(question))
# print(get_title(question))
# link = get_link(question)
# print(link)
# print(get_domain(link))