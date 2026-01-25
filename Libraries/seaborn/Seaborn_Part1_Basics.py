# =============================================================================
# SEABORN PART 1 - BASICS (Beginner Level)
# =============================================================================
# Seaborn is a statistical data visualization library built on Matplotlib.
# It provides beautiful default styles and high-level functions for common plots.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# =============================================================================
# 1. GETTING STARTED
# =============================================================================
"""
Why Seaborn?
    - Beautiful default themes
    - Works seamlessly with Pandas DataFrames
    - Built-in statistical functions
    - Less code than Matplotlib for complex plots
    - Great for exploratory data analysis

Installation:
    pip install seaborn
"""

# =============================================================================
# 2. BUILT-IN DATASETS
# =============================================================================
print("--- Built-in Datasets ---")

# Seaborn comes with sample datasets for practice
print("\nAvailable datasets:")
print(sns.get_dataset_names())

# Load a dataset
tips = sns.load_dataset('tips')
print("\nTips dataset:")
print(tips.head())
print("\nShape:", tips.shape)

# Other useful datasets
iris = sns.load_dataset('iris')
titanic = sns.load_dataset('titanic')
penguins = sns.load_dataset('penguins')

# =============================================================================
# 3. SETTING STYLE AND THEMES
# =============================================================================
print("\n--- Themes and Styles ---")

# Available themes: darkgrid, whitegrid, dark, white, ticks
sns.set_theme(style="whitegrid")  # Set default theme

# Theme demonstration
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

themes = ['darkgrid', 'whitegrid', 'dark', 'white']
for ax, theme in zip(axes.flat, themes):
    sns.set_style(theme)
    sns.barplot(x=['A', 'B', 'C'], y=[3, 7, 5], ax=ax)
    ax.set_title(f'Theme: {theme}')

plt.tight_layout()
plt.savefig('seaborn_themes.png', dpi=100)
plt.close()
print("Saved theme comparison to 'seaborn_themes.png'")

# Reset to default
sns.set_theme(style="whitegrid")

# =============================================================================
# 4. COLOR PALETTES
# =============================================================================
print("\n--- Color Palettes ---")

# View available palettes
"""
Built-in palettes:
    - deep, muted, pastel, bright, dark, colorblind (categorical)
    - Blues, Reds, Greens, etc. (sequential)
    - RdBu, coolwarm, etc. (diverging)
"""

# Set a color palette
sns.set_palette("husl")

# Custom palette
custom_palette = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
sns.set_palette(custom_palette)

# View a palette
plt.figure(figsize=(8, 2))
sns.palplot(sns.color_palette("Set2", 8))
plt.title("Set2 Palette")
plt.savefig('seaborn_palette.png', dpi=100)
plt.close()
print("Saved palette sample to 'seaborn_palette.png'")

# Reset to default
sns.set_palette("deep")

# =============================================================================
# 5. FIGURE SIZE AND CONTEXT
# =============================================================================
print("\n--- Context and Scaling ---")

# Context affects font sizes and line widths
# Options: paper, notebook (default), talk, poster
sns.set_context("notebook")  # Good for Jupyter notebooks
# sns.set_context("talk")    # Larger fonts for presentations
# sns.set_context("poster")  # Even larger for posters

# Custom context with scaling
sns.set_context("notebook", font_scale=1.2)

# =============================================================================
# 6. BASIC SCATTER PLOT
# =============================================================================
print("\n--- Basic Scatter Plot ---")

