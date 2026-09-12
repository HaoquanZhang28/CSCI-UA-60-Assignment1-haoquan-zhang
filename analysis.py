import csv

# Read the CSV file with native Python using csv.DictReader
def load_csv(filepath):
    data = []
    # The dataset contains non-ASCII characters, so "latin-1" encoding is needed.
    with open(filepath, newline="", encoding="latin-1") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data


rows = load_csv("Sample - Superstore.csv")

# 1. Print the first 2 rows
print(rows[:2])
print()

# 2. Print the first row
print(rows[0])
print()

# 3. Print rows 10-19
print(rows[10:20])
print()

# 4. Print column names
print(rows[0].keys())
print()

# 5. Print the first 10 values of one column
for row in rows[:10]:
    print(row["Order ID"])
print()

# 6. Print the first 10 rows of three columns:
for row in rows[:10]:
    print(row["Order ID"], row["Customer Name"], row["Sales"])
print()

# 7.1 Which region in the United States has the highest sales in total?
sales_by_region = {}
for row in rows:
    region = row["Region"]
    sales = float(row["Sales"])
    sales_by_region[region] = sales_by_region.get(region, 0) + sales
highest_region = max(sales_by_region, key=sales_by_region.get)
print(f"The region with the highest sales is \"{highest_region}\", whose total sales is ${round(sales_by_region[highest_region], 2)}.")
print()

# 7.2 Which category of products has the highest profit?
profit_by_category = {}
for row in rows:
    category = row["Category"]
    profit = float(row["Profit"])
    profit_by_category[category] = profit_by_category.get(category, 0) + profit
highest_category = max(profit_by_category, key=profit_by_category.get)
print(f"The category with the highest profit is \"{highest_category}\", whose total profit is ${round(profit_by_category[highest_category], 2)}.")
print()

# 7.3 What is the net profit ratio of the discounted items?
total_discounted_sales = 0
total_discounted_profit = 0
for row in rows:
    discount = float(row["Discount"])
    if discount > 0:
        total_discounted_sales += float(row["Sales"])
        total_discounted_profit += float(row["Profit"])

net_profit_ratio = round(total_discounted_profit / total_discounted_sales * 100, 2)
print(f"The net profit ratio of the discounted items is {net_profit_ratio}%.")