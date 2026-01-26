# =============================================================================
# MATPLOTLIB PART 5 - ADVANCED FEATURES (Advanced Level)
# =============================================================================
# 3D plots, animations, custom styles, and advanced customizations.

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# =============================================================================
# 1. 3D SURFACE PLOTS
# =============================================================================
print("--- 3D Surface Plots ---")

fig = plt.figure(figsize=(14, 5))

# Create meshgrid
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Basic surface plot
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.9)
ax1.set_title('Surface Plot')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# Wireframe plot
ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_wireframe(X, Y, Z, color='#3498db', linewidth=0.5)
ax2.set_title('Wireframe Plot')

# Contour on surface
ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(X, Y, Z, cmap='coolwarm', alpha=0.8)
ax3.contour(X, Y, Z, zdir='z', offset=-2, cmap='coolwarm')
ax3.set_zlim(-2, 1)
ax3.set_title('Surface with Contour')

plt.tight_layout()
plt.savefig('matplotlib_3d_surface.png', dpi=120)
plt.close()
print("Saved 3D surface plots")

# =============================================================================
# 2. 3D SCATTER AND LINE PLOTS
# =============================================================================
print("\n--- 3D Scatter and Line Plots ---")

fig = plt.figure(figsize=(14, 5))

# 3D Scatter
ax1 = fig.add_subplot(131, projection='3d')
np.random.seed(42)
n = 100
xs = np.random.randn(n)
ys = np.random.randn(n)
zs = np.random.randn(n)
colors = np.sqrt(xs**2 + ys**2 + zs**2)

scatter = ax1.scatter(xs, ys, zs, c=colors, cmap='plasma', s=50, alpha=0.8)
ax1.set_title('3D Scatter Plot')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# 3D Line (Parametric curve)
ax2 = fig.add_subplot(132, projection='3d')
t = np.linspace(0, 4*np.pi, 200)
x = np.sin(t)
y = np.cos(t)
z = t / (4*np.pi)
ax2.plot(x, y, z, 'b-', linewidth=2)
ax2.set_title('3D Parametric Curve')

# 3D Bar
ax3 = fig.add_subplot(133, projection='3d')
_x = np.arange(4)
_y = np.arange(3)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
z = np.zeros_like(x)
dx = dy = 0.5
dz = np.random.randint(1, 10, size=len(x))
colors = plt.cm.viridis(dz / max(dz))
ax3.bar3d(x, y, z, dx, dy, dz, color=colors, alpha=0.8)
ax3.set_title('3D Bar Plot')

plt.tight_layout()
plt.savefig('matplotlib_3d_scatter_line.png', dpi=120)
plt.close()
print("Saved 3D scatter and line plots")

# =============================================================================
# 3. CONTOUR PLOTS
# =============================================================================
print("\n--- Contour Plots ---")

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2 + Y**2)) + np.exp(-((X-1.5)**2 + (Y-1.5)**2))

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Basic contour
cs1 = axes[0, 0].contour(X, Y, Z, levels=10, cmap='viridis')
axes[0, 0].clabel(cs1, inline=True, fontsize=8)
axes[0, 0].set_title('Contour Plot')

# Filled contour
cs2 = axes[0, 1].contourf(X, Y, Z, levels=20, cmap='RdYlBu_r')
plt.colorbar(cs2, ax=axes[0, 1])
axes[0, 1].set_title('Filled Contour')

# Contour with colorbar
cs3 = axes[1, 0].contour(X, Y, Z, levels=15, cmap='plasma')
plt.colorbar(cs3, ax=axes[1, 0])
axes[1, 0].set_title('Contour with Colorbar')

# Combined contour and contourf
cs4 = axes[1, 1].contourf(X, Y, Z, levels=15, cmap='coolwarm', alpha=0.8)
axes[1, 1].contour(X, Y, Z, levels=15, colors='black', linewidths=0.5)
plt.colorbar(cs4, ax=axes[1, 1])
axes[1, 1].set_title('Combined Contour')

plt.tight_layout()
plt.savefig('matplotlib_contour.png', dpi=120)
plt.close()
print("Saved contour plots")

# =============================================================================
# 4. HEATMAPS AND IMSHOW
# =============================================================================
print("\n--- Heatmaps ---")

np.random.seed(42)
data = np.random.randn(10, 10)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Basic heatmap
im1 = axes[0].imshow(data, cmap='viridis')
plt.colorbar(im1, ax=axes[0])
axes[0].set_title('Basic Heatmap')

# Annotated heatmap
im2 = axes[1].imshow(data, cmap='RdBu', vmin=-2, vmax=2)
for i in range(10):
    for j in range(10):
        text = axes[1].text(j, i, f'{data[i, j]:.1f}', ha='center', va='center', 
                            color='black' if abs(data[i, j]) < 1 else 'white', fontsize=7)
plt.colorbar(im2, ax=axes[1])
axes[1].set_title('Annotated Heatmap')

