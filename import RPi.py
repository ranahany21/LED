import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import csv

# GPIO setup
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2
    return distance

def get_temperature():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    return temperature

with open('sensor_data.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "Temperature", "Distance"])

    while True:
            distance = get_distance()
            temperature = get_temperature()
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")

            writer.writerow([current_time, temperature, distance])
            print(f"Time: {current_time}, Temperature: {temperature}°C, Distance: {distance} cm")
            time.sleep(1)