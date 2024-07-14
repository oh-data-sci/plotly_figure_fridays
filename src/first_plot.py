import pandas as pd
import plotly.express as px

# Load the data from the Excel file
df = pd.read_excel('data/superstore.xlsx')

# Filter the data to only include sales <= 10,000
df_filtered = df[df['Sales'] <= 10_000]

# Create a scatter plot with sales on the x-axis, profits on the y-axis, and color by category
fig = px.scatter(df_filtered, x='Sales', y='Profit', color='Category', title='Sales vs Profit by Category (Sales <= 10,000)')

# Show the plot
fig.show()
