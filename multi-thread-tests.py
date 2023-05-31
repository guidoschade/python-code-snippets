import threading
import time
import random

# main function
def main():
  threads = list()
  for idx in range(10):
    x = threading.Thread(target=threadTask, args=(idx,))
    threads.append(x)
    x.start()

  # wait until all threads are comppleted
  while True:
     time.sleep(1)
     nthreads = threading.active_count()
     if nthreads == 1:
        break
     print("Number of threads still running:", nthreads - 1)

# simple test thread task
def threadTask(name):
    seconds = random.randint(1, 10)
    print(f"Starting thread #{name} (sleeping for {seconds} seconds)")
    time.sleep(seconds)
    print(f"Finishing thread #{name}")

# entry
if __name__ == "__main__":
    main()
