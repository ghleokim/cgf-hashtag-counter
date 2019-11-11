from subprocess import Popen
import sys
from _requestInstagram import write_log
from datetime import datetime
from time import sleep

filename = '_noudp_request'

while True:
    log_message = f'from {sys.argv[0]} executing {filename}, time {datetime.now().isoformat()}'
    write_log(log_message)
    print(f'Starting {filename}...')
    p = Popen(f'python3 {filename}.py', shell=True)

    # Below is for Windows Use
    # p = Popen(f'python {filename}.py', shell=True)
    
    p.wait()
    sleep(5)