# =============================================================================
# MATPLOTLIB PART 1 - BASICS (Beginner Level)
# =============================================================================
# Matplotlib is the foundational plotting library for Python.
# It provides complete control over every aspect of a figure.

import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# 1. GETTING STARTED
# =============================================================================
"""
Why Matplotlib?
    - Most widely used plotting library in Python
    - Complete control over every element
    - Foundation for other libraries (Seaborn, Pandas plotting)
    - Publication-quality figures
    - Works with NumPy arrays seamlessly

Installation:
    pip install matplotlib

Import Convention:
    import matplotlib.pyplot as plt
"""

# =============================================================================
# 2. YOUR FIRST PLOT
# =============================================================================
print("--- Your First Plot ---")

# Simple line plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title("My First Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.savefig('matplotlib_first_plot.png', dpi=100)
plt.close()
print("Saved first plot")

# =============================================================================
# 3. FIGURE AND AXES CONCEPT
# =============================================================================
print("\n--- Figure and Axes Concept ---")

"""
Key Concepts:
    Figure: The entire window/page containing everything
    Axes: The actual plot area (can have multiple per figure)
    Axis: The x and y number lines
    Artist: Everything visible on the figure (text, lines, markers, etc.)
"""

# Method 1: Pyplot interface (stateful)
plt.figure(figsize=(8, 5))
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Pyplot Interface")
plt.savefig('matplotlib_pyplot_interface.png', dpi=100)
plt.close()
print("Saved pyplot interface example")

# Method 2: Object-oriented interface (recommended)
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot([1, 2, 3], [1, 4, 9])
ax.set_title("Object-Oriented Interface")
ax.set_xlabel("X")
ax.set_ylabel("Y")
fig.savefig('matplotlib_oo_interface.png', dpi=100)
plt.close()
print("Saved OO interface example")

# =============================================================================
# 4. BASIC LINE PLOTS
# =============================================================================
print("\n--- Basic Line Plots ---")

# Create data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Basic line plot
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X")
plt.ylabel("sin(x)")
plt.grid(True)
plt.savefig('matplotlib_sine_wave.png', dpi=100)
plt.close()
print("Saved sine wave plot")

# Multiple lines
plt.figure(figsize=(10, 6))
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.title("Sine and Cosine")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.savefig('matplotlib_sin_cos.png', dpi=100)
plt.close()
print("Saved sin/cos plot")

# =============================================================================
# 5. LINE STYLES AND COLORS
# =============================================================================
print("\n--- Line Styles and Colors ---")

"""
Line Styles:
    '-'   solid line
    '--'  dashed line
    '-.'  dash-dot line
    ':'   dotted line

Colors (short codes):
    'b'  blue      'g'  green     'r'  red
    'c'  cyan      'm'  magenta   'y'  yellow
    'k'  black     'w'  white

Or use:
    - Color names: 'blue', 'green', 'red', etc.
    - Hex codes: '#FF5733'
    - RGB tuples: (0.1, 0.2, 0.5)
"""

x = np.linspace(0, 10, 50)

plt.figure(figsize=(12, 8))

# Different line styles
plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x), '-', label='solid')
plt.plot(x, np.cos(x), '--', label='dashed')
plt.plot(x, np.sin(x/2), '-.', label='dash-dot')
plt.plot(x, np.cos(x/2), ':', label='dotted')
plt.legend()
plt.title("Line Styles")

# Different colors
plt.subplot(2, 2, 2)
plt.plot(x, np.sin(x), 'r', label='red')
plt.plot(x, np.sin(x + 0.5), 'g', label='green')
plt.plot(x, np.sin(x + 1), 'b', label='blue')
plt.plot(x, np.sin(x + 1.5), 'm', label='magenta')
plt.legend()
plt.title("Colors")

# Line width
plt.subplot(2, 2, 3)
plt.plot(x, np.sin(x), linewidth=1, label='lw=1')
plt.plot(x, np.sin(x + 0.5), linewidth=2, label='lw=2')
plt.plot(x, np.sin(x + 1), linewidth=3, label='lw=3')
plt.legend()
plt.title("Line Width")

