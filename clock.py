import time
import math

seconds = int(input("Timer duration in seconds: "))

if seconds <= 0:
    raise ValueError("Duration must be greater than zero.")

deadline = time.monotonic() + seconds

while True:
    remaining = max(0, math.ceil(deadline - time.monotonic()))
    if remaining == 0:
        break

    minutes, secs = divmod(remaining, 60)
    print(f"\rTime remaining: {minutes:02}:{secs:02}", end="", flush=True)
    time.sleep(min(1, deadline - time.monotonic()))

print("\rTime's up!          ")