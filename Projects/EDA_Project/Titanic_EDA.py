"""
Titanic_EDA.py
A Capstone Mini-Project performing Exploratory Data Analysis (EDA) 
using Pandas, Matplotlib, and Seaborn.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    print("=== TITANIC EXPLORATORY DATA ANALYSIS (EDA) ===")
    
    # 1. Load Dataset
    # Seaborn has built-in datasets for practice
    print("Loading Titanic Dataset...")
    df = sns.load_dataset('titanic')
    
    # 2. Basic Inspection
    print("\n--- First 5 Rows ---")
    print(df.head())
    
    print("\n--- Dataset Info ---")
    print(df.info())
    
    print("\n--- Missing Values ---")
    print(df.isnull().sum())
    
    # 3. Data Cleaning
    print("\n--- Cleaning Data ---")
    # 'deck' has too many missing values, let's drop the column
    df.drop('deck', axis=1, inplace=True)
    # Fill missing ages with the median age
    df['age'] = df['age'].fillna(df['age'].median())
    # Drop remaining rows with missing values (e.g., embarked)
    df.dropna(inplace=True)
    print("Remaining Missing Values:", df.isnull().sum().sum())
    
    # 4. Statistical Summary
    print("\n--- Statistical Summary ---")
    print(df.describe())
    
    # 5. Visualizations
    print("\n--- Generating Visualizations ---")
    # Set the style
    sns.set_theme(style="whitegrid")
    
    # Create a figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Titanic Dataset Exploratory Data Analysis', fontsize=16)
    
    # Plot 1: Survival Count
    sns.countplot(data=df, x='survived', ax=axes[0, 0], palette='pastel')
    axes[0, 0].set_title('Survival Count (0 = No, 1 = Yes)')
    axes[0, 0].set_xticklabels(['Did Not Survive', 'Survived'])
    
    # Plot 2: Survival by Gender
    sns.countplot(data=df, x='survived', hue='sex', ax=axes[0, 1], palette='Set2')
    axes[0, 1].set_title('Survival by Gender')
    axes[0, 1].set_xticklabels(['Did Not Survive', 'Survived'])
    
    # Plot 3: Age Distribution by Survival
    sns.histplot(data=df, x='age', hue='survived', kde=True, ax=axes[1, 0], palette='Set1', alpha=0.6)
    axes[1, 0].set_title('Age Distribution grouped by Survival')
    
    # Plot 4: Survival by Passenger Class
    sns.barplot(data=df, x='pclass', y='survived', ax=axes[1, 1], palette='Blues_d')
    axes[1, 1].set_title('Survival Rate by Passenger Class')
    axes[1, 1].set_ylabel('Survival Probability')
    
    plt.tight_layout()
    plt.show()

    # Correlation Matrix Heatmap
    print("Generating Correlation Heatmap...")
    plt.figure(figsize=(8, 6))
    # Select only numerical columns for correlation
    numeric_df = df.select_dtypes(include=[np.number])
    corr_matrix = numeric_df.corr()
    
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)
    plt.title('Correlation Matrix of Numeric Features')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
