
import time
from datetime import datetime
import winsound

def alarm_clock():
    alarm_time = input("Enter alarm time (HH:MM in 24-hour format): ")

    try:
        datetime.strptime(alarm_time, "%H:%M")
    except ValueError:
        print("Invalid time format! Example: 18:30")
        return

    print(f"Alarm set for {alarm_time}")
    print("Waiting for alarm...")

    while True:
        current_time = datetime.now().strftime("%H:%M")

        if current_time == alarm_time:
            print("\n⏰ WAKE UP! ALARM TIME!")
            
            # Play alarm sound for 30 seconds
            for _ in range(30):
                winsound.Beep(1000, 1000)
            break

        time.sleep(1)

if __name__ == "__main__":
    alarm_clock()
