# =============================================================================
# SEABORN PART 3 - DISTRIBUTION PLOTS (Intermediate)
# =============================================================================
# Distribution plots help visualize how data is spread.
# Essential for understanding data characteristics before analysis.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set theme
sns.set_theme(style="whitegrid")

# Load datasets
tips = sns.load_dataset('tips')
penguins = sns.load_dataset('penguins').dropna()

print("Tips dataset preview:")
print(tips.head())

# =============================================================================
# 1. HISTOGRAM (histplot)
# =============================================================================
print("\n--- Histogram ---")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Basic histogram
sns.histplot(data=tips, x='total_bill', ax=axes[0, 0])
axes[0, 0].set_title('Basic Histogram')

# With custom bins
sns.histplot(data=tips, x='total_bill', bins=20, ax=axes[0, 1])
axes[0, 1].set_title('20 Bins')

# With KDE overlay
sns.histplot(data=tips, x='total_bill', kde=True, ax=axes[1, 0])
axes[1, 0].set_title('Histogram with KDE')

# Colored by category
sns.histplot(data=tips, x='total_bill', hue='time', ax=axes[1, 1])
axes[1, 1].set_title('By Time of Day')

plt.tight_layout()
plt.savefig('seaborn_histplot.png', dpi=100)
plt.close()
print("Saved histograms")

# Stacked histogram
plt.figure(figsize=(8, 5))
sns.histplot(data=tips, x='total_bill', hue='day', multiple='stack')
plt.title('Stacked Histogram by Day')
plt.savefig('seaborn_histplot_stacked.png', dpi=100)
plt.close()

# =============================================================================
# 2. KDE PLOT (Kernel Density Estimation)
# =============================================================================
print("\n--- KDE Plot ---")
"""
KDE shows the probability density function.
It's like a smooth histogram.
"""

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Basic KDE
sns.kdeplot(data=tips, x='total_bill', ax=axes[0, 0])
axes[0, 0].set_title('Basic KDE')

# Filled KDE
sns.kdeplot(data=tips, x='total_bill', fill=True, ax=axes[0, 1])
axes[0, 1].set_title('Filled KDE')

# Multiple KDEs
sns.kdeplot(data=tips, x='total_bill', hue='time', ax=axes[1, 0])
axes[1, 0].set_title('KDE by Time')

# With bandwidth adjustment
sns.kdeplot(data=tips, x='total_bill', bw_adjust=0.5, ax=axes[1, 1])
axes[1, 1].set_title('Narrow Bandwidth')

plt.tight_layout()
plt.savefig('seaborn_kdeplot.png', dpi=100)
plt.close()
print("Saved KDE plots")

# 2D KDE (bivariate)
plt.figure(figsize=(8, 6))
sns.kdeplot(data=tips, x='total_bill', y='tip', cmap='Blues', fill=True)
plt.title('2D KDE: Bill vs Tip')
plt.savefig('seaborn_kdeplot_2d.png', dpi=100)
plt.close()

# =============================================================================
# 3. DISPLOT (DISTRIBUTION FIGURE-LEVEL FUNCTION)
# =============================================================================
print("\n--- Displot ---")

# displot is the figure-level function for distributions
# It creates a new figure (can't use with subplots)

# Histogram (default)
g = sns.displot(tips, x='total_bill', kind='hist', height=4, aspect=1.5)
plt.title('Displot - Histogram')
plt.savefig('seaborn_displot_hist.png', dpi=100)
plt.close()

# KDE
g = sns.displot(tips, x='total_bill', kind='kde', fill=True, height=4, aspect=1.5)
plt.title('Displot - KDE')
plt.savefig('seaborn_displot_kde.png', dpi=100)
plt.close()

# ECDF (Empirical Cumulative Distribution Function)
g = sns.displot(tips, x='total_bill', kind='ecdf', height=4, aspect=1.5)
plt.title('Displot - ECDF')
plt.savefig('seaborn_displot_ecdf.png', dpi=100)
plt.close()
print("Saved displot examples")

# With faceting
g = sns.displot(
    tips, 
    x='total_bill', 
    col='time', 
    row='sex',
    kind='kde',
    fill=True,
    height=3,
    aspect=1.2
)
plt.savefig('seaborn_displot_facet.png', dpi=100)
plt.close()

# =============================================================================
# 4. ECDF PLOT
# =============================================================================
print("\n--- ECDF Plot ---")
"""
ECDF = Empirical Cumulative Distribution Function
Shows % of data below each value.
Useful for comparing distributions.
"""

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Basic ECDF
sns.ecdfplot(data=tips, x='total_bill', ax=axes[0])
axes[0].set_title('ECDF of Total Bill')

# Comparing groups
sns.ecdfplot(data=tips, x='total_bill', hue='time', ax=axes[1])
axes[1].set_title('ECDF by Time')

plt.tight_layout()
plt.savefig('seaborn_ecdfplot.png', dpi=100)
plt.close()
print("Saved ECDF plots")

# =============================================================================
# 5. RUG PLOT
# =============================================================================
print("\n--- Rug Plot ---")
"""
Rug plot shows individual data points as ticks.
Usually combined with other distribution plots.
"""

plt.figure(figsize=(10, 6))
sns.histplot(data=tips, x='total_bill', kde=True)
sns.rugplot(data=tips, x='total_bill', height=0.05, color='darkblue')
plt.title('Histogram with Rug Plot')
plt.savefig('seaborn_rugplot.png', dpi=100)
plt.close()
print("Saved rug plot")

