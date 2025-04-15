#!/usr/bin/env python3
import RPi.GPIO as GPIO

OS_LED = 12  # GPIO 12 for OS loaded LED

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(OS_LED, GPIO.OUT)
GPIO.output(OS_LED, GPIO.HIGH)  # Turn on LED
