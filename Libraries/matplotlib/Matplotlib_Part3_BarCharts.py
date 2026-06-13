# =============================================================================
# MATPLOTLIB PART 3 - BAR, HISTOGRAM, AND PIE CHARTS (Intermediate Level)
# =============================================================================
# Comprehensive guide to categorical and distribution visualizations.

import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# 1. BASIC BAR CHARTS
# =============================================================================
print("--- Basic Bar Charts ---")

categories = ['Python', 'JavaScript', 'Java', 'C++', 'C#']
values = [35, 28, 20, 12, 8]

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Vertical bar chart
axes[0].bar(categories, values, color='#3498db', edgecolor='black', linewidth=1.2)
axes[0].set_xlabel('Programming Language')
axes[0].set_ylabel('Usage (%)')
axes[0].set_title('Vertical Bar Chart')
axes[0].grid(axis='y', alpha=0.3)

# Horizontal bar chart
axes[1].barh(categories, values, color='#2ecc71', edgecolor='black', linewidth=1.2)
axes[1].set_xlabel('Usage (%)')
axes[1].set_ylabel('Programming Language')
axes[1].set_title('Horizontal Bar Chart')
axes[1].grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.savefig('matplotlib_bar_basic.png', dpi=120)
plt.close()
print("Saved basic bar charts")

# =============================================================================
# 2. STYLED BAR CHARTS
# =============================================================================
print("\n--- Styled Bar Charts ---")

categories = ['Q1', 'Q2', 'Q3', 'Q4']
values = [120, 150, 180, 200]
colors = ['#e74c3c', '#f39c12', '#2ecc71', '#3498db']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(categories, values, color=colors, edgecolor='black', linewidth=1.5, width=0.6)

# Add value labels on bars
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
            f'${val}K', ha='center', va='bottom', fontweight='bold', fontsize=11)

ax.set_xlabel('Quarter', fontsize=12)
ax.set_ylabel('Revenue ($K)', fontsize=12)
ax.set_title('Quarterly Revenue 2024', fontsize=14, fontweight='bold')
ax.set_ylim(0, 230)
ax.grid(axis='y', linestyle='--', alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('matplotlib_bar_styled.png', dpi=120)
plt.close()
print("Saved styled bar chart")

# =============================================================================
# 3. GROUPED BAR CHARTS
# =============================================================================
print("\n--- Grouped Bar Charts ---")

categories = ['2021', '2022', '2023', '2024']
product_a = [25, 32, 40, 48]
product_b = [20, 28, 35, 42]
product_c = [15, 22, 28, 35]

x = np.arange(len(categories))
width = 0.25

fig, ax = plt.subplots(figsize=(12, 6))
bars1 = ax.bar(x - width, product_a, width, label='Product A', color='#3498db', edgecolor='black')
bars2 = ax.bar(x, product_b, width, label='Product B', color='#2ecc71', edgecolor='black')
bars3 = ax.bar(x + width, product_c, width, label='Product C', color='#e74c3c', edgecolor='black')

ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Sales (units)', fontsize=12)
ax.set_title('Grouped Bar Chart - Product Sales', fontsize=14, fontweight='bold')
ax.legend(loc='upper left')
ax.grid(axis='y', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('matplotlib_bar_grouped.png', dpi=120)
plt.close()
print("Saved grouped bar chart")

# =============================================================================
# 4. STACKED BAR CHARTS
# =============================================================================
print("\n--- Stacked Bar Charts ---")

categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
online = [30, 35, 40, 45, 50]
retail = [25, 28, 32, 35, 38]
wholesale = [15, 18, 20, 22, 25]

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(categories, online, label='Online', color='#3498db', edgecolor='black')
ax.bar(categories, retail, bottom=online, label='Retail', color='#2ecc71', edgecolor='black')
ax.bar(categories, wholesale, bottom=np.array(online)+np.array(retail), 
       label='Wholesale', color='#e74c3c', edgecolor='black')

ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Sales ($K)', fontsize=12)
ax.set_title('Stacked Bar Chart - Sales by Channel', fontsize=14, fontweight='bold')
ax.legend(loc='upper left')
ax.grid(axis='y', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('matplotlib_bar_stacked.png', dpi=120)
plt.close()
print("Saved stacked bar chart")

# =============================================================================
# 5. BASIC HISTOGRAMS
# =============================================================================
print("\n--- Basic Histograms ---")

np.random.seed(42)
data = np.random.randn(1000)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Basic histogram
axes[0, 0].hist(data, bins=30, color='#3498db', edgecolor='black', alpha=0.7)
axes[0, 0].set_title('Basic Histogram (30 bins)')
axes[0, 0].set_xlabel('Value')
axes[0, 0].set_ylabel('Frequency')

# Different bin counts
axes[0, 1].hist(data, bins=10, color='#2ecc71', edgecolor='black', alpha=0.7, label='10 bins')
axes[0, 1].hist(data, bins=50, color='#e74c3c', edgecolor='black', alpha=0.5, label='50 bins')
axes[0, 1].set_title('Comparing Bin Counts')
axes[0, 1].legend()

# Normalized histogram (density)
axes[1, 0].hist(data, bins=30, density=True, color='#9b59b6', edgecolor='black', alpha=0.7)
axes[1, 0].set_title('Normalized Histogram (Density)')
axes[1, 0].set_ylabel('Density')

# Cumulative histogram
axes[1, 1].hist(data, bins=30, cumulative=True, color='#f39c12', edgecolor='black', alpha=0.7)
axes[1, 1].set_title('Cumulative Histogram')
axes[1, 1].set_ylabel('Cumulative Frequency')

plt.tight_layout()
plt.savefig('matplotlib_histogram_basic.png', dpi=120)
plt.close()
print("Saved histogram examples")

# =============================================================================
# 6. MULTIPLE HISTOGRAMS
# =============================================================================
print("\n--- Multiple Histograms ---")

np.random.seed(42)
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(2, 1.5, 1000)
data3 = np.random.normal(-1, 0.8, 1000)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Overlapping histograms
axes[0].hist(data1, bins=30, alpha=0.5, label='Group A', color='#3498db')
axes[0].hist(data2, bins=30, alpha=0.5, label='Group B', color='#e74c3c')
axes[0].hist(data3, bins=30, alpha=0.5, label='Group C', color='#2ecc71')
axes[0].set_title('Overlapping Histograms')
axes[0].legend()

# Step histogram (for clear comparison)
axes[1].hist(data1, bins=30, histtype='step', linewidth=2, label='Group A')
axes[1].hist(data2, bins=30, histtype='step', linewidth=2, label='Group B')
axes[1].hist(data3, bins=30, histtype='step', linewidth=2, label='Group C')
axes[1].set_title('Step Histograms')
axes[1].legend()

plt.tight_layout()
plt.savefig('matplotlib_histogram_multiple.png', dpi=120)
plt.close()
print("Saved multiple histogram examples")

# =============================================================================
# 7. BASIC PIE CHARTS
# =============================================================================
print("\n--- Basic Pie Charts ---")

labels = ['Python', 'JavaScript', 'Java', 'C++', 'Other']
sizes = [35, 25, 20, 12, 8]
colors = ['#3498db', '#f39c12', '#e74c3c', '#2ecc71', '#9b59b6']

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Basic pie chart
axes[0].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
axes[0].set_title('Basic Pie Chart')

# Exploded pie chart
explode = (0.1, 0, 0, 0, 0)  # Explode first slice
axes[1].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', 
            explode=explode, shadow=True, startangle=90)
axes[1].set_title('Exploded Pie Chart')

plt.tight_layout()
plt.savefig('matplotlib_pie_basic.png', dpi=120)
plt.close()
print("Saved basic pie charts")

# =============================================================================
# 8. STYLED PIE CHARTS
# =============================================================================
print("\n--- Styled Pie Charts ---")

labels = ['Mobile', 'Desktop', 'Tablet', 'Smart TV']
sizes = [45, 35, 15, 5]
colors = ['#3498db', '#2ecc71', '#f39c12', '#e74c3c']
explode = (0.05, 0.05, 0.05, 0.05)

fig, ax = plt.subplots(figsize=(10, 8))

wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, colors=colors, autopct='%1.1f%%',
    explode=explode, shadow=True, startangle=45,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1.5},
    textprops={'fontsize': 11, 'fontweight': 'bold'}
)

