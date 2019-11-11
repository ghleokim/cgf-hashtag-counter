from time import sleep
from _requestInstagram import makeRequest
from gpiozero import LED

relay = LED(17)
keyword = '싸구려인조인간'

# turn on signal
for i in range(3):
    relay.on()
    sleep(0.5)
    relay.off()
    sleep(0.5)


def makeSignal():
    print('signal')
    relay.on()
    sleep(3)
    relay.off()
    
    
# read log
try:
    with open(f'logs/log_{keyword}.txt', 'r') as f:
        count_log = int(f.readlines()[-1])
except:
    with open(f'logs/log_{keyword}.txt', 'w') as f:
        f.write('1')
        f.write('\n')


while True:
    count = makeRequest(keyword)
    print('count', count)

    if count != count_log:
        makeSignal()

    count_log = count

    with open(f'logs/log_{keyword}.txt', 'a') as f:
        f.write(str(count))
        f.write('\n')
    
    sleep(5)