import sys
from datetime import datetime
from time import sleep
from source import _initializer as init
from source import _log as log
from source import _request as req
# # source for raspberrypi
# from source import _raspberrypi as pi

# get keyword and count from upper process
keyword = sys.argv[1]
prev_count = int(sys.argv[2])

# make directory with keyword
log.log_history_mkdir(keyword)

while True:
    count, log_message, data = req.makeRequest(keyword)
    
    if prev_count != count:
        log_message += f'difference: {count-prev_count}'
        # do something on count change
        # ...
    else:
        log_message += f'difference: {count-prev_count}'

    prev_count = count
    log.log_count(count, keyword)

    if data:
        log.log_history(data, keyword)
        
    log.log(log_message)

    sleep(3)