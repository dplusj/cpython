# fibonacci.py

import os
import threading
import time
def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)

start = time.time()

# collect the thraed and join
threads = []
for _ in range(os.cpu_count()):
    t = threading.Thread(target=fib, args=(35,))
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()

print('Time:', time.time() - start)