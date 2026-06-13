# ============================================================
# CONCURRENCY: THREADING
# ============================================================
# Threading is used to run multiple threads (smaller units of a process)
# concurrently. It is best used for I/O-bound tasks (like downloading
# files, web scraping, or waiting for network responses) because the 
# Python Global Interpreter Lock (GIL) prevents threads from executing 
# Python bytecodes at exactly the same time in CPython.
# ============================================================

import threading
import time
import urllib.request

print("=" * 50)
print("1. BASIC THREADING")
print("=" * 50)

def print_numbers():
    for i in range(1, 6):
        time.sleep(0.5)
        print(f"Number: {i}")

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        time.sleep(0.6)
        print(f"Letter: {letter}")

print("Running sequentially (takes ~5.5s):")
start_time = time.time()
# print_numbers()
# print_letters()
print("Skipping sequential to save time in this demo...")

print("\nRunning with threads (takes ~3s):")
start_time = time.time()

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete before moving on
thread1.join()
thread2.join()

print(f"Threads completed in {time.time() - start_time:.2f} seconds.")


print("\n" + "=" * 50)
print("2. I/O BOUND TASK EXAMPLE (DOWNLOADING)")
print("=" * 50)

def download_site(url):
    print(f"Starting download: {url}")
    with urllib.request.urlopen(url) as response:
        content = response.read()
    print(f"Finished download: {url} ({len(content)} bytes)")

urls = [
    "http://www.python.org",
    "http://www.wikipedia.org",
    "http://www.github.com"
]

print("Downloading sequentially...")
start_seq = time.time()
for url in urls:
    download_site(url)
print(f"Sequential download took {time.time() - start_seq:.2f} seconds.")

print("\nDownloading with threading...")
start_thr = time.time()
threads = []
for url in urls:
    t = threading.Thread(target=download_site, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print(f"Threaded download took {time.time() - start_thr:.2f} seconds.")


print("\n" + "=" * 50)
print("3. THREAD POOL EXECUTOR (MODERN WAY)")
print("=" * 50)
# concurrent.futures provides a higher-level interface for threading

import concurrent.futures

def square_number(n):
    time.sleep(0.5) # Simulate some work
    return n * n

numbers = [1, 2, 3, 4, 5]

print("Using ThreadPoolExecutor:")
start_pool = time.time()

# Using map
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # map returns the results in the order the iterables were given
    results = list(executor.map(square_number, numbers))

print(f"Results: {results}")
print(f"ThreadPoolExecutor took {time.time() - start_pool:.2f} seconds.")
