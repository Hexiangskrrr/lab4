from hal import hal_input_switch as switch
from hal import hal_led as led
from time import sleep
import time
def main():
    led.init()
    switch.init()
    while True:
        if switch.read_slide_switch() == 0:
            led.set_output(1,1)
            sleep(0.1)
            led.set_output(1, 0)
            sleep(0.1)
        else:
            led.set_output(1, 1)
            sleep(0.2)
            led.set_output(1, 0)
            sleep(0.2)
if __name__=='__main__':
    main()