# Correlation matrix style
corr = np.corrcoef(np.random.randn(5, 100))
im3 = axes[2].imshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar(im3, ax=axes[2])
axes[2].set_xticks(range(5))
axes[2].set_yticks(range(5))
axes[2].set_xticklabels(['A', 'B', 'C', 'D', 'E'])
axes[2].set_yticklabels(['A', 'B', 'C', 'D', 'E'])
axes[2].set_title('Correlation Matrix')

plt.tight_layout()
plt.savefig('matplotlib_heatmap.png', dpi=120)
plt.close()
print("Saved heatmap examples")

# =============================================================================
# 5. POLAR PLOTS
# =============================================================================
print("\n--- Polar Plots ---")

fig, axes = plt.subplots(1, 3, figsize=(15, 5), subplot_kw={'projection': 'polar'})

# Line plot in polar
theta1 = np.linspace(0, 2*np.pi, 100)
r1 = 1 + 0.5 * np.cos(5*theta1)
axes[0].plot(theta1, r1, 'b-', linewidth=2)
axes[0].set_title('Polar Line Plot')

# Scatter in polar
theta2 = np.random.uniform(0, 2*np.pi, 50)
r2 = np.random.uniform(0.5, 1.5, 50)
axes[1].scatter(theta2, r2, c=r2, cmap='viridis', s=50, alpha=0.8)
axes[1].set_title('Polar Scatter')

# Radar/spider chart
categories = ['Speed', 'Power', 'Defense', 'Magic', 'Skill', 'Luck']
N = len(categories)
values = [4, 3, 5, 2, 4, 3]
values += values[:1]  # Close the polygon
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

axes[2].plot(angles, values, 'o-', linewidth=2, color='#e74c3c')
axes[2].fill(angles, values, alpha=0.25, color='#e74c3c')
axes[2].set_xticks(angles[:-1])
axes[2].set_xticklabels(categories)
axes[2].set_title('Radar Chart')

plt.tight_layout()
plt.savefig('matplotlib_polar.png', dpi=120)
plt.close()
print("Saved polar plots")

# =============================================================================
# 6. BOX AND VIOLIN PLOTS
# =============================================================================
print("\n--- Box and Violin Plots ---")

np.random.seed(42)
data1 = np.random.normal(100, 10, 200)
data2 = np.random.normal(90, 20, 200)
data3 = np.random.normal(110, 15, 200)
all_data = [data1, data2, data3]

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Box plot
bp = axes[0].boxplot(all_data, labels=['A', 'B', 'C'], patch_artist=True)
colors = ['#3498db', '#2ecc71', '#e74c3c']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
axes[0].set_title('Box Plot')
axes[0].set_ylabel('Value')
axes[0].grid(True, alpha=0.3)

# Violin plot
vp = axes[1].violinplot(all_data, positions=[1, 2, 3], showmeans=True, showmedians=True)
for i, body in enumerate(vp['bodies']):
    body.set_facecolor(colors[i])
    body.set_alpha(0.7)
axes[1].set_xticks([1, 2, 3])
axes[1].set_xticklabels(['A', 'B', 'C'])
axes[1].set_title('Violin Plot')
axes[1].grid(True, alpha=0.3)

# Combined box + violin
parts = axes[2].violinplot(all_data, positions=[1, 2, 3], showextrema=False)
for i, body in enumerate(parts['bodies']):
    body.set_facecolor(colors[i])
    body.set_alpha(0.3)
bp2 = axes[2].boxplot(all_data, positions=[1, 2, 3], widths=0.15, patch_artist=True)
for patch, color in zip(bp2['boxes'], colors):
    patch.set_facecolor(color)
axes[2].set_xticks([1, 2, 3])
axes[2].set_xticklabels(['A', 'B', 'C'])
axes[2].set_title('Box + Violin')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('matplotlib_box_violin.png', dpi=120)
plt.close()
print("Saved box and violin plots")

# =============================================================================
# 7. CUSTOM STYLES AND RCPARAMS
# =============================================================================
print("\n--- Custom Styles ---")

"""
Available built-in styles:
    plt.style.available  # List all styles
    
    Popular styles:
    - 'seaborn'
    - 'ggplot'
    - 'fivethirtyeight'
    - 'dark_background'
    - 'grayscale'
"""

# Using a style context
styles = ['default', 'seaborn-v0_8', 'ggplot', 'dark_background']

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
x = np.linspace(0, 10, 100)

for ax, style in zip(axes.flat, styles):
    try:
        with plt.style.context(style):
            ax.plot(x, np.sin(x), linewidth=2, label='sin(x)')
            ax.plot(x, np.cos(x), linewidth=2, label='cos(x)')
            ax.set_title(f"Style: {style}")
            ax.legend()
            ax.grid(True, alpha=0.3)
    except:
        ax.plot(x, np.sin(x), linewidth=2, label='sin(x)')
        ax.set_title(f"Style: {style} (fallback)")
        ax.legend()

plt.tight_layout()
plt.savefig('matplotlib_styles.png', dpi=120)
plt.close()
print("Saved style examples")

