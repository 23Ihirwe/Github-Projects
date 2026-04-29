import pandas as pd
import plotly.express as px

# 1. Load the data
df = pd.read_csv('ecommerce_funnel_data.csv')

# 2. Group by stage to count unique users
funnel_df = df.groupby('stage')['user_id'].nunique().reset_index()
funnel_df.columns = ['Stage', 'Users']

# 3. Sort stages in logical business order
order = ['landing_page', 'product_view', 'add_to_cart', 'checkout_start', 'purchase']
funnel_df['Stage'] = pd.Categorical(funnel_df['Stage'], categories=order, ordered=True)
funnel_df = funnel_df.sort_values('Stage')

# 4. Calculate Business Metrics (Drop-off)
funnel_df['Conversion_Rate'] = (funnel_df['Users'] / funnel_df['Users'].shift(1) * 100).fillna(100)

# 5. Create the Visualization
fig = px.funnel(funnel_df, x='Users', y='Stage', 
                title='E-commerce Funnel: Where are we losing customers?',
                color_discrete_sequence=['#636EFA'])

print("--- Analysis Complete ---")
print(funnel_df)

fig.write_html("funnel_chart.html")
print("Success! Your chart is saved as 'funnel_chart.html' in your folder.")
