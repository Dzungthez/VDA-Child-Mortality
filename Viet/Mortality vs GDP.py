import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

file_path = 'E:\VDA-Child-Mortality\Viet\child-mortality-gdp-per-capita.csv'
data = pd.read_csv(file_path)

data.head(), data.columns
# Remove NaN rows
cleaned_data = data.dropna(subset=['Under-five mortality rate', 'GDP per capita'])
latest_data = cleaned_data.sort_values('Year').groupby('Entity').tail(1)

sorted_by_gdp = latest_data.sort_values('GDP per capita', ascending=False)
sorted_by_mortality = latest_data.sort_values('Under-five mortality rate')

# Bin GDP into groups
gdp_bins = pd.qcut(sorted_by_gdp['GDP per capita'], 3, labels=['Low', 'Middle', 'High'])
latest_data['GDP Group'] = gdp_bins

# Calculate mean Under-five mortality rate for each GDP group
mortality_by_gdp_group = latest_data.groupby('GDP Group')['Under-five mortality rate'].mean()
latest_data.head(), mortality_by_gdp_group

sns.set(style="darkgrid")
# Scatter plot
plt.figure(figsize=(12, 8))
scatter_plot = sns.scatterplot(x='GDP per capita', y='Under-five mortality rate', hue='GDP Group', style='GDP Group', s=100, data=latest_data)
plt.title('Scatter Plot of Under-five Mortality Rate vs GDP per Capita')
plt.xlabel('GDP per Capita (USD)')
plt.ylabel('Under-five Mortality Rate (per 1000 live births)')
plt.legend(title='GDP Group')
plt.grid(True)
plt.show()

# Bar plot
plt.figure(figsize=(10, 6))
bar_plot = sns.barplot(x='GDP Group', y='Under-five mortality rate', data=latest_data, estimator=np.mean, ci=None, palette='coolwarm')
plt.title('Bar plot of Average Under-five Mortality Rate by GDP Group')
plt.xlabel('GDP Group')
plt.ylabel('Average Under-five Mortality Rate (per 1000 live births)')
plt.show()

