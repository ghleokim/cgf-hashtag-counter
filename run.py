import os
import sys
import json
from subprocess import Popen
from source import _initializer as init
from source import _log as log
from time import sleep
from datetime import datetime


# 1. initialize keyword, count
filepath = os.path.join(init.BASE_DIR, 'counter.py')
jsonpath = os.path.join(init.BASE_DIR, 'json', 'settings.json')

with open(f'{jsonpath}', 'r', encoding='utf-8') as setting:
    data = json.loads(setting.read())

    keyword = data.get('keyword').split()[0]
    prev_count = log.log_count_get_or_create(keyword)


# 2. start process
while True:
    log.log(f'\n::: Starting counter.py ... {datetime.now().isoformat()}')

    p = Popen(f'python3 {filepath} {keyword} {prev_count}', shell=True)

    # Below is for Windows Use
    # p = Popen(f'python {filename}.py', shell=True)

    returncode = p.wait()

    log.log(f'::: Finished counter.py ... {datetime.now().isoformat()}')
    log.log(f'::: Process finished with return code {returncode}\n')

    sleep(5)