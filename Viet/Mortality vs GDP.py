import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from the uploaded CSV file
file_path = '/mnt/data/child-mortality-gdp-per-capita (1).csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
data.head(), data.columns
# Remove rows with missing values in the necessary columns
cleaned_data = data.dropna(subset=['Under-five mortality rate', 'GDP per capita'])

# Get the most recent data for each country
latest_data = cleaned_data.sort_values('Year').groupby('Entity').tail(1)

# Sort data by GDP per capita and Under-five mortality rate
sorted_by_gdp = latest_data.sort_values('GDP per capita', ascending=False)
sorted_by_mortality = latest_data.sort_values('Under-five mortality rate')

# Bin GDP into groups: low, middle, high
gdp_bins = pd.qcut(sorted_by_gdp['GDP per capita'], 3, labels=['Low', 'Middle', 'High'])
latest_data['GDP Group'] = gdp_bins

# Calculate mean Under-five mortality rate for each GDP group
mortality_by_gdp_group = latest_data.groupby('GDP Group')['Under-five mortality rate'].mean()

latest_data.head(), mortality_by_gdp_group

# Set the style
sns.set(style="whitegrid")

# Create scatter plot
plt.figure(figsize=(12, 8))
scatter_plot = sns.scatterplot(x='GDP per capita', y='Under-five mortality rate', hue='GDP Group', style='GDP Group', s=100, data=latest_data)
plt.title('Scatter Plot of Under-five Mortality Rate vs GDP per Capita')
plt.xlabel('GDP per Capita (USD)')
plt.ylabel('Under-five Mortality Rate (per 1000 live births)')
plt.legend(title='GDP Group')
plt.grid(True)
plt.show()

# Create bar plot
plt.figure(figsize=(10, 6))
bar_plot = sns.barplot(x='GDP Group', y='Under-five mortality rate', data=latest_data, estimator=np.mean, ci=None, palette='coolwarm')
plt.title('Average Under-five Mortality Rate by GDP Group')
plt.xlabel('GDP Group')
plt.ylabel('Average Under-five Mortality Rate (per 1000 live births)')
plt.show()

