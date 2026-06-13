# =============================================================================
# MATPLOTLIB PART 2 - LINE AND SCATTER PLOTS (Intermediate Level)
# =============================================================================
# Detailed exploration of line plots, scatter plots, and their variations.

import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# 1. ADVANCED LINE PLOTS
# =============================================================================
print("--- Advanced Line Plots ---")

x = np.linspace(0, 4*np.pi, 200)

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(x, np.sin(x), color='#2ecc71', linewidth=2.5, label='sin(x)')
ax.plot(x, np.sin(x - np.pi/4), color='#e74c3c', linewidth=2, linestyle='--', label='sin(x - π/4)')
ax.plot(x, np.sin(x - np.pi/2), color='#3498db', linewidth=2, linestyle='-.', label='sin(x - π/2)')
ax.set_xlabel('X (radians)', fontsize=12)
ax.set_ylabel('Amplitude', fontsize=12)
ax.set_title('Phase-Shifted Sine Waves', fontsize=14, fontweight='bold')
ax.legend(loc='upper right')
ax.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('matplotlib_phase_shift.png', dpi=120)
plt.close()
print("Saved phase shift plot")

# =============================================================================
# 2. FILL BETWEEN LINES
# =============================================================================
print("\n--- Fill Between Lines ---")

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.sin(x) * 0.5

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Fill between curve and zero
axes[0, 0].plot(x, y1, 'b-', linewidth=2)
axes[0, 0].fill_between(x, y1, alpha=0.3, color='blue')
axes[0, 0].set_title('Fill Between Curve and Zero')
axes[0, 0].grid(True, alpha=0.3)

# Fill between two curves
axes[0, 1].plot(x, y1, 'r-', label='sin(x)', linewidth=2)
axes[0, 1].plot(x, y2, 'b-', label='sin(x)*0.5', linewidth=2)
axes[0, 1].fill_between(x, y1, y2, alpha=0.3, color='purple')
axes[0, 1].legend()
axes[0, 1].set_title('Fill Between Two Curves')

# Conditional fill
axes[1, 0].plot(x, y1, 'k-', linewidth=2)
axes[1, 0].fill_between(x, y1, where=(y1 > 0), alpha=0.5, color='green', label='Positive')
axes[1, 0].fill_between(x, y1, where=(y1 < 0), alpha=0.5, color='red', label='Negative')
axes[1, 0].legend()
axes[1, 0].set_title('Conditional Fill')

# Gradient effect
axes[1, 1].plot(x, y1, 'b-', linewidth=2)
for i in range(5):
    axes[1, 1].fill_between(x, y1*(1-i*0.2), y1*(1-(i+1)*0.2), alpha=0.3)
axes[1, 1].set_title('Gradient Fill Effect')

plt.tight_layout()
plt.savefig('matplotlib_fill_between.png', dpi=120)
plt.close()
print("Saved fill between examples")

# =============================================================================
# 3. ERROR BARS
# =============================================================================
print("\n--- Error Bars ---")

np.random.seed(42)
x = np.arange(1, 11)
y = np.random.randn(10).cumsum() + 10
y_err = np.random.rand(10) * 2

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].errorbar(x, y, yerr=y_err, fmt='o-', capsize=5, color='#3498db', ecolor='#2c3e50')
axes[0].set_title('Error Bars')
axes[0].grid(True, alpha=0.3)

axes[1].plot(x, y, 'b-', linewidth=2, label='Mean')
axes[1].fill_between(x, y-y_err, y+y_err, alpha=0.3, color='blue', label='±1σ')
axes[1].legend()
axes[1].set_title('Confidence Band')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('matplotlib_error_bars.png', dpi=120)
plt.close()
print("Saved error bar examples")

# =============================================================================
# 4. STEP PLOTS
# =============================================================================
print("\n--- Step Plots ---")

x = np.arange(10)
y = np.random.randint(1, 10, 10)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].step(x, y, where='pre', color='#2ecc71', linewidth=2)
axes[0, 0].plot(x, y, 'o', color='#27ae60', markersize=8)
axes[0, 0].set_title("Step: where='pre'")

axes[0, 1].step(x, y, where='post', color='#e74c3c', linewidth=2)
axes[0, 1].plot(x, y, 'o', color='#c0392b', markersize=8)
axes[0, 1].set_title("Step: where='post'")

axes[1, 0].step(x, y, where='mid', color='#3498db', linewidth=2)
axes[1, 0].plot(x, y, 'o', color='#2980b9', markersize=8)
axes[1, 0].set_title("Step: where='mid'")

axes[1, 1].step(x, y, where='pre', color='#9b59b6', linewidth=2)
axes[1, 1].fill_between(x, y, step='pre', alpha=0.3, color='#9b59b6')
axes[1, 1].set_title("Filled Step Plot")

plt.tight_layout()
plt.savefig('matplotlib_step_plots.png', dpi=120)
plt.close()
print("Saved step plot examples")

# =============================================================================
# 5. SCATTER PLOTS
# =============================================================================
print("\n--- Scatter Plots ---")

np.random.seed(42)
x = np.random.randn(100)
y = x * 2 + np.random.randn(100) * 0.5

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].scatter(x, y)
axes[0, 0].set_title('Basic Scatter')
axes[0, 0].grid(True, alpha=0.3)

