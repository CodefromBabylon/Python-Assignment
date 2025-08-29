# Data Analysis with Pandas and Visualization with Matplotlib
# Using the Iris dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import numpy as np

# Set style for better looking plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Task 1: Load and Explore the Dataset
print("=" * 50)
print("TASK 1: LOAD AND EXPLORE THE DATASET")
print("=" * 50)

try:
    # Load the Iris dataset
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    
    print("Dataset loaded successfully!")
    print(f"Dataset shape: {df.shape}")
    
    # Display first few rows
    print("\nFirst 5 rows of the dataset:")
    print(df.head())
    
    # Explore structure
    print("\nDataset information:")
    print(df.info())
    
    # Check for missing values
    print("\nMissing values in each column:")
    print(df.isnull().sum())
    
    # Clean dataset (though Iris dataset is already clean)
    # For demonstration, we'll show how to handle missing values if they existed
    if df.isnull().sum().sum() > 0:
        print("\nCleaning dataset...")
        # Fill numerical missing values with mean
        numerical_cols = df.select_dtypes(include=[np.number]).columns
        df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())
        
        # Fill categorical missing values with mode
        categorical_cols = df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            df[col] = df[col].fillna(df[col].mode()[0])
        
        print("Dataset cleaned successfully!")
    else:
        print("\nNo missing values found. Dataset is clean!")

except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

# Task 2: Basic Data Analysis
print("\n" + "=" * 50)
print("TASK 2: BASIC DATA ANALYSIS")
print("=" * 50)

# Basic statistics
print("Basic statistics for numerical columns:")
print(df.describe())

# Group by species and compute means
print("\nMean values by species:")
species_means = df.groupby('species').mean()
print(species_means)

# Additional analysis
print("\nAdditional findings:")
print(f"1. Number of samples per species:")
print(df['species'].value_counts())

print(f"\n2. Correlation between features:")
correlation_matrix = df.select_dtypes(include=[np.number]).corr()
print(correlation_matrix)

# Task 3: Data Visualization
print("\n" + "=" * 50)
print("TASK 3: DATA VISUALIZATION")
print("=" * 50)

# Create a figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Iris Dataset Analysis - Visualizations', fontsize=16, fontweight='bold')

# 1. Line chart (simulating trends by creating a time index)
# Since Iris doesn't have time data, we'll create a synthetic example
plt.subplot(2, 2, 1)
df_sorted = df.sort_values('sepal length (cm)')
plt.plot(df_sorted['sepal length (cm)'], df_sorted['petal length (cm)'], 
         marker='o', linestyle='-', linewidth=2, markersize=4, alpha=0.7)
plt.title('Trend: Petal Length vs Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.grid(True, alpha=0.3)

# 2. Bar chart - average sepal length by species
plt.subplot(2, 2, 2)
species_means = df.groupby('species')['sepal length (cm)'].mean()
colors = ['skyblue', 'lightcoral', 'lightgreen']
species_means.plot(kind='bar', color=colors, edgecolor='black', alpha=0.8)
plt.title('Average Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Sepal Length (cm)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

# 3. Histogram - distribution of sepal length
plt.subplot(2, 2, 3)
plt.hist(df['sepal length (cm)'], bins=15, color='lightblue', 
         edgecolor='black', alpha=0.8)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)

# 4. Scatter plot - sepal length vs petal length colored by species
plt.subplot(2, 2, 4)
colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
for species, color in colors.items():
    subset = df[df['species'] == species]
    plt.scatter(subset['sepal length (cm)'], subset['petal length (cm)'],
               color=color, alpha=0.7, label=species, s=50)
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Additional visualizations with seaborn for better styling
print("\nAdditional Seaborn Visualizations:")
plt.figure(figsize=(15, 10))

# Box plot
plt.subplot(2, 2, 1)
sns.boxplot(x='species', y='sepal length (cm)', data=df)
plt.title('Sepal Length Distribution by Species')
plt.xticks(rotation=45)

# Violin plot
plt.subplot(2, 2, 2)
sns.violinplot(x='species', y='petal length (cm)', data=df)
plt.title('Petal Length Distribution by Species')
plt.xticks(rotation=45)

# Pair plot (comprehensive view)
plt.subplot(2, 2, 3)
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', 
                hue='species', data=df, palette='viridis', s=60)
plt.title('Sepal vs Petal Length by Species')

# Heatmap
plt.subplot(2, 2, 4)
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')

plt.tight_layout()
plt.show()

# Findings and Observations
print("\n" + "=" * 50)
print("FINDINGS AND OBSERVATIONS")
print("=" * 50)

print("""
1. DATA OVERVIEW:
   - The Iris dataset contains 150 samples with 4 numerical features and 1 categorical target (species)
   - Three species: setosa, versicolor, and virginica (50 samples each)

2. KEY FINDINGS:
   - Setosa species has distinctly smaller petal dimensions compared to the other two species
   - Virginica has the largest sepal and petal measurements on average
   - Strong positive correlation exists between petal length and petal width (0.96)
   - Sepal length also shows good correlation with petal dimensions

3. VISUALIZATION INSIGHTS:
   - The scatter plot clearly shows three distinct clusters corresponding to the three species
   - Setosa is easily separable from the other two species based on petal measurements
   - Versicolor and virginica have some overlap but are generally separable
   - All features show approximately normal distributions within each species

4. POTENTIAL APPLICATIONS:
   - This dataset is excellent for classification problems
   - The clear separability makes it good for demonstrating machine learning algorithms
   - The correlations suggest that dimensionality reduction could be effective
""")

# Save the cleaned dataset (optional)
df.to_csv('cleaned_iris_dataset.csv', index=False)
print("Cleaned dataset saved as 'cleaned_iris_dataset.csv'")