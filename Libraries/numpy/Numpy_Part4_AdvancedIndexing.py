# =============================================================================
# NUMPY PART 4 - ADVANCED INDEXING & BROADCASTING (Advanced Level)
# =============================================================================
# This part covers boolean indexing, fancy indexing, broadcasting, and more.

import numpy as np

# =============================================================================
# 1. BOOLEAN INDEXING
# =============================================================================
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Original Array:", arr)

# Create boolean mask
mask = arr > 5
print("\nBoolean mask (arr > 5):", mask)

# Apply boolean indexing
filtered = arr[mask]
print("Filtered values:", filtered)

# Direct boolean indexing
print("arr[arr > 5]:", arr[arr > 5])
print("arr[arr % 2 == 0]:", arr[arr % 2 == 0])

# Multiple conditions
print("arr[(arr > 3) & (arr < 8)]:", arr[(arr > 3) & (arr < 8)])
print("arr[(arr < 3) | (arr > 8)]:", arr[(arr < 3) | (arr > 8)])

# 2D Boolean indexing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(arr2d)
print("Values > 4:", arr2d[arr2d > 4])

# Modify values using boolean indexing
arr_copy = arr.copy()
arr_copy[arr_copy > 5] = 0
print("\nSet values > 5 to 0:", arr_copy)

# =============================================================================
# 2. FANCY INDEXING
# =============================================================================
arr = np.arange(10, 20)
print("\nArray:", arr)

# Using array of indices
indices = np.array([0, 3, 5, 7])
print("Indices:", indices)
print("arr[indices]:", arr[indices])

# Negative indices
print("arr[[-1, -3, -5]]:", arr[np.array([-1, -3, -5])])

# 2D fancy indexing
arr2d = np.arange(12).reshape(3, 4)
print("\n2D Array:")
print(arr2d)

# Select specific rows
row_indices = np.array([0, 2])
print("\nRows 0 and 2:")
print(arr2d[row_indices])

# Select specific elements
row_idx = np.array([0, 1, 2])
col_idx = np.array([0, 2, 3])
print("\nElements at (0,0), (1,2), (2,3):", arr2d[row_idx, col_idx])

# =============================================================================
# 3. IX_ FUNCTION (Advanced Fancy Indexing)
# =============================================================================
arr = np.arange(20).reshape(4, 5)
print("\n4x5 Array:")
print(arr)

# Select subarray using ix_
rows = np.array([0, 2, 3])
cols = np.array([1, 3, 4])
subarray = arr[np.ix_(rows, cols)]
print("\nSubarray using ix_(rows, cols):")
print(subarray)

# =============================================================================
# 4. BROADCASTING
# =============================================================================
print("\n" + "="*50)
print("BROADCASTING")
print("="*50)

# Scalar broadcasting
arr = np.array([1, 2, 3, 4, 5])
print("\nArray:", arr)
print("Array * 2:", arr * 2)  # 2 is broadcast to [2, 2, 2, 2, 2]

# 1D with 2D
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr1d = np.array([10, 20, 30])
print("\n2D Array:")
print(arr2d)
print("1D Array:", arr1d)
print("\n2D + 1D (broadcast along columns):")
print(arr2d + arr1d)

# Column broadcasting (need to reshape)
col_arr = np.array([[100], [200], [300]])
print("\nColumn vector:")
print(col_arr)
print("\n2D + column vector (broadcast along rows):")
print(arr2d + col_arr)

# Broadcasting rules:
# 1. Arrays with fewer dimensions are padded with 1s on the left
# 2. Arrays with size 1 along a dimension act as if copied
# 3. Arrays must have compatible shapes (same or 1)

print("\n--- Broadcasting Examples ---")
a = np.ones((3, 4))
b = np.arange(4)
print(f"a shape: {a.shape}, b shape: {b.shape}")
print(f"a + b shape: {(a + b).shape}")

# More complex broadcasting
a = np.ones((3, 1, 4))
b = np.ones((1, 5, 1))
print(f"\na shape: {a.shape}, b shape: {b.shape}")
print(f"a + b shape: {(a + b).shape}")

