# =============================================================================
# NUMPY PART 5 - ADVANCED TOPICS (Expert Level)
# =============================================================================
# This part covers advanced linear algebra, FFT, random module, and performance.

import numpy as np
from numpy import linalg as LA

# =============================================================================
# 1. ADVANCED LINEAR ALGEBRA
# =============================================================================
print("="*60)
print("ADVANCED LINEAR ALGEBRA")
print("="*60)

A = np.array([[4, 2, 1], [2, 5, 3], [1, 3, 6]])
print("Matrix A:")
print(A)

# ----- Eigenvalues and Eigenvectors -----
eigenvalues, eigenvectors = LA.eig(A)
print("\nEigenvalues:", eigenvalues)
print("Eigenvectors:")
print(eigenvectors)

# ----- Singular Value Decomposition (SVD) -----
U, s, Vh = LA.svd(A)
print("\nSVD Decomposition:")
print("U (left singular vectors):")
print(U)
print("s (singular values):", s)
print("Vh (right singular vectors):")
print(Vh)

# ----- Matrix Rank -----
print("\nMatrix Rank:", LA.matrix_rank(A))

# ----- Norm -----
print("\nMatrix Norms:")
print("Frobenius norm:", LA.norm(A, 'fro'))
print("L2 norm (spectral):", LA.norm(A, 2))
print("L1 norm:", LA.norm(A, 1))
print("Infinity norm:", LA.norm(A, np.inf))

# ----- Solving Linear Systems -----
# Solve Ax = b
b = np.array([1, 2, 3])
x = LA.solve(A, b)
print("\nSolve Ax = b where b =", b)
print("Solution x:", x)
print("Verification A @ x:", A @ x)

# ----- Least Squares -----
# Solve overdetermined system
A_over = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
b_over = np.array([1, 2, 3, 4])
x_lstsq, residuals, rank, s = LA.lstsq(A_over, b_over, rcond=None)
print("\nLeast Squares Solution:", x_lstsq)

# ----- QR Decomposition -----
Q, R = LA.qr(A)
print("\nQR Decomposition:")
print("Q (orthogonal matrix):")
print(Q)
print("R (upper triangular):")
print(R)

# ----- Cholesky Decomposition -----
# For positive definite matrices
B = A @ A.T  # Create positive definite matrix
L = LA.cholesky(B)
print("\nCholesky Decomposition of B (A @ A.T):")
print(L)

# =============================================================================
# 2. RANDOM MODULE
# =============================================================================
print("\n" + "="*60)
print("NUMPY RANDOM")
print("="*60)

# Set seed for reproducibility
np.random.seed(42)

# ----- Basic Random Arrays -----
print("Random floats [0, 1):", np.random.rand(5))
print("Random integers [0, 10):", np.random.randint(0, 10, 5))
print("Random floats (standard normal):", np.random.randn(5))

# ----- Random Choice -----
arr = np.array(['apple', 'banana', 'cherry', 'date'])
print("\nRandom choice:", np.random.choice(arr))
print("3 random choices:", np.random.choice(arr, 3))
print("Without replacement:", np.random.choice(arr, 3, replace=False))

# Weighted random choice
weights = [0.1, 0.4, 0.3, 0.2]
print("Weighted choice:", np.random.choice(arr, 5, p=weights))

# ----- Shuffling -----
arr = np.arange(10)
np.random.shuffle(arr)
print("\nShuffled array:", arr)

# Permutation (returns shuffled copy)
arr = np.arange(10)
perm = np.random.permutation(arr)
print("Permutation:", perm)
print("Original unchanged:", arr)

# ----- Statistical Distributions -----
print("\n--- Statistical Distributions ---")
print("Uniform [5, 10):", np.random.uniform(5, 10, 5))
print("Normal (mean=0, std=1):", np.random.normal(0, 1, 5))
print("Binomial (n=10, p=0.5):", np.random.binomial(10, 0.5, 5))
print("Poisson (lambda=3):", np.random.poisson(3, 5))
print("Exponential (scale=2):", np.random.exponential(2, 5))

# ----- New Random Generator (Recommended) -----
rng = np.random.default_rng(seed=42)
print("\n--- New Generator API ---")
print("Random floats:", rng.random(5))
print("Random integers:", rng.integers(0, 10, 5))
print("Normal distribution:", rng.normal(0, 1, 5))

# =============================================================================
# 3. FOURIER TRANSFORMS
# =============================================================================
print("\n" + "="*60)
print("FOURIER TRANSFORMS")
print("="*60)

