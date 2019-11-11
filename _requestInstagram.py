import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup as bs
import os

def write_log(log_message):
    text_data = None

    with open('logs/log.txt', 'r') as log:
        text_data = log.read()

    with open('logs/log.txt', 'w') as log:
        text_data += log_message
        log.write(text_data)
        log.write('\n')

def makeRequest(keyword):

    print(f'incoming keyword:{keyword}')
    url = f'https://www.instagram.com/explore/tags/{keyword}/?hl=ko'

    os.makedirs(os.path.dirname(f'search_history/{keyword}/'), exist_ok=True)
    os.makedirs(os.path.dirname(f'logs/'), exist_ok=True)

    log_message = ''
    filename = ''
    count = 0
    timenow = datetime.now()

    r = requests.get(url)

    if r.status_code == 200:

        with open('output.txt', 'w') as f:
            f.write('hello')
            f.write(r.text)

        soup = bs(r.text, 'html.parser')

        target = soup.find_all('script')

        try:
            data = json.loads(target[3].string[21:-1])
        except TypeError:
            data = None

        if data:
            with open(f'search_history/{keyword}/{int(datetime.timestamp(timenow))}.json', 'w') as f:
                filename = f.name     
                json.dump(data, f)
                
                # print(data.get('entry_data'))
                with open(f'search_history/{keyword}/{int(datetime.timestamp(datetime.now()))}.txt', 'w') as f2:
                    mod_data = data.get('entry_data').get('TagPage')[0].get('graphql').get('hashtag').get('edge_hashtag_to_media')
                    # print(mod_data)
                    count = mod_data.get('count')
                    f2.write(str(count))
                    f2.write('\n')
                    for d in mod_data.get('edges'):
                        f2.write(d.get('node').get('id'))
                        f2.write('\n')

        log_message = f'filename: {filename}, log time: {timenow.isoformat()}, keyword: {keyword}\n   current counts: {count}'

    else:
        log_message = f'log time: {timenow.isoformat()}, keyword: {keyword}\n   Error: status code {r.status_code}'


    write_log(log_message)

    return count