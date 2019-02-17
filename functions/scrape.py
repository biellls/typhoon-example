import logging

import pandas as pd
import requests
from scrapy import Selector


def get_titles(response):
    return Selector(response).css('.athing > .title > a::text').extract()


def get_links(response):
    return Selector(response).css('.athing > .title > a::attr(href)').extract()


def get_scores(response):
    raw_scores = (x.css('.score::text').extract_first() for x in Selector(response).css('.subtext'))
    return [int(x.split()[0]) if x else 0 for x in raw_scores]


def get_comments(response):
    raw_comments = (x.css('a:nth-child(6)[href^="item"]::text').extract_first() for x in Selector(response).css('.subtext'))
    return [0 if x is None or x == 'discuss' else int(x.split('\xa0')[0]) for x in raw_comments]


def get_comment_links(response):
    return [x.css('a[href^="item"]::attr(href)').extract_first() for x in Selector(response).css('.subtext')]


def get_users(response):
    return [x.css('a[href^="user"]::text').extract_first() for x in Selector(response).css('.subtext')]


def extract_hackernews_page(page_num: int = 1):
    url = f'https://news.ycombinator.com/news?p={page_num}'
    logging.info(f'Scraping stories from {url}')
    response = requests.get(url=url)
    data = {
        'title': get_titles(response),
        'link': get_links(response),
        'score': get_scores(response),
        'comment': get_comments(response),
        'comment_link': get_comment_links(response),
        'user': get_users(response),
    }

    df = pd.DataFrame(data, columns=['title', 'user', 'score', 'comment', 'link', 'comment_link'])
    yield df, page_num
