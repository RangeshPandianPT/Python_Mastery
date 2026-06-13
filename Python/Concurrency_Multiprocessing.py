# ============================================================
# CONCURRENCY: MULTIPROCESSING
# ============================================================
# Multiprocessing is used to run multiple processes concurrently.
# Unlike threads, processes have their own memory space and their 
# own Python interpreter. This completely bypasses the Global 
# Interpreter Lock (GIL), making multiprocessing ideal for CPU-bound 
# tasks (heavy math, image processing, data crunching).
# ============================================================

import multiprocessing
import time
import math

print("=" * 50)
print("1. CPU-BOUND TASK EXAMPLE")
print("=" * 50)

def compute_heavy_math(n):
    """A CPU intensive operation."""
    count = 0
    for i in range(1, n):
        count += math.sqrt(i)
    return count

if __name__ == '__main__':
    # It is crucial to put multiprocessing code inside the 
    # if __name__ == '__main__': block on Windows to avoid 
    # recursive infinite process creation.

    numbers = [5_000_000, 5_000_000, 5_000_000, 5_000_000]

    print("Running sequentially (may take a few seconds)...")
    start_seq = time.time()
    for n in numbers:
        compute_heavy_math(n)
    print(f"Sequential processing took {time.time() - start_seq:.2f} seconds.")

    print("\nRunning with Multiprocessing...")
    start_multi = time.time()
    
    # Create processes
    processes = []
    for n in numbers:
        p = multiprocessing.Process(target=compute_heavy_math, args=(n,))
        processes.append(p)
        p.start()
        
    for p in processes:
        p.join()
        
    print(f"Multiprocessing took {time.time() - start_multi:.2f} seconds.")


    print("\n" + "=" * 50)
    print("2. PROCESS POOL EXECUTOR (MODERN WAY)")
    print("=" * 50)
    import concurrent.futures

    start_pool = time.time()
    
    # Using ProcessPoolExecutor
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(compute_heavy_math, numbers))
        
    print(f"ProcessPoolExecutor took {time.time() - start_pool:.2f} seconds.")
    # Notice that we don't print the results here just to keep the console clean,
    # but 'results' holds the returned values in order.

    print("\n" + "=" * 50)
    print("3. SHARING STATE BETWEEN PROCESSES (ADVANCED)")
    print("=" * 50)
    # Because processes have separate memory, you must use special 
    # objects to share data between them.
    
    def deposit(balance, amount):
        for _ in range(100):
            time.sleep(0.01)
            balance.value += amount

    def withdraw(balance, amount):
        for _ in range(100):
            time.sleep(0.01)
            balance.value -= amount

    # A Value object from multiprocessing module allows safe sharing
    # 'd' stands for double precision float
    shared_balance = multiprocessing.Value('d', 200.0)
    
    print(f"Initial balance: {shared_balance.value}")
    
    p1 = multiprocessing.Process(target=deposit, args=(shared_balance, 5.0))
    p2 = multiprocessing.Process(target=withdraw, args=(shared_balance, 5.0))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print(f"Final balance: {shared_balance.value}")
    print("(Note: Without locks, shared state can still have race conditions. This is just a demo.)")
