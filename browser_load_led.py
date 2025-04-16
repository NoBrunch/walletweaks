import RPi.GPIO as GPIO
import time
import psutil
import requests

# Setup GPIO13 for LED
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, GPIO.LOW)  # LED off initially

def is_chromium_running():
    """Check if Chromium is running."""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'chromium-browser':
            return True
    return False

def check_page_load():
    """Check if page is accessible."""
    try:
        response = requests.get('http://localhost:5000', timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def main():
    try:
        # Wait for Chromium and page load (up to 90s)
        print("Waiting for Chromium and page load...")
        for _ in range(90):  # Extended for slow Chromium
            if is_chromium_running() and check_page_load():
                print("Chromium and page loaded.")
                GPIO.output(13, GPIO.HIGH)  # Turn on LED
                return
            time.sleep(1)
        print("Exiting: Chromium or page not loaded.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
