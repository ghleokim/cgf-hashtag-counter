import os
import json
from datetime import datetime
from ._initializer import BASE_DIR


def log(message):
    print(message)


def log_count(count, keyword):
    with open(f'{BASE_DIR}/log/count/{keyword}.txt', 'a') as f:
        f.write(str(count))
        f.write('\n')


def log_count_get_or_create(keyword):
    countpath = f'{BASE_DIR}/log/count/{keyword}.txt'
    count = 0

    try:
        with open(f'{countpath}', 'r', encoding='utf-8') as f:
            count = int(f.readlines()[-1])
    except:
        with open(f'{countpath}', 'w', encoding='utf-8') as f:
            f.write('0')
            f.write('\n')
    
    return count


def log_history(data, keyword):
    cutoff_data = data.get('entry_data').get('TagPage')[0].get('graphql').get('hashtag')
    
    try:
        del cutoff_data['edge_hashtag_to_top_posts']
        del cutoff_data['edge_hashtag_to_media']['edges'][4:]
        data['entry_data']['TagPage'][0]['graphql']['hashtag'] = cutoff_data
    except:
        log('problem with data processing')
    
    timenow = datetime.now()

    # write time index
    try:
        with open(f'{BASE_DIR}/log/index/timeindex.json', 'r', encoding='utf-8') as f_log:
            log_data = json.loads(f_log.read())
            if log_data.get('data').get(keyword) is None:
                log_data['data'][keyword] = []
    
    # when file doesn't exist
    except FileNotFoundError:
        with open(f'{BASE_DIR}/log/index/timeindex.json', 'w', encoding='utf-8') as f_log:
            log_data = {
                'data': {
                    keyword: []
                },
            }
            json.dump(log_data, f_log)

    # when file has no/wrong data
    except json.decoder.JSONDecodeError:
        log_data = {
                'data': {
                    keyword: []
                },
            }
        with open(f'{BASE_DIR}/log/index/timeindex.json', 'w', encoding='utf-8') as f_log:
            json.dump(log_data, f_log)

    # write new data
    with open(f'{BASE_DIR}/log/index/timeindex.json', 'w', encoding='utf-8') as f_log:
        log_data['data'][keyword].append(int(datetime.timestamp(timenow)))
        json.dump(log_data, f_log)


    # dump data to json
    with open(f'{BASE_DIR}/log/search_history/{keyword}/{int(datetime.timestamp(timenow))}_BIG.json', 'w', encoding='utf-8') as f_big:
        json.dump(data, f_big)

    # store count and id as json
    with open(f'{BASE_DIR}/log/search_history/{keyword}/{int(datetime.timestamp(timenow))}_SHORT.json', 'w', encoding='utf-8') as f_short:
        ref_data = data.get('entry_data').get('TagPage')[0].get('graphql').get('hashtag').get('edge_hashtag_to_media')
        count = ref_data.get('count')
        edges = ref_data.get('edges')

        short_data = {
            'count': str(count),
            'edges': edges[:3]
        }

        json.dump(short_data, f_short)


def log_history_mkdir(keyword):
    os.makedirs(f'{BASE_DIR}/log/search_history/{keyword}/', exist_ok=True)

