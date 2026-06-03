import threading
import time
def main():
    start_event = threading.Event()

    def worker(i):
        start_event.wait()
        print(f"Running Thread {i}")
        

    for i in range(5):
        t = threading.Thread(target = worker, args=(i,))
        t.start()

    time.sleep(2)
    
    start_event.set()    
if __name__ == '__main__':
    main()