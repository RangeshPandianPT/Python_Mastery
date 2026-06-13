# =============================================================================
# NUMPY PART 3 - MATHEMATICAL OPERATIONS (Intermediate Level)
# =============================================================================
# This part covers mathematical functions, statistics, and linear algebra basics.

import numpy as np

# =============================================================================
# 1. UNIVERSAL FUNCTIONS (ufuncs)
# =============================================================================
arr = np.array([1, 4, 9, 16, 25])
print("Original Array:", arr)

# Basic math functions
print("\nBasic Math Functions:")
print("Square root:", np.sqrt(arr))
print("Square:", np.square(arr))
print("Cube:", np.power(arr, 3))
print("Absolute:", np.abs(np.array([-1, -2, 3, -4])))

# Exponential and logarithmic
print("\nExponential & Logarithmic:")
print("Exponential (e^x):", np.exp([1, 2, 3]))
print("Natural log:", np.log([1, np.e, np.e**2]))
print("Log base 10:", np.log10([1, 10, 100]))
print("Log base 2:", np.log2([1, 2, 4, 8]))

# =============================================================================
# 2. TRIGONOMETRIC FUNCTIONS
# =============================================================================
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
print("\nAngles (radians):", angles)

print("\nTrigonometric Functions:")
print("Sine:", np.sin(angles))
print("Cosine:", np.cos(angles))
print("Tangent:", np.tan(angles[:4]))  # Avoid pi/2 for tan

# Inverse trigonometric
print("\nInverse Trig:")
print("Arcsin of 0.5:", np.arcsin(0.5))
print("Arccos of 0.5:", np.arccos(0.5))
print("Arctan of 1:", np.arctan(1))

# Convert degrees to radians and vice versa
print("\nConversions:")
print("90 degrees to radians:", np.radians(90))
print("Pi/2 radians to degrees:", np.degrees(np.pi/2))

# =============================================================================
# 3. ROUNDING FUNCTIONS
# =============================================================================
arr = np.array([1.2, 2.5, 3.7, -1.4, -2.5, -3.6])
print("\nOriginal:", arr)

print("\nRounding Functions:")
print("Round:", np.round(arr))
print("Floor:", np.floor(arr))
print("Ceil:", np.ceil(arr))
print("Truncate:", np.trunc(arr))

# Round to specific decimals
decimals = np.array([3.14159, 2.71828])
print("\nRound to 2 decimals:", np.round(decimals, 2))

# =============================================================================
# 4. AGGREGATE FUNCTIONS
# =============================================================================
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(arr)

print("\nAggregate Functions:")
print("Sum (all):", np.sum(arr))
print("Sum (axis=0, columns):", np.sum(arr, axis=0))
print("Sum (axis=1, rows):", np.sum(arr, axis=1))

print("\nProduct (all):", np.prod(arr))
print("Product (columns):", np.prod(arr, axis=0))

print("\nCumulative sum (flattened):", np.cumsum(arr))
print("Cumulative sum (columns):")
print(np.cumsum(arr, axis=0))

print("\nCumulative product (rows):")
print(np.cumprod(arr, axis=1))

# =============================================================================
# 5. STATISTICAL FUNCTIONS
# =============================================================================
data = np.array([23, 45, 67, 89, 34, 56, 78, 90, 12, 45])
print("\nData:", data)

print("\nStatistical Functions:")
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))
print("Min:", np.min(data))
print("Max:", np.max(data))
print("Range:", np.ptp(data))  # Peak to peak (max - min)

# Percentiles
print("\nPercentiles:")
print("25th percentile:", np.percentile(data, 25))
print("50th percentile (median):", np.percentile(data, 50))
print("75th percentile:", np.percentile(data, 75))

# Quantiles
print("\nQuantiles:")
print("Quartiles:", np.quantile(data, [0.25, 0.5, 0.75]))

# =============================================================================
# 6. COMPARISON OPERATIONS
# =============================================================================
a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 3, 3, 2, 5])

print("\nArray a:", a)
print("Array b:", b)

print("\nComparisons:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a >= b:", a >= b)
print("a < b:", a < b)

# Comparison with scalar
print("\na > 3:", a > 3)

# all and any
print("\nAll a > 0:", np.all(a > 0))
print("Any a > 4:", np.any(a > 4))

# array_equal - check if two arrays are equal
print("Arrays equal:", np.array_equal(a, b))

# =============================================================================
# 7. LOGICAL OPERATIONS
# =============================================================================
a = np.array([True, True, False, False])
b = np.array([True, False, True, False])

print("\nLogical Operations:")
print("a:", a)
print("b:", b)
print("AND:", np.logical_and(a, b))
print("OR:", np.logical_or(a, b))
print("NOT a:", np.logical_not(a))
print("XOR:", np.logical_xor(a, b))

# With conditions
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
cond1 = arr > 3
cond2 = arr < 8
print("\nCombined conditions (3 < arr < 8):")
print(np.logical_and(cond1, cond2))

# =============================================================================
# 8. BASIC LINEAR ALGEBRA
# =============================================================================
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("\nMatrix A:")
print(A)
print("\nMatrix B:")
print(B)

# Matrix multiplication
print("\nMatrix Multiplication (A @ B):")
print(A @ B)  # Or np.matmul(A, B) or np.dot(A, B)

# Element-wise multiplication
print("\nElement-wise multiplication (A * B):")
print(A * B)

# Dot product of vectors
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print("\nDot product of vectors:", np.dot(v1, v2))

# Transpose
print("\nTranspose of A:")
print(A.T)

# Determinant
print("\nDeterminant of A:", np.linalg.det(A))

# Inverse
print("\nInverse of A:")
print(np.linalg.inv(A))

# Trace (sum of diagonal)
print("\nTrace of A:", np.trace(A))

# =============================================================================
# 9. WHERE FUNCTION
# =============================================================================
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("\nArray:", arr)

# np.where(condition, x, y) - if condition, return x, else return y
result = np.where(arr > 5, arr, 0)
print("Where arr > 5, keep value, else 0:", result)

result2 = np.where(arr % 2 == 0, 'even', 'odd')
print("Even or odd:", result2)

# Get indices where condition is true
indices = np.where(arr > 5)
print("Indices where arr > 5:", indices[0])

# =============================================================================
# 10. CLIP, MINIMUM, MAXIMUM
# =============================================================================
arr = np.array([1, 5, 10, 15, 20, 25])
print("\nArray:", arr)

# Clip values to range
clipped = np.clip(arr, 5, 15)
print("Clipped to [5, 15]:", clipped)

# Element-wise minimum/maximum
a = np.array([1, 5, 3, 8])
b = np.array([2, 4, 6, 7])
print("\nElement-wise minimum:", np.minimum(a, b))
print("Element-wise maximum:", np.maximum(a, b))

print("\n" + "="*50)
print("NUMPY PART 3 - MATH OPERATIONS COMPLETE!")
print("="*50)
