# =============================================================================
# NUMPY PART 1 - BASICS (Beginner Level)
# =============================================================================
# NumPy is the fundamental package for scientific computing in Python.
# It provides support for large, multi-dimensional arrays and matrices.

import numpy as np

# =============================================================================
# 1. CREATING ARRAYS
# =============================================================================

# ----- From Python Lists -----
# 1D Array
arr1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1d)
print("Type:", type(arr1d))

# 2D Array (Matrix)
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(arr2d)

# 3D Array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Array:")
print(arr3d)

# ----- Special Arrays -----
# Array of zeros
zeros = np.zeros((3, 4))  # 3 rows, 4 columns
print("\nZeros Array:")
print(zeros)

# Array of ones
ones = np.ones((2, 3))
print("\nOnes Array:")
print(ones)

# Array with a constant value
full = np.full((2, 2), 7)  # 2x2 array filled with 7
print("\nFull Array (filled with 7):")
print(full)

# Identity matrix
identity = np.eye(3)  # 3x3 identity matrix
print("\nIdentity Matrix:")
print(identity)

# Empty array (uninitialized)
empty = np.empty((2, 2))  # Values are random/garbage
print("\nEmpty Array (uninitialized):")
print(empty)

# =============================================================================
# 2. ARRAY RANGES
# =============================================================================

# arange - like Python's range()
arr_range = np.arange(0, 10, 2)  # start, stop, step
print("\nnp.arange(0, 10, 2):", arr_range)

# linspace - evenly spaced values
arr_linspace = np.linspace(0, 1, 5)  # 5 values from 0 to 1
print("np.linspace(0, 1, 5):", arr_linspace)

# logspace - logarithmically spaced values
arr_logspace = np.logspace(0, 2, 5)  # 5 values from 10^0 to 10^2
print("np.logspace(0, 2, 5):", arr_logspace)

# =============================================================================
# 3. ARRAY ATTRIBUTES
# =============================================================================
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("\nSample Array:")
print(arr)

print("\nArray Attributes:")
print("Shape:", arr.shape)       # (3, 4) - 3 rows, 4 columns
print("Dimensions:", arr.ndim)   # 2
print("Size:", arr.size)         # 12 (total elements)
print("Data Type:", arr.dtype)   # int64 or int32
print("Item Size:", arr.itemsize, "bytes")  # Size of each element
print("Total Bytes:", arr.nbytes)  # Total memory used

# =============================================================================
# 4. DATA TYPES
# =============================================================================

# Specify data type during creation
arr_int = np.array([1, 2, 3], dtype=np.int32)
arr_float = np.array([1, 2, 3], dtype=np.float64)
arr_complex = np.array([1, 2, 3], dtype=np.complex128)
arr_bool = np.array([1, 0, 1], dtype=np.bool_)

print("\nData Types:")
print("Integer array:", arr_int, "dtype:", arr_int.dtype)
print("Float array:", arr_float, "dtype:", arr_float.dtype)
print("Complex array:", arr_complex, "dtype:", arr_complex.dtype)
print("Boolean array:", arr_bool, "dtype:", arr_bool.dtype)

# Convert data type
arr_converted = arr_int.astype(np.float64)
print("\nConverted to float:", arr_converted)

# =============================================================================
# 5. BASIC INDEXING
# =============================================================================
arr = np.array([10, 20, 30, 40, 50])
print("\n1D Array:", arr)

# Single element
print("First element (index 0):", arr[0])
print("Last element (index -1):", arr[-1])
print("Second last (index -2):", arr[-2])

# 2D Indexing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(arr2d)
print("Element at [0, 0]:", arr2d[0, 0])  # 1
print("Element at [1, 2]:", arr2d[1, 2])  # 6
print("Element at [2, -1]:", arr2d[2, -1])  # 9

# =============================================================================
# 6. BASIC SLICING
# =============================================================================
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("\nOriginal Array:", arr)

# Basic slicing: arr[start:stop:step]
print("arr[2:7]:", arr[2:7])      # Elements 2 to 6
print("arr[:5]:", arr[:5])        # First 5 elements
print("arr[5:]:", arr[5:])        # From index 5 to end
print("arr[::2]:", arr[::2])      # Every other element
print("arr[::-1]:", arr[::-1])    # Reversed array

# 2D Slicing
arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("\n2D Array:")
print(arr2d)
print("\nFirst 2 rows:", arr2d[:2])
print("\nFirst 2 columns:")
print(arr2d[:, :2])
print("\nSubarray [rows 0-1, cols 1-2]:")
print(arr2d[0:2, 1:3])

# =============================================================================
# 7. BASIC OPERATIONS
# =============================================================================
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print("\nArray a:", a)
print("Array b:", b)

# Element-wise operations
print("\nAddition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("Division (a / b):", a / b)
print("Power (a ** 2):", a ** 2)

# Scalar operations
print("\nScalar addition (a + 10):", a + 10)
print("Scalar multiplication (a * 3):", a * 3)

# =============================================================================
# 8. BASIC FUNCTIONS
# =============================================================================
arr = np.array([1, 2, 3, 4, 5])

print("\nBasic Functions:")
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))
print("Standard Deviation:", np.std(arr))

# Argmax/Argmin - index of max/min
print("Index of Max:", np.argmax(arr))
print("Index of Min:", np.argmin(arr))

# Cumulative sum
print("Cumulative Sum:", np.cumsum(arr))

print("\n" + "="*50)
print("NUMPY PART 1 - BASICS COMPLETE!")
print("="*50)
