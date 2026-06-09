"""
StandardLib_Collections_Itertools.py
Exploring powerful built-in data structures and iteration tools.
"""

from collections import Counter, defaultdict, namedtuple, deque
import itertools

def main():
    print("=== COLLECTIONS MODULE ===")
    
    print("\n--- 1. Counter ---")
    # Great for counting frequencies
    words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
    word_counts = Counter(words)
    print(f"Word Counts: {word_counts}")
    print(f"Most common word: {word_counts.most_common(1)}")

    print("\n--- 2. DefaultDict ---")
    # Prevents KeyError when accessing missing keys
    dd = defaultdict(list)
    dd['fruits'].append('apple')
    dd['fruits'].append('banana')
    # Accessing a missing key returns an empty list instead of error
    print(f"Fruits: {dd['fruits']}")
    print(f"Vegetables (missing key): {dd['vegetables']}")

    print("\n--- 3. NamedTuple ---")
    # Creates simple classes for data containers
    Point = namedtuple('Point', ['x', 'y'])
    p1 = Point(10, 20)
    print(f"Point: {p1}, x={p1.x}, y={p1.y}")

    print("\n--- 4. Deque (Double Ended Queue) ---")
    # Fast appends and pops from both ends (O(1) time)
    dq = deque(['b', 'c', 'd'])
    dq.append('e')      # Add right
    dq.appendleft('a')  # Add left
    print(f"Deque: {dq}")
    dq.pop()            # Remove right
    dq.popleft()        # Remove left
    print(f"Deque after pops: {dq}")

    print("\n=== ITERTOOLS MODULE ===")

    print("\n--- 5. Infinite Iterators (count) ---")
    counter = itertools.count(start=10, step=5)
    print("Counting: ", [next(counter) for _ in range(5)])

    print("\n--- 6. Combinatorics (permutations & combinations) ---")
    letters = ['A', 'B', 'C']
    perms = list(itertools.permutations(letters, 2))
    combs = list(itertools.combinations(letters, 2))
    print(f"Permutations (order matters): {perms}")
    print(f"Combinations (order doesn't matter): {combs}")

    print("\n--- 7. Chaining Iterables ---")
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    chained = list(itertools.chain(list1, list2))
    print(f"Chained List: {chained}")

if __name__ == "__main__":
    main()
