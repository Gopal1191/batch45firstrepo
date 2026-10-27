from time import sleep, strftime

while True:
    print("\r" + strftime("%H:%M:%S"), end="", flush=True)
    sleep(1)