# Combined format strings
plt.subplot(2, 2, 4)
plt.plot(x, np.sin(x), 'r--', label='red dashed')
plt.plot(x, np.cos(x), 'b-.', label='blue dash-dot')
plt.plot(x, np.sin(x/2), 'g:', label='green dotted')
plt.legend()
plt.title("Format Strings")

plt.tight_layout()
plt.savefig('matplotlib_line_styles.png', dpi=100)
plt.close()
print("Saved line styles example")

# =============================================================================
# 6. MARKERS
# =============================================================================
print("\n--- Markers ---")

"""
Common Markers:
    'o'  circle        's'  square       '^'  triangle up
    'v'  triangle down 'd'  diamond      '*'  star
    '+'  plus          'x'  X            '.'  point
    'p'  pentagon      'h'  hexagon      '|'  vertical line
"""

x = np.linspace(0, 10, 15)

plt.figure(figsize=(12, 8))

# Different markers
plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x), 'o', label='circle')
plt.plot(x, np.cos(x), 's', label='square')
plt.legend()
plt.title("Basic Markers")

# Markers with lines
plt.subplot(2, 2, 2)
plt.plot(x, np.sin(x), '-o', label='line with circles')
plt.plot(x, np.cos(x), '--s', label='dashed with squares')
plt.legend()
plt.title("Lines with Markers")

# Marker customization
plt.subplot(2, 2, 3)
plt.plot(x, np.sin(x), marker='o', markersize=8, 
         markerfacecolor='red', markeredgecolor='black',
         markeredgewidth=2)
plt.title("Custom Markers")

# All marker options
plt.subplot(2, 2, 4)
markers = ['o', 's', '^', 'v', 'd', '*', 'p', 'h']
for i, marker in enumerate(markers):
    plt.plot(x, np.sin(x + i*0.3) + i*0.3, marker=marker, 
             label=f"marker='{marker}'", linestyle='--', alpha=0.7)
plt.legend(fontsize=8)
plt.title("Marker Gallery")

plt.tight_layout()
plt.savefig('matplotlib_markers.png', dpi=100)
plt.close()
print("Saved markers example")

# =============================================================================
# 7. TITLES, LABELS, AND TEXT
# =============================================================================
print("\n--- Titles, Labels, and Text ---")

x = np.linspace(0, 10, 100)

plt.figure(figsize=(10, 6))
plt.plot(x, np.sin(x))

# Title with formatting
plt.title("Sine Function: $y = \sin(x)$", fontsize=16, fontweight='bold', 
          color='navy', fontfamily='serif')

# Axis labels
plt.xlabel("Time (seconds)", fontsize=12, color='darkgreen')
plt.ylabel("Amplitude", fontsize=12, color='darkred')

# Add text annotation
plt.text(5, 0.5, "Peak region", fontsize=12, ha='center', 
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Add arrow annotation
plt.annotate("Maximum", xy=(np.pi/2, 1), xytext=(2, 0.7),
             arrowprops=dict(arrowstyle='->', color='black'),
             fontsize=11)

plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('matplotlib_text_labels.png', dpi=100)
plt.close()
print("Saved text and labels example")

# =============================================================================
# 8. LEGENDS
# =============================================================================
print("\n--- Legends ---")

x = np.linspace(0, 10, 100)

plt.figure(figsize=(10, 6))
plt.plot(x, np.sin(x), label='Sine')
plt.plot(x, np.cos(x), label='Cosine')
plt.plot(x, np.sin(x) * np.cos(x), label='Sin × Cos')

# Legend with customization
plt.legend(
    loc='upper right',      # Position
    fontsize=10,            # Font size
    framealpha=0.9,         # Frame transparency
    shadow=True,            # Shadow effect
    borderpad=1,            # Padding inside legend
    title='Functions',      # Legend title
    title_fontsize=12       # Title font size
)

"""
Location codes for legends:
    'best'         'upper right'   'upper left'
    'lower right'  'lower left'    'right'
    'center left'  'center right'  'lower center'
    'upper center' 'center'
    
Or use (x, y) tuple for exact position
"""

plt.title("Legend Customization")
plt.grid(True, alpha=0.3)
plt.savefig('matplotlib_legend.png', dpi=100)
plt.close()
print("Saved legend example")

# =============================================================================
# 9. GRID AND AXIS LIMITS
# =============================================================================
print("\n--- Grid and Axis Limits ---")

x = np.linspace(0, 10, 100)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Default grid
ax1 = axes[0, 0]
ax1.plot(x, np.sin(x))
ax1.grid(True)
ax1.set_title("Default Grid")

# Custom grid
ax2 = axes[0, 1]
ax2.plot(x, np.sin(x))
ax2.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.7)
ax2.set_title("Custom Grid Style")

