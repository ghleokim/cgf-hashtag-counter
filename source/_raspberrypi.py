from gpiozero import LED
from time import sleep

signal = LED(17)

# make N signals for T seconds interval.
def makeSignal(T=1, N=1):
    for _ in range(N):
        signal.on()
        sleep(T)
        signal.off()
