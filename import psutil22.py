import psutil
from time import sleep
from datetime import datetime
from gpiozero import LED

 #Setup GPIO pins
GREEN_LED = 27
YELLOW_LED = 17
RED_LED = 22


def log_cpu_usage():
    with open("cpu_usage_log.txt", "a") as log_file:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"Total CPU Usage: {cpu_usage}%")
            timestamp = f"{datetime.now().strftime('%Y/%m/%d %HH %MM %SS')}"
            x = f"{timestamp} - CPU Usage: {cpu_usage}%\n"
            log_file.write(x)
            print(f'{timestamp} - CPU Usage: {cpu_usage}%')
            
        #control LEDs based on CPU usage
            if cpu_usage < 50:
                LED.output(GREEN_LED, LED.HIGH)
                LED.output(YELLOW_LED, LED.LOW)
                LED.output(RED_LED, LED.LOW)
            elif cpu_usage < 80:
                LED.output(GREEN_LED, LED.LOW)
                LED.output(YELLOW_LED, LED.HIGH)
                LED.output(RED_LED, LED.LOW)
            else:
                LED.output(GREEN_LED, LED.LOW)
                LED.output(YELLOW_LED, LED.LOW)
                LED.output(RED_LED, LED.HIGH)
    sleep(5)
log_cpu_usage()