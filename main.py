import pandas as pd

# Replace 'yourfile.csv' with the path to your CSV file
file_path = 'yourfile.csv'

# Read the CSV file
df = pd.read_csv(file_path, names=['Date', 'Price'])

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

# Function to convert price from string to float
def convert_price(price):
    # Remove the dollar sign and commas
    price = price.replace('$', '').replace(',', '')
    # Convert to float
    return float(price)

# Apply the conversion function to each price entry
df['Price'] = df['Price'].apply(convert_price)

# Extract month from the date for grouping
df['Month'] = df['Date'].dt.month

# Group by month and sum the prices
monthly_totals = df.groupby('Month')['Price'].sum().reset_index()

grand_total = monthly_totals['Price'].sum()
# Sort the results by month
monthly_totals = monthly_totals.sort_values(by='Month')

# Print the result
print(monthly_totals)
print(f"\nGrand Total: ${grand_total:.2f}")