scatter = axes[0, 1].scatter(x, y, c=y, cmap='viridis', alpha=0.7)
plt.colorbar(scatter, ax=axes[0, 1], label='Y Value')
axes[0, 1].set_title('Color Mapping')

sizes = np.abs(x) * 100 + 10
axes[1, 0].scatter(x, y, s=sizes, alpha=0.5, c='#e74c3c', edgecolors='white')
axes[1, 0].set_title('Variable Size')

scatter = axes[1, 1].scatter(x, y, c=x, s=np.abs(y)*50+10, cmap='RdYlBu', alpha=0.7)
plt.colorbar(scatter, ax=axes[1, 1])
axes[1, 1].set_title('Color and Size')

plt.tight_layout()
plt.savefig('matplotlib_scatter.png', dpi=120)
plt.close()
print("Saved scatter examples")

# =============================================================================
# 6. BUBBLE CHART
# =============================================================================
print("\n--- Bubble Chart ---")

countries = ['USA', 'China', 'Japan', 'Germany', 'UK']
gdp = np.array([21.43, 14.34, 5.08, 3.86, 2.83])
life_exp = np.array([78.9, 76.9, 84.4, 81.3, 81.2])
population = np.array([331, 1402, 126, 83, 67])

fig, ax = plt.subplots(figsize=(10, 7))
scatter = ax.scatter(gdp, life_exp, s=population*2, c=life_exp, cmap='RdYlGn', alpha=0.7, edgecolors='black')

for i, country in enumerate(countries):
    ax.annotate(country, (gdp[i], life_exp[i]), xytext=(5, 5), textcoords='offset points', fontweight='bold')

plt.colorbar(scatter, label='Life Expectancy')
ax.set_xlabel('GDP (Trillion USD)')
ax.set_ylabel('Life Expectancy (years)')
ax.set_title('GDP vs Life Expectancy (Bubble Size = Population)')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('matplotlib_bubble.png', dpi=120)
plt.close()
print("Saved bubble chart")

# =============================================================================
# 7. DUAL Y-AXIS
# =============================================================================
print("\n--- Dual Y-Axis ---")

x = np.linspace(0, 10, 100)
y1 = np.sin(x) * 100
y2 = np.exp(x/3)

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_xlabel('X')
ax1.set_ylabel('Sine Values', color='#3498db')
line1, = ax1.plot(x, y1, color='#3498db', linewidth=2, label='sin(x) × 100')
ax1.tick_params(axis='y', labelcolor='#3498db')

ax2 = ax1.twinx()
ax2.set_ylabel('Exponential Values', color='#e74c3c')
line2, = ax2.plot(x, y2, color='#e74c3c', linewidth=2, linestyle='--', label='exp(x/3)')
ax2.tick_params(axis='y', labelcolor='#e74c3c')

ax1.legend([line1, line2], ['sin(x) × 100', 'exp(x/3)'], loc='upper left')
ax1.set_title('Dual Y-Axis Plot')
ax1.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('matplotlib_dual_axis.png', dpi=120)
plt.close()
print("Saved dual axis plot")

# =============================================================================
# 8. STACKED AREA CHART
# =============================================================================
print("\n--- Stacked Area Chart ---")

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
product_a = np.array([10, 12, 15, 18, 20, 25])
product_b = np.array([8, 10, 12, 15, 18, 20])
product_c = np.array([5, 6, 8, 10, 12, 15])

fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(range(6), product_a, product_b, product_c,
             labels=['Product A', 'Product B', 'Product C'],
             colors=['#3498db', '#2ecc71', '#e74c3c'], alpha=0.8)
ax.set_xticks(range(6))
ax.set_xticklabels(months)
ax.set_xlabel('Month')
ax.set_ylabel('Sales')
ax.set_title('Stacked Area Chart')
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('matplotlib_stacked_area.png', dpi=120)
plt.close()
print("Saved stacked area chart")

# =============================================================================
# 9. LOGARITHMIC SCALES
# =============================================================================
print("\n--- Logarithmic Scales ---")

x = np.linspace(0.1, 100, 500)
y = x ** 2

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].plot(x, y, 'b-', linewidth=2)
axes[0, 0].set_title('Linear Scale')
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].plot(x, y, 'r-', linewidth=2)
axes[0, 1].set_xscale('log')
axes[0, 1].set_title('Log X-Axis')
axes[0, 1].grid(True, alpha=0.3, which='both')

axes[1, 0].plot(x, y, 'g-', linewidth=2)
axes[1, 0].set_yscale('log')
axes[1, 0].set_title('Log Y-Axis')
axes[1, 0].grid(True, alpha=0.3, which='both')

axes[1, 1].plot(x, y, 'm-', linewidth=2)
axes[1, 1].set_xscale('log')
axes[1, 1].set_yscale('log')
axes[1, 1].set_title('Log-Log Scale')
axes[1, 1].grid(True, alpha=0.3, which='both')

plt.tight_layout()
plt.savefig('matplotlib_log_scales.png', dpi=120)
plt.close()
print("Saved log scale examples")

print("\n" + "=" * 55)
print("MATPLOTLIB PART 2 - LINE AND SCATTER PLOTS COMPLETE!")
print("=" * 55)
print("\nNext: Matplotlib_Part3_BarCharts.py")
