# =============================================================================
# MATPLOTLIB PART 4 - SUBPLOTS AND LAYOUTS (Intermediate Level)
# =============================================================================
# Master creating complex figure layouts with multiple plots.

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

# =============================================================================
# 1. BASIC SUBPLOTS
# =============================================================================
print("--- Basic Subplots ---")

x = np.linspace(0, 10, 100)

# Using plt.subplots()
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].plot(x, np.sin(x), 'b-', linewidth=2)
axes[0, 0].set_title('Sine Wave')
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].plot(x, np.cos(x), 'r-', linewidth=2)
axes[0, 1].set_title('Cosine Wave')
axes[0, 1].grid(True, alpha=0.3)

axes[1, 0].plot(x, np.tan(x), 'g-', linewidth=2)
axes[1, 0].set_ylim(-5, 5)
axes[1, 0].set_title('Tangent Wave')
axes[1, 0].grid(True, alpha=0.3)

axes[1, 1].plot(x, np.exp(-x/5) * np.sin(x), 'm-', linewidth=2)
axes[1, 1].set_title('Damped Sine')
axes[1, 1].grid(True, alpha=0.3)

plt.suptitle('2x2 Subplot Grid', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('matplotlib_subplots_basic.png', dpi=120)
plt.close()
print("Saved basic subplots")

# =============================================================================
# 2. SHARING AXES
# =============================================================================
print("\n--- Sharing Axes ---")

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(2*x)

fig, axes = plt.subplots(3, 1, figsize=(12, 8), sharex=True)

axes[0].plot(x, y1, 'b-', linewidth=2)
axes[0].set_ylabel('sin(x)')
axes[0].grid(True, alpha=0.3)

axes[1].plot(x, y2, 'r-', linewidth=2)
axes[1].set_ylabel('cos(x)')
axes[1].grid(True, alpha=0.3)

axes[2].plot(x, y3, 'g-', linewidth=2)
axes[2].set_ylabel('sin(2x)')
axes[2].set_xlabel('X')
axes[2].grid(True, alpha=0.3)

plt.suptitle('Subplots with Shared X-Axis', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('matplotlib_subplots_shared.png', dpi=120)
plt.close()
print("Saved shared axis subplots")

# =============================================================================
# 3. DIFFERENT SUBPLOT SIZES WITH GRIDSPEC
# =============================================================================
print("\n--- GridSpec Layouts ---")

fig = plt.figure(figsize=(14, 10))
gs = gridspec.GridSpec(3, 3, figure=fig)

# Large plot spanning 2 rows, 2 columns
ax1 = fig.add_subplot(gs[0:2, 0:2])
x = np.linspace(0, 10, 100)
ax1.plot(x, np.sin(x) * np.exp(-x/10), 'b-', linewidth=2)
ax1.set_title('Main Plot (2x2)', fontsize=12, fontweight='bold')
ax1.grid(True, alpha=0.3)

# Small plots on the right
ax2 = fig.add_subplot(gs[0, 2])
ax2.bar(['A', 'B', 'C'], [3, 7, 5], color='#2ecc71')
ax2.set_title('Bar Chart')

ax3 = fig.add_subplot(gs[1, 2])
ax3.pie([30, 40, 30], labels=['X', 'Y', 'Z'], autopct='%1.0f%%')
ax3.set_title('Pie Chart')

# Bottom row plots
ax4 = fig.add_subplot(gs[2, 0])
ax4.scatter(np.random.randn(50), np.random.randn(50), c='#e74c3c', alpha=0.7)
ax4.set_title('Scatter')

ax5 = fig.add_subplot(gs[2, 1])
ax5.hist(np.random.randn(500), bins=20, color='#3498db', edgecolor='black')
ax5.set_title('Histogram')

ax6 = fig.add_subplot(gs[2, 2])
ax6.plot(np.random.randn(20).cumsum(), 'o-', color='#9b59b6')
ax6.set_title('Line')

plt.suptitle('Complex GridSpec Layout', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('matplotlib_gridspec.png', dpi=120)
plt.close()
print("Saved GridSpec layout")

# =============================================================================
# 4. SUBPLOT2GRID
# =============================================================================
print("\n--- Subplot2Grid ---")

fig = plt.figure(figsize=(12, 8))

# Create different sized subplots
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2, rowspan=2)
ax2 = plt.subplot2grid((3, 3), (0, 2), rowspan=2)
ax3 = plt.subplot2grid((3, 3), (2, 0))
ax4 = plt.subplot2grid((3, 3), (2, 1))
ax5 = plt.subplot2grid((3, 3), (2, 2))

# Add content
x = np.linspace(0, 10, 100)
ax1.plot(x, np.sin(x), 'b-', linewidth=2)
ax1.set_title('Main Plot')
ax1.grid(True, alpha=0.3)

ax2.barh(['A', 'B', 'C', 'D'], [4, 7, 2, 9], color='#2ecc71')
ax2.set_title('Horizontal Bar')

ax3.scatter(np.random.rand(30), np.random.rand(30), c='#e74c3c')
ax3.set_title('Scatter')

ax4.plot(np.random.randn(10), 'o-', color='#f39c12')
ax4.set_title('Line')

ax5.pie([25, 35, 40], labels=['X', 'Y', 'Z'])
ax5.set_title('Pie')

plt.tight_layout()
plt.savefig('matplotlib_subplot2grid.png', dpi=120)
plt.close()
print("Saved subplot2grid layout")

# =============================================================================
# 5. NESTED SUBPLOTS
# =============================================================================
print("\n--- Nested Subplots ---")

fig = plt.figure(figsize=(14, 10))
outer = gridspec.GridSpec(2, 2, figure=fig, wspace=0.3, hspace=0.3)

# Top-left: Single plot
ax1 = fig.add_subplot(outer[0, 0])
x = np.linspace(0, 10, 100)
ax1.plot(x, np.sin(x), 'b-', linewidth=2)
ax1.set_title('Single Plot')
ax1.grid(True, alpha=0.3)

# Top-right: 2x2 nested grid
inner1 = gridspec.GridSpecFromSubplotSpec(2, 2, subplot_spec=outer[0, 1], wspace=0.2, hspace=0.2)
for i in range(4):
    ax = fig.add_subplot(inner1[i // 2, i % 2])
    ax.plot(np.random.randn(20), color=f'C{i}')
    ax.set_title(f'Nested {i+1}', fontsize=9)

# Bottom-left: 1x3 nested grid
inner2 = gridspec.GridSpecFromSubplotSpec(1, 3, subplot_spec=outer[1, 0], wspace=0.2)
colors = ['#e74c3c', '#2ecc71', '#3498db']
for i in range(3):
    ax = fig.add_subplot(inner2[0, i])
    ax.bar(['A', 'B'], [np.random.randint(3, 10), np.random.randint(3, 10)], color=colors[i])
    ax.set_title(f'Bar {i+1}', fontsize=9)

# Bottom-right: 3x1 nested grid
inner3 = gridspec.GridSpecFromSubplotSpec(3, 1, subplot_spec=outer[1, 1], hspace=0.3)
for i in range(3):
    ax = fig.add_subplot(inner3[i, 0])
    ax.plot(np.cumsum(np.random.randn(30)), color=f'C{i+4}')
    ax.set_title(f'Series {i+1}', fontsize=9)

plt.suptitle('Nested Subplot Layouts', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('matplotlib_nested.png', dpi=120)
plt.close()
print("Saved nested subplots")

# =============================================================================
# 6. ADDING AND CUSTOMIZING COLORBARS
# =============================================================================
print("\n--- Colorbars ---")

np.random.seed(42)
data = np.random.randn(20, 20)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Default vertical colorbar
im1 = axes[0].imshow(data, cmap='viridis')
plt.colorbar(im1, ax=axes[0])
axes[0].set_title('Default Colorbar')

# Horizontal colorbar
im2 = axes[1].imshow(data, cmap='plasma')
cbar2 = plt.colorbar(im2, ax=axes[1], orientation='horizontal', pad=0.15)
cbar2.set_label('Value')
axes[1].set_title('Horizontal Colorbar')

# Customized colorbar
im3 = axes[2].imshow(data, cmap='coolwarm', vmin=-2, vmax=2)
cbar3 = plt.colorbar(im3, ax=axes[2], extend='both', shrink=0.8)
cbar3.set_label('Temperature (°C)', fontsize=10)
cbar3.ax.tick_params(labelsize=9)
axes[2].set_title('Customized Colorbar')

plt.tight_layout()
plt.savefig('matplotlib_colorbars.png', dpi=120)
plt.close()
print("Saved colorbar examples")

# =============================================================================
# 7. INSET AXES
# =============================================================================
print("\n--- Inset Axes ---")

from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

fig, ax = plt.subplots(figsize=(10, 8))

x = np.linspace(0, 10, 1000)
y = np.sin(x) * np.exp(-x/10)

ax.plot(x, y, 'b-', linewidth=2)
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_title('Main Plot with Inset', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)

# Create inset axes
axins = inset_axes(ax, width="40%", height="40%", loc='upper right')
axins.plot(x, y, 'b-', linewidth=1.5)
axins.set_xlim(0, 2)
axins.set_ylim(0.5, 1.0)
axins.set_title('Zoomed View', fontsize=10)
axins.grid(True, alpha=0.3)

# Mark the zoomed region
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

plt.tight_layout()
plt.savefig('matplotlib_inset.png', dpi=120)
plt.close()
print("Saved inset axes example")

# =============================================================================
# 8. FIGURE SIZE AND DPI
# =============================================================================
print("\n--- Figure Size and DPI ---")

"""
Figure Size and DPI:
    figsize = (width, height) in inches
    dpi = dots per inch
    
    Pixel dimensions = figsize × dpi
    Example: figsize=(10, 6), dpi=100 → 1000 × 600 pixels
    
Common settings:
    Web/screen: dpi=100
    Print quality: dpi=300
    High-res print: dpi=600
"""

# Create same plot at different sizes
sizes = [(6, 4), (10, 6), (12, 8)]

for i, size in enumerate(sizes):
    fig, ax = plt.subplots(figsize=size)
    x = np.linspace(0, 10, 100)
    ax.plot(x, np.sin(x), 'b-', linewidth=2)
    ax.set_title(f'Figure Size: {size[0]} × {size[1]} inches')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'matplotlib_size_{size[0]}x{size[1]}.png', dpi=100)
    plt.close()

print("Saved different figure sizes")

# =============================================================================
# 9. FIGURE BACKGROUNDS AND BORDERS
# =============================================================================
print("\n--- Figure Styling ---")

x = np.linspace(0, 10, 100)

fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f0f0f0')
ax.set_facecolor('#ffffff')

ax.plot(x, np.sin(x), color='#3498db', linewidth=2.5)
ax.set_title('Styled Figure', fontsize=14, fontweight='bold', color='#2c3e50')
ax.set_xlabel('X', fontsize=12, color='#34495e')
ax.set_ylabel('sin(x)', fontsize=12, color='#34495e')
ax.grid(True, linestyle='--', alpha=0.5, color='#bdc3c7')

# Customize spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#7f8c8d')
ax.spines['bottom'].set_color('#7f8c8d')
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

ax.tick_params(colors='#34495e', labelsize=10)

plt.tight_layout()
plt.savefig('matplotlib_styled_figure.png', dpi=120, facecolor=fig.get_facecolor())
plt.close()
print("Saved styled figure")

# =============================================================================
# 10. CONSTRAINED LAYOUT
# =============================================================================
print("\n--- Constrained Layout ---")

# Constrained layout automatically adjusts subplots
fig, axes = plt.subplots(2, 3, figsize=(14, 8), layout='constrained')

x = np.linspace(0, 10, 100)
for i, ax in enumerate(axes.flat):
    ax.plot(x, np.sin(x + i), linewidth=2)
    ax.set_title(f'Plot {i+1} with long title', fontsize=11)
    ax.set_xlabel('X axis label')
    ax.set_ylabel('Y axis label')
    ax.grid(True, alpha=0.3)

fig.suptitle('Constrained Layout (Automatic Spacing)', fontsize=16, fontweight='bold')
plt.savefig('matplotlib_constrained.png', dpi=120)
plt.close()
print("Saved constrained layout example")

print("\n" + "=" * 55)
print("MATPLOTLIB PART 4 - SUBPLOTS AND LAYOUTS COMPLETE!")
print("=" * 55)
print("\nNext: Matplotlib_Part5_Advanced.py")
