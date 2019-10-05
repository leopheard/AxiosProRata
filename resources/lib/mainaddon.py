import requests
import re
from bs4 import BeautifulSoup

def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup))
    return soup

def get_playable_podcast(soup):
    subjects = []
    for content in soup.find_all('item'):
        try:
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone-prod.s3.amazonaws.com/podcasts/c11bb198-0ed5-11e9-b104-23783a81f42d/image/53aa1a75b60e36e8a5daaa6f9fde44382b12e7d7db1ee809e53544ddb1cc2126a09b70662657dfa250798d6ffc0f75f332b7bc6e0a6d1fa3009a965dbab2920f.jpeg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast(playable_podcast):
    items = []
    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast1(soup):
    subjects = []
    for content in soup.find_all('item', limit=10):
        try:
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone-prod.s3.amazonaws.com/podcasts/c11bb198-0ed5-11e9-b104-23783a81f42d/image/53aa1a75b60e36e8a5daaa6f9fde44382b12e7d7db1ee809e53544ddb1cc2126a09b70662657dfa250798d6ffc0f75f332b7bc6e0a6d1fa3009a965dbab2920f.jpeg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items
