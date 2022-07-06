import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


def shorten_link(token, url):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    payload = {
        'long_url': f'{url}',
        'domain': 'bit.ly'
    }
    response = requests.post(
        'https://api-ssl.bitly.com/v4/shorten',
        headers=headers,
        json=payload
    )
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, url):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    parsed_url = urlparse(url)
    bitlink = f'{parsed_url.netloc}{parsed_url.path}'
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary',
        headers=headers,
    )
    response.raise_for_status()
    count_clicks = response.json()["total_clicks"]
    return count_clicks


def is_bitlink(url, token):
    parsed_url = urlparse(url)
    link = f'{parsed_url.netloc}{parsed_url.path}'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{link}',
        headers=headers
    )
    return response.ok


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
    description='use bitlink'
)
    parser.add_argument('url', help='input link')
    args = parser.parse_args()
    url = args.url
    token = os.environ['BITLY_TOKEN']
    try:
        if is_bitlink(url, token):
            print('Count of clicks', count_clicks(token, url))
        else:
            print('Bitlink', shorten_link(token, url))
    except requests.exceptions.HTTPError:
        print('Error. Invalid URL.')


if __name__ == '__main__':
    main()

