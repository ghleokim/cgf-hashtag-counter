import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup as bs

def makeRequest(keyword):
    url = f'https://www.instagram.com/explore/tags/{keyword}/?hl=ko'
    count = 0
    timenow = datetime.now()

    r = requests.get(url)

    log_message = f'time: {timenow.isoformat()}, STATUS CODE: {r.status_code}, keyword: {keyword}, '

    if r.status_code == 200:
        soup = bs(r.text, 'html.parser')
        target = soup.find_all('script')

        # get data from target
        try:
            data = json.loads(target[3].string[21:-1])
        except TypeError:
            data = None

        if data:
            count = data.get('entry_data').get('TagPage')[0].get('graphql').get('hashtag').get('edge_hashtag_to_media').get('count')

        log_message += f'count: {count}'

    else:
        log_message = f'count: failed with status code {r.status_code}'

    return (count, log_message, data)