# Create sample signal (sum of two sine waves)
t = np.linspace(0, 1, 256)  # 1 second, 256 samples
freq1, freq2 = 5, 15  # 5 Hz and 15 Hz
signal = np.sin(2 * np.pi * freq1 * t) + 0.5 * np.sin(2 * np.pi * freq2 * t)

print("Signal shape:", signal.shape)

# FFT
fft_result = np.fft.fft(signal)
print("FFT result shape:", fft_result.shape)
print("FFT is complex:", fft_result.dtype)

# Get frequencies
frequencies = np.fft.fftfreq(len(signal), t[1] - t[0])
print("Sample frequencies:", frequencies[:10])

# Power spectrum (magnitude)
power = np.abs(fft_result) ** 2
print("Power spectrum shape:", power.shape)

# Inverse FFT
reconstructed = np.fft.ifft(fft_result)
print("Reconstructed signal close to original:", np.allclose(reconstructed.real, signal))

# 2D FFT (for images)
image = np.random.rand(64, 64)
fft_2d = np.fft.fft2(image)
fft_shifted = np.fft.fftshift(fft_2d)  # Shift zero frequency to center
print("\n2D FFT shape:", fft_2d.shape)

# =============================================================================
# 4. POLYNOMIAL OPERATIONS
# =============================================================================
print("\n" + "="*60)
print("POLYNOMIAL OPERATIONS")
print("="*60)

# Polynomial represented by coefficients [highest to lowest degree]
# p(x) = 2x^3 + 3x^2 - x + 5
p = np.array([2, 3, -1, 5])

# Evaluate polynomial
x = 2
result = np.polyval(p, x)
print(f"p(x) = 2x³ + 3x² - x + 5")
print(f"p({x}) = {result}")

# Roots of polynomial
roots = np.roots(p)
print("\nRoots of polynomial:", roots)

# Create polynomial from roots
roots_example = [1, -2, 3]
poly_from_roots = np.poly(roots_example)
print("\nPolynomial from roots [1, -2, 3]:", poly_from_roots)

# Polynomial fitting
x_data = np.array([0, 1, 2, 3, 4])
y_data = np.array([1, 2.1, 4.9, 9.1, 15.8])
coeffs = np.polyfit(x_data, y_data, 2)  # Fit quadratic
print("\nQuadratic fit coefficients:", coeffs)
print("Fitted values:", np.polyval(coeffs, x_data))

# Polynomial arithmetic
p1 = np.array([1, 2])      # x + 2
p2 = np.array([1, -1, 1])  # x² - x + 1

print("\nPolynomial multiplication:")
print("(x + 2) * (x² - x + 1) =", np.polymul(p1, p2))

print("\nPolynomial addition:")
print("(x + 2) + (x² - x + 1) =", np.polyadd(p1, p2))

# =============================================================================
# 5. SET OPERATIONS
# =============================================================================
print("\n" + "="*60)
print("SET OPERATIONS")
print("="*60)

a = np.array([1, 2, 3, 4, 5, 3, 2])
b = np.array([4, 5, 6, 7, 8])

print("Array a:", a)
print("Array b:", b)

# Unique elements
print("\nUnique in a:", np.unique(a))

# With counts
unique, counts = np.unique(a, return_counts=True)
print("Unique with counts:", dict(zip(unique, counts)))

# Set operations
print("\nUnion:", np.union1d(a, b))
print("Intersection:", np.intersect1d(a, b))
print("Difference (a - b):", np.setdiff1d(a, b))
print("Symmetric difference:", np.setxor1d(a, b))

# Element membership
print("\nIs b in a:", np.isin(b, a))

# =============================================================================
# 6. MEMORY AND PERFORMANCE
# =============================================================================
print("\n" + "="*60)
print("MEMORY AND PERFORMANCE")
print("="*60)

arr = np.arange(1000000)

# Memory information
print("Array size:", arr.size)
print("Item size:", arr.itemsize, "bytes")
print("Total bytes:", arr.nbytes)
print("Memory (MB):", arr.nbytes / (1024 * 1024))

# Contiguous memory
print("\nC-contiguous:", arr.flags['C_CONTIGUOUS'])
print("F-contiguous:", arr.flags['F_CONTIGUOUS'])

# Make Fortran-contiguous
arr_f = np.asfortranarray(arr.reshape(1000, 1000))
print("After asfortranarray F-contiguous:", arr_f.flags['F_CONTIGUOUS'])

# =============================================================================
# 7. EINSUM (Einstein Summation)
# =============================================================================
print("\n" + "="*60)
print("EINSUM - EINSTEIN SUMMATION")
print("="*60)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
v = np.array([1, 2])