# =============================================================================
# 6. JOINT PLOT (Bivariate Distribution)
# =============================================================================
print("\n--- Joint Plot ---")
"""
Joint plot shows the relationship between two variables
along with their individual distributions.
"""

# Scatter with histograms (default)
g = sns.jointplot(data=tips, x='total_bill', y='tip')
plt.savefig('seaborn_jointplot_scatter.png', dpi=100)
plt.close()
print("Saved joint plot (scatter)")

# With regression line
g = sns.jointplot(data=tips, x='total_bill', y='tip', kind='reg')
plt.savefig('seaborn_jointplot_reg.png', dpi=100)
plt.close()

# KDE version
g = sns.jointplot(data=tips, x='total_bill', y='tip', kind='kde', fill=True)
plt.savefig('seaborn_jointplot_kde.png', dpi=100)
plt.close()

# Hexbin (for large datasets)
g = sns.jointplot(data=tips, x='total_bill', y='tip', kind='hex')
plt.savefig('seaborn_jointplot_hex.png', dpi=100)
plt.close()

# With hue
g = sns.jointplot(data=tips, x='total_bill', y='tip', hue='time')
plt.savefig('seaborn_jointplot_hue.png', dpi=100)
plt.close()
print("Saved all joint plot variants")

# =============================================================================
# 7. PAIR PLOT (All Pairwise Relationships)
# =============================================================================
print("\n--- Pair Plot ---")
"""
Pair plot shows scatter plots for all variable pairs
and histograms on the diagonal.
"""

# Basic pair plot (using subset for speed)
penguins_subset = penguins[['bill_length_mm', 'bill_depth_mm', 
                             'flipper_length_mm', 'body_mass_g', 'species']]

g = sns.pairplot(penguins_subset, hue='species')
plt.savefig('seaborn_pairplot.png', dpi=100)
plt.close()
print("Saved pair plot")

# Pair plot with KDE on diagonal
g = sns.pairplot(penguins_subset, hue='species', diag_kind='kde')
plt.savefig('seaborn_pairplot_kde.png', dpi=100)
plt.close()

# Custom corner plot (lower triangle only)
g = sns.pairplot(penguins_subset, hue='species', corner=True)
plt.savefig('seaborn_pairplot_corner.png', dpi=100)
plt.close()

# =============================================================================
# 8. COMPARING MULTIPLE DISTRIBUTIONS
# =============================================================================
print("\n--- Comparing Distributions ---")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Multiple histograms
sns.histplot(data=tips, x='total_bill', hue='day', element='step', ax=axes[0, 0])
axes[0, 0].set_title('Step Histogram by Day')

# Multiple KDEs
sns.kdeplot(data=tips, x='total_bill', hue='day', fill=True, 
            alpha=0.4, ax=axes[0, 1])
axes[0, 1].set_title('KDE by Day')

# Overlapping histograms (dodged)
sns.histplot(data=tips, x='total_bill', hue='time', 
             multiple='dodge', shrink=0.8, ax=axes[1, 0])
axes[1, 0].set_title('Dodged Histogram')

# Multiple ECDFs
sns.ecdfplot(data=tips, x='total_bill', hue='day', ax=axes[1, 1])
axes[1, 1].set_title('ECDF by Day')

plt.tight_layout()
plt.savefig('seaborn_compare_distributions.png', dpi=100)
plt.close()
print("Saved distribution comparison plots")

# =============================================================================
# 9. STATISTICAL ANNOTATIONS
# =============================================================================
print("\n--- Adding Statistics ---")

plt.figure(figsize=(10, 6))

# Create histogram
sns.histplot(data=tips, x='total_bill', kde=True)

# Add vertical lines for statistics
mean_val = tips['total_bill'].mean()
median_val = tips['total_bill'].median()

plt.axvline(mean_val, color='red', linestyle='--', label=f'Mean: ${mean_val:.2f}')
plt.axvline(median_val, color='green', linestyle=':', label=f'Median: ${median_val:.2f}')
plt.legend()
plt.title('Distribution with Mean and Median')
plt.savefig('seaborn_dist_statistics.png', dpi=100)
plt.close()
print("Saved plot with statistics")

# =============================================================================
# 10. PRACTICAL EXAMPLE - PENGUIN ANALYSIS
# =============================================================================
print("\n--- Practical Example: Penguin Analysis ---")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Body mass distribution by species
sns.histplot(data=penguins, x='body_mass_g', hue='species', 
             kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Body Mass Distribution')

# Bill length distribution
sns.kdeplot(data=penguins, x='bill_length_mm', hue='species', 
            fill=True, ax=axes[0, 1])
axes[0, 1].set_title('Bill Length Distribution')

# 2D distribution
sns.kdeplot(data=penguins, x='bill_length_mm', y='bill_depth_mm',
            hue='species', ax=axes[1, 0])
axes[1, 0].set_title('Bill Dimensions by Species')

# ECDF comparison
sns.ecdfplot(data=penguins, x='flipper_length_mm', hue='species', ax=axes[1, 1])
axes[1, 1].set_title('Flipper Length ECDF')

plt.tight_layout()
plt.savefig('seaborn_penguin_analysis.png', dpi=100)
plt.close()
print("Saved penguin analysis")

print("\n" + "=" * 55)
print("SEABORN PART 3 - DISTRIBUTION PLOTS COMPLETE!")
print("=" * 55)