# =============================================================================
# 5. STRUCTURED ARRAYS
# =============================================================================
print("\n" + "="*50)
print("STRUCTURED ARRAYS")
print("="*50)

# Define structured data type
dt = np.dtype([
    ('name', 'U20'),      # Unicode string, max 20 chars
    ('age', 'i4'),        # 32-bit integer
    ('salary', 'f8')      # 64-bit float
])

# Create structured array
employees = np.array([
    ('Alice', 30, 50000.0),
    ('Bob', 25, 45000.0),
    ('Charlie', 35, 60000.0)
], dtype=dt)

print("\nStructured Array:")
print(employees)
print("\nAccess by field name:", employees['name'])
print("Access by index and field:", employees[0]['name'])

# Filter structured array
print("\nEmployees with salary > 48000:")
print(employees[employees['salary'] > 48000])

# =============================================================================
# 6. RECORD ARRAYS
# =============================================================================
# Similar to structured arrays but with attribute access
rec_arr = np.rec.array([
    ('Alice', 30, 50000.0),
    ('Bob', 25, 45000.0)
], dtype=dt)

print("\nRecord Array:")
print("Names via attribute:", rec_arr.name)
print("First person's age:", rec_arr[0].age)

# =============================================================================
# 7. MASKED ARRAYS
# =============================================================================
print("\n" + "="*50)
print("MASKED ARRAYS")
print("="*50)

# Create masked array
data = np.array([1, 2, -999, 4, 5, -999, 7])
mask = (data == -999)  # True where data is invalid
masked = np.ma.masked_array(data, mask=mask)

print("Original data:", data)
print("Mask (True = invalid):", mask)
print("Masked array:", masked)
print("Mean (ignoring masked):", masked.mean())

# Mask based on condition
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
masked_arr = np.ma.masked_greater(arr, 5)  # Mask values > 5
print("\nMask values > 5:", masked_arr)
print("Sum of unmasked:", masked_arr.sum())

# =============================================================================
# 8. VIEWS VS COPIES
# =============================================================================
print("\n" + "="*50)
print("VIEWS VS COPIES")
print("="*50)

original = np.arange(10)
print("Original:", original)

# Slicing creates a VIEW
view = original[3:7]
print("\nView (slice):", view)
print("Shares memory:", np.shares_memory(original, view))

view[0] = 999
print("After modifying view:")
print("Original:", original)  # Also modified!

# Fancy indexing creates a COPY
original = np.arange(10)
copy = original[[3, 4, 5, 6]]  # Fancy indexing
print("\nCopy (fancy index):", copy)
print("Shares memory:", np.shares_memory(original, copy))

copy[0] = 999
print("After modifying copy:")
print("Original:", original)  # Not modified!

# =============================================================================
# 9. ADVANCED SLICING WITH STEP
# =============================================================================
arr = np.arange(20).reshape(4, 5)
print("\n4x5 Array:")
print(arr)

# Every other row
print("\nEvery other row (::2):")
print(arr[::2])

# Every other element in each row
print("\nEvery other column (::2):")
print(arr[:, ::2])

# Reversed
print("\nReversed rows:")
print(arr[::-1])

print("\nReversed columns:")
print(arr[:, ::-1])

# Complex slicing
print("\nComplex slice [1:, ::2]:")
print(arr[1:, ::2])

# =============================================================================
# 10. ADVANCED TAKE AND PUT
# =============================================================================
arr = np.arange(10, 20)
print("\nArray:", arr)

# take - similar to fancy indexing but with more options
indices = [0, 2, 4, 6]
taken = np.take(arr, indices)
print("Take indices [0,2,4,6]:", taken)

# take with mode='wrap'
indices_wrap = [0, 1, 10, 11]  # 10, 11 are out of bounds
taken_wrap = np.take(arr, indices_wrap, mode='wrap')
print("Take with wrap mode:", taken_wrap)

# put - modify array at specified indices
arr_copy = arr.copy()
np.put(arr_copy, [0, 2, 4], [100, 200, 300])
print("After put:", arr_copy)

print("\n" + "="*50)
print("NUMPY PART 4 - ADVANCED INDEXING COMPLETE!")
print("="*50)