print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
print("Vector v:", v)

# Trace
print("\nTrace of A (sum of diagonal):", np.einsum('ii', A))

# Diagonal
print("Diagonal of A:", np.einsum('ii->i', A))

# Sum all elements
print("Sum of A:", np.einsum('ij->', A))

# Sum along axis
print("Sum along rows:", np.einsum('ij->i', A))
print("Sum along columns:", np.einsum('ij->j', A))

# Matrix transpose
print("Transpose:", np.einsum('ij->ji', A))

# Matrix-vector multiplication
print("A @ v:", np.einsum('ij,j->i', A, v))

# Matrix multiplication
print("A @ B:")
print(np.einsum('ij,jk->ik', A, B))

# Element-wise multiplication then sum
print("Element-wise multiply and sum:", np.einsum('ij,ij->', A, B))

# Outer product
print("Outer product of v with itself:")
print(np.einsum('i,j->ij', v, v))

# =============================================================================
# 8. SAVING AND LOADING
# =============================================================================
print("\n" + "="*60)
print("SAVING AND LOADING")
print("="*60)

arr = np.arange(10)
arr2d = np.random.rand(3, 3)

# Save single array (.npy)
# np.save('array.npy', arr)
# loaded = np.load('array.npy')

# Save multiple arrays (.npz)
# np.savez('arrays.npz', arr=arr, arr2d=arr2d)
# data = np.load('arrays.npz')
# loaded_arr = data['arr']
# loaded_arr2d = data['arr2d']

# Save as text
# np.savetxt('array.txt', arr2d, delimiter=',')
# loaded_txt = np.loadtxt('array.txt', delimiter=',')

print("Save/Load examples (commented out to avoid creating files):")
print("- np.save('file.npy', arr) / np.load('file.npy')")
print("- np.savez('file.npz', arr1=a, arr2=b)")
print("- np.savetxt('file.txt', arr) / np.loadtxt('file.txt')")

# =============================================================================
# 9. VECTORIZATION AND UFUNC CREATION
# =============================================================================
print("\n" + "="*60)
print("CUSTOM UFUNCS WITH VECTORIZE")
print("="*60)

# Create vectorized function from Python function
def custom_function(x):
    if x < 0:
        return 0
    elif x < 5:
        return x ** 2
    else:
        return x * 10

vectorized_func = np.vectorize(custom_function)

arr = np.array([-2, 0, 3, 5, 10])
print("Input array:", arr)
print("Vectorized result:", vectorized_func(arr))

# Using frompyfunc (more flexible)
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

ufunc_c2f = np.frompyfunc(celsius_to_fahrenheit, 1, 1)
celsius = np.array([0, 20, 37, 100])
print("\nCelsius:", celsius)
print("Fahrenheit:", ufunc_c2f(celsius))

# =============================================================================
# 10. PERFORMANCE TIPS SUMMARY
# =============================================================================
print("\n" + "="*60)
print("PERFORMANCE TIPS")
print("="*60)

tips = """
1. USE VECTORIZED OPERATIONS
   - arr * 2 instead of [x * 2 for x in arr]
   - 100x+ faster!

2. AVOID PYTHON LOOPS
   - Use broadcasting, ufuncs, and array operations
   - Use np.where() instead of if/else loops

3. PRE-ALLOCATE ARRAYS
   - np.empty() then fill, instead of append
   - arr = np.empty(1000); arr[i] = value

4. USE APPROPRIATE DATA TYPES
   - np.float32 uses half memory of np.float64
   - np.int8 for small integers

5. USE CONTIGUOUS ARRAYS
   - C-order for row operations, F-order for column operations
   - np.ascontiguousarray()

6. LEVERAGE NUMBA OR CYTHON
   - For loops that can't be vectorized
   - @numba.jit decorator for JIT compilation

7. USE VIEWS INSTEAD OF COPIES
   - Slicing creates views (no memory copy)
   - Use reshape() not flatten() when possible

8. EINSUM FOR COMPLEX OPERATIONS
   - Often faster than multiple operations
   - More memory efficient

9. MEMORY-MAPPED FILES
   - np.memmap() for arrays larger than RAM

10. PARALLEL OPERATIONS
    - Use libraries like Dask for parallel computing
    - NumPy is already optimized with BLAS/LAPACK
"""
print(tips)

print("="*60)
print("NUMPY PART 5 - ADVANCED TOPICS COMPLETE!")
print("="*60)
print("\nCongratulations! You've completed all 5 parts of NumPy!")