# =============================================================================
# 8. CUSTOM COLORMAPS
# =============================================================================
print("\n--- Custom Colormaps ---")

from matplotlib.colors import LinearSegmentedColormap, ListedColormap

# Create custom colormap
colors = ['#2c3e50', '#3498db', '#2ecc71', '#f1c40f', '#e74c3c']
custom_cmap = LinearSegmentedColormap.from_list('custom', colors, N=256)

# Sample data
data = np.random.randn(20, 20)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

im1 = axes[0].imshow(data, cmap='viridis')
plt.colorbar(im1, ax=axes[0])
axes[0].set_title('Viridis (Default)')

im2 = axes[1].imshow(data, cmap=custom_cmap)
plt.colorbar(im2, ax=axes[1])
axes[1].set_title('Custom Colormap')

# Discrete colormap
discrete_colors = ['#3498db', '#2ecc71', '#f39c12', '#e74c3c', '#9b59b6']
discrete_cmap = ListedColormap(discrete_colors)
im3 = axes[2].imshow(np.random.randint(0, 5, (10, 10)), cmap=discrete_cmap)
cbar = plt.colorbar(im3, ax=axes[2], ticks=[0.5, 1.5, 2.5, 3.5, 4.5])
cbar.ax.set_yticklabels(['A', 'B', 'C', 'D', 'E'])
axes[2].set_title('Discrete Colormap')

plt.tight_layout()
plt.savefig('matplotlib_custom_cmap.png', dpi=120)
plt.close()
print("Saved custom colormap examples")

# =============================================================================
# 9. ANNOTATIONS AND ARROWS
# =============================================================================
print("\n--- Annotations and Arrows ---")

fig, ax = plt.subplots(figsize=(12, 8))

x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y, 'b-', linewidth=2)

# Different annotation styles
ax.annotate('Simple Arrow', xy=(np.pi/2, 1), xytext=(2, 0.5),
            arrowprops=dict(arrowstyle='->', color='red'),
            fontsize=11, color='red')

ax.annotate('Fancy Arrow', xy=(3*np.pi/2, -1), xytext=(6, -0.5),
            arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=0.3',
                           fc='green', ec='green'),
            fontsize=11, color='green')

ax.annotate('Curved', xy=(5*np.pi/2, 1), xytext=(9, 0.5),
            arrowprops=dict(arrowstyle='wedge', connectionstyle='angle,angleA=0,angleB=90',
                           fc='purple', ec='purple'),
            fontsize=11, color='purple')

# Text box
props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
ax.text(0.02, 0.98, 'Text Box\nwith multi-line', transform=ax.transAxes, 
        fontsize=12, verticalalignment='top', bbox=props)

ax.set_title('Annotations and Arrows', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 10)

plt.tight_layout()
plt.savefig('matplotlib_annotations.png', dpi=120)
plt.close()
print("Saved annotation examples")

# =============================================================================
# 10. ANIMATION BASICS (Save as GIF info)
# =============================================================================
print("\n--- Animation Info ---")

"""
Animation with Matplotlib:

from matplotlib.animation import FuncAnimation, PillowWriter

fig, ax = plt.subplots()
line, = ax.plot([], [], 'b-', linewidth=2)
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)

def init():
    line.set_data([], [])
    return line,

def animate(frame):
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x + frame/10)
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init, 
                     frames=100, interval=50, blit=True)

# Save as GIF
anim.save('animation.gif', writer=PillowWriter(fps=20))

# Save as MP4 (requires ffmpeg)
# anim.save('animation.mp4', writer='ffmpeg', fps=20)
"""

print("Animation example code provided in comments")

# =============================================================================
# SUMMARY
# =============================================================================
print("\n" + "=" * 60)
print("MATPLOTLIB PART 5 - ADVANCED FEATURES COMPLETE!")
print("=" * 60)
print("""
Topics Covered in This Series:

Part 1 - Basics:
    • Installation and imports
    • Figure and axes concepts
    • Basic plots, line styles, colors
    • Markers, titles, labels, legends
    • Grid, axis limits, saving figures

Part 2 - Line and Scatter Plots:
    • Advanced line plots
    • Fill between curves
    • Error bars and confidence intervals
    • Step plots
    • Scatter plots and bubble charts
    • Dual y-axis, stacked area, log scales

Part 3 - Bar, Histogram, Pie Charts:
    • Bar charts (basic, styled, grouped, stacked)
    • Histograms (basic, multiple, 2D)
    • Pie charts and donut charts

Part 4 - Subplots and Layouts:
    • Basic subplots
    • GridSpec and subplot2grid
    • Nested layouts
    • Colorbars and inset axes
    • Figure styling

Part 5 - Advanced Features:
    • 3D plots (surface, scatter, bar)
    • Contour plots
    • Heatmaps
    • Polar plots
    • Box and violin plots
    • Custom styles and colormaps
    • Annotations and animations
""")
print("All plots saved as PNG files in current directory.")
