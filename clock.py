from datetime import datetime
import time


try:
    while True:
        now = datetime.now()
        print(f"\r{now:%H:%M:%S}", end="", flush=True)
        time.sleep(1 - now.microsecond / 1_000_000)
except KeyboardInterrupt:
    print("\nClock stopped.")