# Style the percentage text
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(12)
    autotext.set_fontweight('bold')

ax.set_title('Device Usage Distribution', fontsize=16, fontweight='bold', pad=20)
ax.legend(wedges, labels, title="Devices", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.savefig('matplotlib_pie_styled.png', dpi=120)
plt.close()
print("Saved styled pie chart")

# =============================================================================
# 9. DONUT CHARTS
# =============================================================================
print("\n--- Donut Charts ---")

labels = ['Rent', 'Food', 'Transport', 'Entertainment', 'Savings']
sizes = [30, 25, 15, 10, 20]
colors = ['#e74c3c', '#f39c12', '#3498db', '#9b59b6', '#2ecc71']

fig, ax = plt.subplots(figsize=(10, 8))

wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, colors=colors, autopct='%1.1f%%',
    startangle=90, pctdistance=0.75,
    wedgeprops={'width': 0.5, 'edgecolor': 'white', 'linewidth': 2}
)

# Add center circle with text
centre_circle = plt.Circle((0, 0), 0.35, fc='white')
ax.add_artist(centre_circle)
ax.text(0, 0, 'Monthly\nBudget', ha='center', va='center', fontsize=14, fontweight='bold')

ax.set_title('Monthly Expense Breakdown', fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('matplotlib_donut.png', dpi=120)
plt.close()
print("Saved donut chart")

# =============================================================================
# 10. 2D HISTOGRAM (HEATMAP-LIKE)
# =============================================================================
print("\n--- 2D Histogram ---")

np.random.seed(42)
x = np.random.randn(10000)
y = x * 0.5 + np.random.randn(10000) * 0.5

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Basic 2D histogram
h1 = axes[0].hist2d(x, y, bins=30, cmap='Blues')
plt.colorbar(h1[3], ax=axes[0], label='Count')
axes[0].set_title('2D Histogram')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')

# Hexbin plot (alternative)
hb = axes[1].hexbin(x, y, gridsize=30, cmap='Greens')
plt.colorbar(hb, ax=axes[1], label='Count')
axes[1].set_title('Hexbin Plot')
axes[1].set_xlabel('X')
axes[1].set_ylabel('Y')

plt.tight_layout()
plt.savefig('matplotlib_2d_histogram.png', dpi=120)
plt.close()
print("Saved 2D histogram examples")

print("\n" + "=" * 55)
print("MATPLOTLIB PART 3 - BAR, HISTOGRAM, PIE COMPLETE!")
print("=" * 55)
print("\nNext: Matplotlib_Part4_Subplots.py")
