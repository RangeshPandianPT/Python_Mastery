# =============================================================================
# SEABORN PART 4 - RELATIONAL PLOTS (Intermediate)
# =============================================================================
# Relational plots show relationships between variables.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.set_theme(style="whitegrid")
tips = sns.load_dataset('tips')
fmri = sns.load_dataset('fmri')

# =============================================================================
# 1. SCATTER PLOT
# =============================================================================
print("--- Scatter Plot ---")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

sns.scatterplot(data=tips, x='total_bill', y='tip', ax=axes[0, 0])
axes[0, 0].set_title('Basic Scatter')

sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time', ax=axes[0, 1])
axes[0, 1].set_title('Colored by Time')

sns.scatterplot(data=tips, x='total_bill', y='tip', size='size', ax=axes[1, 0])
axes[1, 0].set_title('Size by Party')

sns.scatterplot(data=tips, x='total_bill', y='tip', 
                hue='day', style='time', size='size', ax=axes[1, 1])
axes[1, 1].set_title('Multiple Encodings')

plt.tight_layout()
plt.savefig('seaborn_scatterplot.png', dpi=100)
plt.close()

# =============================================================================
# 2. LINE PLOT
# =============================================================================
print("\n--- Line Plot ---")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

sns.lineplot(data=fmri, x='timepoint', y='signal', ax=axes[0, 0])
axes[0, 0].set_title('Basic Line (Mean + CI)')

sns.lineplot(data=fmri, x='timepoint', y='signal', hue='event', ax=axes[0, 1])
axes[0, 1].set_title('By Event Type')

sns.lineplot(data=fmri, x='timepoint', y='signal', 
             hue='region', style='event', ax=axes[1, 0])
axes[1, 0].set_title('Hue + Style')

sns.lineplot(data=fmri, x='timepoint', y='signal', 
             hue='event', errorbar=None, ax=axes[1, 1])
axes[1, 1].set_title('Without CI')

plt.tight_layout()
plt.savefig('seaborn_lineplot.png', dpi=100)
plt.close()

# =============================================================================
# 3. RELPLOT (Figure-Level Function)
# =============================================================================
print("\n--- Relplot ---")

g = sns.relplot(data=tips, x='total_bill', y='tip', 
                col='time', hue='day', kind='scatter', height=4)
plt.savefig('seaborn_relplot.png', dpi=100)
plt.close()

# =============================================================================
# 4. REGRESSION PLOTS
# =============================================================================
print("\n--- Regression Plots ---")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

sns.regplot(data=tips, x='total_bill', y='tip', ax=axes[0, 0])
axes[0, 0].set_title('Linear Regression')

sns.regplot(data=tips, x='total_bill', y='tip', order=2, ax=axes[0, 1])
axes[0, 1].set_title('Polynomial (order=2)')

sns.regplot(data=tips, x='total_bill', y='tip', lowess=True, ax=axes[1, 0])
axes[1, 0].set_title('LOWESS Regression')

sns.regplot(data=tips, x='total_bill', y='tip', ci=None, ax=axes[1, 1])
axes[1, 1].set_title('No Confidence Interval')

plt.tight_layout()
plt.savefig('seaborn_regplot.png', dpi=100)
plt.close()

# =============================================================================
# 5. LMPLOT (Regression with Faceting)
# =============================================================================
print("\n--- LMPlot ---")

g = sns.lmplot(data=tips, x='total_bill', y='tip', 
               hue='smoker', col='time', height=4)
plt.savefig('seaborn_lmplot.png', dpi=100)
plt.close()

print("\n" + "=" * 55)
print("SEABORN PART 4 - RELATIONAL PLOTS COMPLETE!")
print("=" * 55)
