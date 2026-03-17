"""
Raspberry Pi Project - Main Script
Author: Your Name
Date: 2024

Description:
    Entry point for the Raspberry Pi project.
    Replace this with your actual project code.
"""

import RPi.GPIO as GPIO
import time
# import any other libraries you used

# ─── Configuration ────────────────────────────────────────────────
LED_PIN = 18        # Change to your actual GPIO pin
BUTTON_PIN = 17     # Change to your actual GPIO pin
DELAY = 0.5         # Seconds

# ─── Setup ────────────────────────────────────────────────────────
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    print("[INFO] GPIO setup complete.")

# ─── Main Logic ───────────────────────────────────────────────────
def run():
    print("[INFO] Project running. Press Ctrl+C to stop.")
    try:
        while True:
            button_state = GPIO.input(BUTTON_PIN)

            if button_state == GPIO.LOW:
                GPIO.output(LED_PIN, GPIO.HIGH)
                print("[ACTION] Button pressed — LED ON")
            else:
                GPIO.output(LED_PIN, GPIO.LOW)

            time.sleep(DELAY)

    except KeyboardInterrupt:
        print("\n[INFO] Stopping...")

# ─── Cleanup ──────────────────────────────────────────────────────
def cleanup():
    GPIO.cleanup()
    print("[INFO] GPIO cleaned up.")

# ─── Entry Point ──────────────────────────────────────────────────
if __name__ == "__main__":
    setup()
    run()
    cleanup()
