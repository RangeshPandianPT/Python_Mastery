# ============================================================
# CONCURRENCY: ASYNCIO
# ============================================================
# Asyncio is a library to write concurrent code using the async/await syntax.
# It uses an event loop to run asynchronous tasks. It's fantastic for
# I/O-bound tasks and highly scalable network servers (like FastAPI).
# It uses a single thread and single process!
# ============================================================

import asyncio
import time

print("=" * 50)
print("1. BASIC ASYNC/AWAIT")
print("=" * 50)

# The 'async' keyword defines a coroutine
async def fetch_data(id, delay):
    print(f"Task {id}: Starting fetch...")
    # 'await' yields control back to the event loop while waiting
    await asyncio.sleep(delay)  
    print(f"Task {id}: Finished fetch after {delay}s!")
    return {"id": id, "data": f"Sample data {id}"}

async def main_basic():
    print("Running sequential awaits (Defeats the purpose of asyncio!)")
    start = time.time()
    await fetch_data(1, 2)
    await fetch_data(2, 2)
    print(f"Took: {time.time() - start:.2f}s\n")
    
    print("Running concurrently with asyncio.gather:")
    start = time.time()
    # gather runs multiple coroutines concurrently
    results = await asyncio.gather(
        fetch_data(1, 2),
        fetch_data(2, 2),
        fetch_data(3, 2)
    )
    print(f"Results: {results}")
    print(f"Took: {time.time() - start:.2f}s") # Should take ~2 seconds total!

# To run an async function from a normal script, use asyncio.run()
asyncio.run(main_basic())


print("\n" + "=" * 50)
print("2. ASYNC TASKS")
print("=" * 50)
# Tasks are used to schedule coroutines concurrently.

async def background_task(name):
    print(f"Background Task '{name}' started")
    await asyncio.sleep(1)
    print(f"Background Task '{name}' finished")

async def main_tasks():
    # Create a task (starts running immediately in the background)
    task1 = asyncio.create_task(background_task("Logging"))
    task2 = asyncio.create_task(background_task("Metrics"))
    
    print("Doing some other work in the main function while tasks run...")
    await asyncio.sleep(0.5)
    print("Main work done.")
    
    # Wait for the background tasks to finish
    await task1
    await task2

asyncio.run(main_tasks())


print("\n" + "=" * 50)
print("3. ASYNC QUEUES")
print("=" * 50)
# Asyncio has its own queues for producer-consumer patterns

async def producer(queue):
    for i in range(3):
        print(f"Producer: adding item {i}")
        await queue.put(i)
        await asyncio.sleep(0.5) # simulate work
    
    # Send a sentinel value to indicate completion
    await queue.put(None)

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumer: processing item {item}")
        await asyncio.sleep(1) # simulate work
        queue.task_done()

async def main_queue():
    queue = asyncio.Queue()
    
    # Run producer and consumer concurrently
    await asyncio.gather(
        producer(queue),
        consumer(queue)
    )

asyncio.run(main_queue())
