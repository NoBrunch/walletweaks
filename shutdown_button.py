#!/usr/bin/env python3
import RPi.GPIO as GPIO
import subprocess
import time

# GPIO pin definitions
BUTTON_PIN = 6   # GPIO 6 for push button
LED1 = 12        # GPIO 12 for first LED
LED2 = 13        # GPIO 13 for second LED

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button with internal pull-up
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

# Ensure LEDs are off initially
GPIO.output(LED1, GPIO.LOW)
GPIO.output(LED2, GPIO.LOW)

def shutdown():
    """Handle shutdown with LED feedback."""
    print("Button pressed! Initiating shutdown...")
    for _ in range(3):
        GPIO.output(LED1, GPIO.HIGH)
        GPIO.output(LED2, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(LED1, GPIO.LOW)
        GPIO.output(LED2, GPIO.LOW)
        time.sleep(0.3)
    subprocess.run(["sudo", "shutdown", "-h", "now"])

try:
    print("Monitoring button on GPIO 6 (polling). Press to shut down.")
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            time.sleep(0.2)  # Debounce delay
            if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # Confirm still pressed
                shutdown()
                break  # Exit after shutdown
        time.sleep(0.1)  # Poll every 100ms

except KeyboardInterrupt:
    print("\nStopping button monitoring.")

finally:
    GPIO.cleanup()
    print("GPIO cleaned up.")