plt.figure(figsize=(8, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.title('Total Bill vs Tip')
plt.savefig('seaborn_scatter_basic.png', dpi=100)
plt.close()
print("Saved basic scatter plot")

# Enhanced scatter with hue (color by category)
plt.figure(figsize=(8, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time')
plt.title('Tips by Time of Day')
plt.savefig('seaborn_scatter_hue.png', dpi=100)
plt.close()
print("Saved scatter plot with hue")

# With size and style
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=tips, 
    x='total_bill', 
    y='tip', 
    hue='day',        # Color by day
    size='size',      # Point size by party size
    style='time',     # Shape by time
    palette='Set2'
)
plt.title('Comprehensive Tip Analysis')
plt.savefig('seaborn_scatter_full.png', dpi=100)
plt.close()
print("Saved full scatter plot")

# =============================================================================
# 7. BASIC LINE PLOT
# =============================================================================
print("\n--- Basic Line Plot ---")

# Create time series data
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=30)
sales_data = pd.DataFrame({
    'Date': dates,
    'Sales': np.cumsum(np.random.randn(30)) + 50,
    'Region': ['North']*15 + ['South']*15
})

plt.figure(figsize=(10, 5))
sns.lineplot(data=sales_data, x='Date', y='Sales')
plt.title('Daily Sales Trend')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('seaborn_line_basic.png', dpi=100)
plt.close()
print("Saved basic line plot")

# Line plot with confidence interval
plt.figure(figsize=(10, 5))
sns.lineplot(data=sales_data, x='Date', y='Sales', hue='Region')
plt.title('Sales by Region')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('seaborn_line_hue.png', dpi=100)
plt.close()
print("Saved line plot with hue")

# =============================================================================
# 8. BASIC BAR PLOT
# =============================================================================
print("\n--- Basic Bar Plot ---")

plt.figure(figsize=(8, 5))
sns.barplot(data=tips, x='day', y='total_bill')
plt.title('Average Bill by Day')
plt.savefig('seaborn_bar_basic.png', dpi=100)
plt.close()
print("Saved basic bar plot")

# Note: Seaborn shows mean with confidence intervals by default

# Bar plot with hue
plt.figure(figsize=(8, 5))
sns.barplot(data=tips, x='day', y='total_bill', hue='sex')
plt.title('Average Bill by Day and Gender')
plt.savefig('seaborn_bar_hue.png', dpi=100)
plt.close()
print("Saved bar plot with hue")

# Horizontal bar plot
plt.figure(figsize=(8, 5))
sns.barplot(data=tips, y='day', x='total_bill', orient='h')
plt.title('Average Bill by Day (Horizontal)')
plt.savefig('seaborn_bar_horizontal.png', dpi=100)
plt.close()
print("Saved horizontal bar plot")

# =============================================================================
# 9. COUNT PLOT
# =============================================================================
print("\n--- Count Plot ---")

# Count plot - shows frequency of categories
plt.figure(figsize=(8, 5))
sns.countplot(data=tips, x='day')
plt.title('Number of Visits by Day')
plt.savefig('seaborn_count_basic.png', dpi=100)
plt.close()
print("Saved count plot")

# Count plot with hue
plt.figure(figsize=(8, 5))
sns.countplot(data=tips, x='day', hue='time')
plt.title('Visits by Day and Time')
plt.savefig('seaborn_count_hue.png', dpi=100)
plt.close()
print("Saved count plot with hue")

# =============================================================================
# 10. SAVING AND DISPLAYING
# =============================================================================
print("\n--- Saving Plots ---")

"""
Save options:
    plt.savefig('plot.png', dpi=300)           # High resolution PNG
    plt.savefig('plot.pdf')                     # Vector format
    plt.savefig('plot.svg')                     # Scalable vector
    plt.savefig('plot.jpg', quality=95)         # JPEG

Display options:
    plt.show()                                  # Show in window/notebook
    plt.close()                                 # Close figure (free memory)
    plt.clf()                                   # Clear current figure
"""

# Example with multiple customizations
plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day', s=100, alpha=0.7)
plt.title('Restaurant Tips Analysis', fontsize=14, fontweight='bold')
plt.xlabel('Total Bill ($)', fontsize=12)
plt.ylabel('Tip ($)', fontsize=12)
plt.legend(title='Day', loc='upper left')
plt.tight_layout()
plt.savefig('seaborn_final_example.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved final example plot")

print("\n" + "=" * 55)
print("SEABORN PART 1 - BASICS COMPLETE!")
print("=" * 55)
print("\nAll plots saved as PNG files in current directory.")
