import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Dataset .csv')

# Check basic info and nulls
# df.info()

# Drop rows with 0 rating, they are usually unrated
df_clean = df[df['Aggregate rating'] != 0].copy()

# 1. Cities with most restaurants
plt.figure()
top_cities = df['City'].value_counts().head(10)
sns.barplot(y=top_cities.index, x=top_cities.values, color='steelblue')
plt.title('Top 10 Cities')
plt.xlabel('Number of Restaurants')
plt.tight_layout()
plt.savefig('top_cities.png')

# 2. Rating distribution
plt.figure()
sns.histplot(df_clean['Aggregate rating'], bins=20)
plt.title('Rating Distribution')
plt.tight_layout()
plt.savefig('rating_dist.png')

# 3. Price range vs rating
plt.figure()
sns.boxplot(data=df_clean, x='Price range', y='Aggregate rating', color='lightgreen')
plt.title('Ratings by Price Range')
plt.tight_layout()
plt.savefig('price_vs_rating.png')

# 4. Delivery pie chart
plt.figure()
delivery_counts = df['Has Online delivery'].value_counts()
plt.pie(delivery_counts, labels=delivery_counts.index, autopct='%1.0f%%')
plt.title('Has Online Delivery?')
plt.tight_layout()
plt.savefig('delivery_pie.png')

