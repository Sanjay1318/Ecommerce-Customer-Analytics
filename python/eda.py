import pandas as pd

# Load dataset
df = pd.read_excel('../data/OnlineRetail.xlsx')

# Remove missing Customer IDs
df = df[df['CustomerID'].notnull()]

# Create Revenue column
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Remove duplicates
df = df.drop_duplicates()

# Print updated info
print("Rows after cleaning:", len(df))
print("Columns:", df.shape[1])
print("\nSample data after cleaning:\n")
print(df.head(10))
# Summary Insights

print("\nTotal Unique Customers:", df['CustomerID'].nunique())
print("Total Revenue:", df['Revenue'].sum())

# Revenue by Country (excluding UK because it has most data)
country_rev = df[df['Country'] != 'United Kingdom'].groupby('Country')['Revenue'].sum().sort_values(ascending=False)
print("\nTop Revenue Countries:\n", country_rev.head(5))

# Top 5 Customers by Revenue
top_customers = df.groupby('CustomerID')['Revenue'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Revenue Customers:\n", top_customers)

import matplotlib.pyplot as plt

# Revenue by top countries bar chart
top_countries = country_rev.head(5)
top_countries.plot(kind='bar')
plt.title("Top 5 Revenue Countries (Excluding UK)")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig('../images/top_countries.png')
plt.close()

# Top 5 customers bar chart
top_customers.plot(kind='bar')
plt.title("Top 5 Revenue Customers")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig('../images/top_customers.png')
plt.close()

print("\nPlots saved in images folder.")

df.to_excel('../data/OnlineRetail_Cleaned.xlsx', index=False)
print("Cleaned file exported.")
