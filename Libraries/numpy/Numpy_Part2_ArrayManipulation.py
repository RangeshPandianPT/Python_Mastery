# =============================================================================
# NUMPY PART 2 - ARRAY MANIPULATION (Elementary Level)
# =============================================================================
# This part covers reshaping, stacking, splitting, and copying arrays.

import numpy as np

# =============================================================================
# 1. RESHAPING ARRAYS
# =============================================================================

# Create a 1D array
arr = np.arange(12)
print("Original 1D Array:", arr)

# Reshape to 2D
arr_2d = arr.reshape(3, 4)  # 3 rows, 4 columns
print("\nReshaped to 3x4:")
print(arr_2d)

# Reshape to 3D
arr_3d = arr.reshape(2, 2, 3)  # 2 blocks, 2 rows, 3 columns
print("\nReshaped to 2x2x3:")
print(arr_3d)

# Using -1 for automatic dimension calculation
arr_auto = arr.reshape(4, -1)  # 4 rows, calculate columns
print("\nReshaped to 4x(auto):")
print(arr_auto)

# Flatten array back to 1D
flattened = arr_2d.flatten()  # Returns a copy
print("\nFlattened:", flattened)

# Ravel - similar to flatten but may return a view
raveled = arr_2d.ravel()
print("Raveled:", raveled)

# =============================================================================
# 2. TRANSPOSE
# =============================================================================
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("\nOriginal Array (2x3):")
print(arr)

# Transpose (swap rows and columns)
transposed = arr.T
print("\nTransposed (3x2):")
print(transposed)

# Using transpose function
transposed2 = np.transpose(arr)
print("\nUsing np.transpose:")
print(transposed2)

# =============================================================================
# 3. CHANGING DIMENSIONS
# =============================================================================

# Add new axis
arr = np.array([1, 2, 3])
print("\n1D Array:", arr, "shape:", arr.shape)

# newaxis adds a dimension
row_vector = arr[np.newaxis, :]  # 1x3
col_vector = arr[:, np.newaxis]  # 3x1
print("Row vector shape:", row_vector.shape)
print("Column vector shape:", col_vector.shape)

# expand_dims - more explicit
expanded = np.expand_dims(arr, axis=0)
print("Expanded dims:", expanded.shape)

# squeeze - remove dimensions of size 1
arr_with_extra = np.array([[[1, 2, 3]]])  # shape (1, 1, 3)
squeezed = np.squeeze(arr_with_extra)
print("\nBefore squeeze:", arr_with_extra.shape)
print("After squeeze:", squeezed.shape)

# =============================================================================
# 4. STACKING ARRAYS
# =============================================================================
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nArray a:", a)
print("Array b:", b)

# Vertical stack (vstack)
vstacked = np.vstack((a, b))
print("\nVertical Stack:")
print(vstacked)

# Horizontal stack (hstack)
hstacked = np.hstack((a, b))
print("\nHorizontal Stack:", hstacked)

# Stack along new axis
stacked = np.stack((a, b), axis=0)  # Stack as rows
print("\nStack along axis 0:")
print(stacked)

stacked_axis1 = np.stack((a, b), axis=1)  # Stack as columns
print("\nStack along axis 1:")
print(stacked_axis1)

# For 2D arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print("\n2D Stacking:")
print("Vertical:")
print(np.vstack((arr1, arr2)))

print("\nHorizontal:")
print(np.hstack((arr1, arr2)))

# =============================================================================
# 5. CONCATENATING ARRAYS
# =============================================================================
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

print("\nArray a:")
print(a)
print("Array b:")
print(b)

# Concatenate along axis 0 (rows)
concat0 = np.concatenate((a, b), axis=0)
print("\nConcatenate along axis 0:")
print(concat0)

# Concatenate along axis 1 (columns - need matching dimensions)
c = np.array([[5], [6]])
concat1 = np.concatenate((a, c), axis=1)
print("\nConcatenate along axis 1:")
print(concat1)

# =============================================================================
# 6. SPLITTING ARRAYS
# =============================================================================
arr = np.arange(12).reshape(3, 4)
print("\nOriginal Array:")
print(arr)

# Split into equal parts
split3 = np.split(arr, 3, axis=0)  # Split into 3 along rows
print("\nSplit into 3 (axis=0):")
for i, part in enumerate(split3):
    print(f"Part {i}:", part)

# Split along columns
split2 = np.split(arr, 2, axis=1)
print("\nSplit into 2 (axis=1):")
for i, part in enumerate(split2):
    print(f"Part {i}:")
    print(part)

# hsplit and vsplit
hsplit = np.hsplit(arr, 2)  # Horizontal split
vsplit = np.vsplit(arr, 3)  # Vertical split

# Split at specific indices
arr1d = np.arange(10)
parts = np.split(arr1d, [3, 7])  # Split at index 3 and 7
print("\nSplit [0-10] at indices [3, 7]:")
print("Parts:", [p.tolist() for p in parts])

# =============================================================================
# 7. COPYING ARRAYS
# =============================================================================

# IMPORTANT: Assignment is NOT a copy!
original = np.array([1, 2, 3, 4, 5])

# This creates a VIEW, not a copy
view = original
view[0] = 100
print("\nAfter modifying view:")
print("Original:", original)  # Also changed!
print("View:", view)

# Reset
original = np.array([1, 2, 3, 4, 5])

# Using .copy() creates a TRUE copy
copy = original.copy()
copy[0] = 100
print("\nAfter modifying copy:")
print("Original:", original)  # Unchanged
print("Copy:", copy)

# Slices are also views!
original = np.array([1, 2, 3, 4, 5])
slice_view = original[1:4]
slice_view[0] = 999
print("\nAfter modifying slice:")
print("Original:", original)  # Changed!

# =============================================================================
# 8. REPEATING AND TILING
# =============================================================================
arr = np.array([1, 2, 3])

# repeat - repeat each element
repeated = np.repeat(arr, 3)
print("\nRepeat each element 3 times:", repeated)

# tile - repeat the whole array
tiled = np.tile(arr, 3)
print("Tile array 3 times:", tiled)

# 2D tiling
arr2d = np.array([[1, 2], [3, 4]])
tiled2d = np.tile(arr2d, (2, 3))  # 2 times vertically, 3 times horizontally
print("\nTiled 2D array (2, 3):")
print(tiled2d)

# =============================================================================
# 9. APPEND, INSERT, DELETE
# =============================================================================
arr = np.array([1, 2, 3, 4, 5])
print("\nOriginal:", arr)

# Append
appended = np.append(arr, [6, 7, 8])
print("Appended:", appended)

# Insert
inserted = np.insert(arr, 2, [10, 20])  # Insert at index 2
print("Inserted at index 2:", inserted)

# Delete
deleted = np.delete(arr, [1, 3])  # Delete indices 1 and 3
print("Deleted indices 1, 3:", deleted)

# =============================================================================
# 10. FLIP AND ROTATE
# =============================================================================
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("\nOriginal:")
print(arr)

# Flip vertically
print("\nFlip vertical (flipud):")
print(np.flipud(arr))

# Flip horizontally
print("\nFlip horizontal (fliplr):")
print(np.fliplr(arr))

# Rotate 90 degrees
print("\nRotate 90 degrees:")
print(np.rot90(arr))

# Rotate 180 degrees
print("\nRotate 180 degrees:")
print(np.rot90(arr, 2))

print("\n" + "="*50)
print("NUMPY PART 2 - ARRAY MANIPULATION COMPLETE!")
print("="*50)
