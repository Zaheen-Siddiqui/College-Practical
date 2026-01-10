import threading
import time

balance = 1000

def withdraw(amount):
    global balance
    for _ in range(10):
        if balance >= amount:
            temp = balance
            time.sleep(0.001)  # simulate delay
            temp -= amount
            balance = temp
            print(f"[{threading.current_thread().name}] Withdrawn: ₹{amount}, Remaining: ₹{balance}")

threads = []

for i in range(10):  # 10 threads trying to withdraw ₹100 each
    t = threading.Thread(target=withdraw, args=(100,), name=f"Thread-{i+1}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"\nFinal Balance (WITHOUT LOCK): ₹{balance}")