# Major and minor grid
ax3 = axes[1, 0]
ax3.plot(x, np.sin(x))
ax3.grid(True, which='major', linestyle='-', linewidth=0.5)
ax3.grid(True, which='minor', linestyle=':', linewidth=0.3, alpha=0.5)
ax3.minorticks_on()
ax3.set_title("Major and Minor Grid")

# Axis limits and ticks
ax4 = axes[1, 1]
ax4.plot(x, np.sin(x))
ax4.set_xlim(0, 8)                              # X-axis limits
ax4.set_ylim(-1.5, 1.5)                         # Y-axis limits
ax4.set_xticks([0, 2, 4, 6, 8])                 # X-axis tick positions
ax4.set_xticklabels(['0', '2π/5', '4π/5', '6π/5', '8π/5'])  # Custom labels
ax4.set_title("Custom Axis Limits and Ticks")

plt.tight_layout()
plt.savefig('matplotlib_grid_axis.png', dpi=100)
plt.close()
print("Saved grid and axis example")

# =============================================================================
# 10. SAVING FIGURES
# =============================================================================
print("\n--- Saving Figures ---")

"""
Supported formats:
    PNG  - Best for web, supports transparency
    PDF  - Vector format, great for publications
    SVG  - Vector format, scalable
    JPG  - Compressed, smaller file size
    EPS  - Vector format for LaTeX

savefig() parameters:
    dpi         - Resolution (dots per inch)
    facecolor   - Background color
    edgecolor   - Border color
    transparent - Transparent background
    bbox_inches - 'tight' removes extra whitespace
    pad_inches  - Padding when using bbox_inches='tight'
"""

x = np.linspace(0, 10, 100)

plt.figure(figsize=(8, 6))
plt.plot(x, np.sin(x), 'b-', linewidth=2)
plt.title("Publication Quality Figure")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True, alpha=0.3)

# Save with different options
plt.savefig('matplotlib_high_dpi.png', dpi=300, bbox_inches='tight')
plt.savefig('matplotlib_transparent.png', transparent=True, bbox_inches='tight')
# plt.savefig('matplotlib_vector.pdf')  # Uncomment for PDF
# plt.savefig('matplotlib_vector.svg')  # Uncomment for SVG

plt.close()
print("Saved publication quality figures")

# =============================================================================
# 11. QUICK REFERENCE
# =============================================================================
"""
MATPLOTLIB QUICK REFERENCE:

Basic Workflow:
    import matplotlib.pyplot as plt
    import numpy as np
    
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'r-', label='sine')
    plt.title('My Plot')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.savefig('plot.png', dpi=300)
    plt.show()

Common Functions:
    plt.figure()    - Create new figure
    plt.plot()      - Line plot
    plt.title()     - Add title
    plt.xlabel()    - X-axis label
    plt.ylabel()    - Y-axis label
    plt.legend()    - Show legend
    plt.grid()      - Show grid
    plt.xlim()      - Set x-axis limits
    plt.ylim()      - Set y-axis limits
    plt.savefig()   - Save figure
    plt.show()      - Display figure
    plt.close()     - Close figure

Format String Pattern: '[color][marker][line]'
    Examples: 'ro-', 'b--', 'g^:', 'ks-.'
"""

print("\n" + "=" * 55)
print("MATPLOTLIB PART 1 - BASICS COMPLETE!")
print("=" * 55)
print("\nAll plots saved as PNG files in current directory.")
print("\nNext: Matplotlib_Part2_LinePlots.py - Detailed line visualizations")
