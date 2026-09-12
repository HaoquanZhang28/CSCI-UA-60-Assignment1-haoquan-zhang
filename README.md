# Superstore Dataset (Dataset containing Sales & Profits of a Superstore)    
#kaggle dataset link: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final    
#GitHub Repository link: https://github.com/HaoquanZhang28/CSCI-UA-60-Assignment1-haoquan-zhang    
#edstem workspace link: https://edstem.org/us/courses/105050/workspaces/pLV3Qv2auljAudoenES6l4w6YjTe4X4k    

## Why I Chose This Dataset?    
I chose the superstore dataset because it contains real retail data that covers various fields such as regions, sales, profits, etc. These fields make the dataset suitable for analyzing realistic business operational problems. Besides, the topic of the dataset aligns with my career interests in data analysis and business analytics.    

---

## Three Data Questions    

### Question 1: Which region in the United States has the highest total sales?    
```python
# 7.1 [Filtering] Which region in the United States has the highest sales in total?
sales_by_region = {}
if row["Country"] == "United States":
    for row in rows:
        region = row["Region"]
        sales = float(row["Sales"])
        sales_by_region[region] = sales_by_region.get(region, 0) + sales
highest_region = max(sales_by_region, key=sales_by_region.get)
print(f"The region with the highest sales is \"{highest_region}\", whose total sales is ${round(sales_by_region[highest_region], 2)}.")
```
The output is:    
```text
The region with the highest sales is "West", whose total sales is $725457.82.
```

Why the data structure supports this question:    
This works because the column "Country" can serve as a filter to find transactions in the United States, the column "Region" is a categorical attribute that divides the U.S. market into 4 regions (East, Central, South, and West), and the column "Sales" is a quantitative attribute that shows the sales of each transaction. With the two columns, the data supports this question.    

### Question 2: Which product category has the highest profit?    
```python
# 7.2 Which category of products has the highest profit?
profit_by_category = {}
for row in rows:
    category = row["Category"]
    profit = float(row["Profit"])
    profit_by_category[category] = profit_by_category.get(category, 0) + profit
highest_category = max(profit_by_category, key=profit_by_category.get)
print(f"The category with the highest profit is \"{highest_category}\", whose total profit is ${round(profit_by_category[highest_category], 2)}.")
```
The output is:    
```text
The category with the highest profit is "Technology", whose total profit is $145454.95.
```

Why the data structure supports this question:    
This works because the column "Profit" is a quantitative attribute that shows the profits of each transaction, while the column "Category" groups similar products together. With the two columns, the data supports this question.    

### Question 3: What is the net profit ratio of the discounted items?    
```python
# 7.3 [Filtering, Counting, Two-condition breakdown] What is the net profit ratio of the discounted items in the "Technology" category?
total_discounted_sales = 0
total_discounted_profit = 0
count = 0
for row in rows:
    discount = float(row["Discount"])
    category = row["Category"]
    if discount > 0 and category == "Technology":
        total_discounted_sales += float(row["Sales"])
        total_discounted_profit += float(row["Profit"])
        count += 1

net_profit_ratio = round(total_discounted_profit / total_discounted_sales * 100, 2)
print(f"The net profit ratio of the discounted items in the \"Technology\" category is {net_profit_ratio}%. This statistics is based on {count} discounted transactions and ${round(total_discounted_sales, 2)} total sales.")
```
The output is:    
```text
The net profit ratio of the discounted items in the "Technology" category is 2.94%. This statistics is based on 1014 discounted transactions and $446420.83 total sales.
```

Why the data structure supports this question:    
This works because the column "Discount" shows the discount applied to each transaction, while the column "Category" serves as the other filtering condition to find a particular category of products. I can filter the discounted technology items and calculate the net profit ratio by dividing the total profit by the total sales.    

---

## What the Data Cannot Answer    
The data cannot answer: How does a level of discount make a product more or less profitable?    
The dataset cannot answer because it doesn't include useful information that is related to the purchase motivation of customers, such as whether they are sensitive to prices, whether they purchase because of the discounts, etc.    
Without this information, it may be misleading to assume that there are relationships between the discounts of products and the profits of the store selling them.     
