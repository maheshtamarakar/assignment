from datetime import datetime

f = open("./assets/sales-data.txt", "r")
# global variables
data = f.readlines() # storing all sales-data as an list of string
rupee_symbol = u'\u20B9'
sales_data = []
months = {
    1: "2019-01-01",
    2: "2019-02-01",
    3: "2019-03-01"
}

# converting list of string to list of object
for i in range(1, len(data) - 1):
    sale_row = data[i]
    sale_row = sale_row.replace("\n", "")
    sales_data_list = sale_row.split(',')
    sale_obj = {
        "date": sales_data_list[0],
        "sku": sales_data_list[1],
        "unit_price": sales_data_list[2],
        "qty": sales_data_list[3],
        "total_price": sales_data_list[4],
    }
    sales_data.append(sale_obj)
# print(sales_data)

# Tasks
# 1. Total sales of the store.

total_sale = 0
for sales_obj in sales_data:
    total_sale += int(sales_obj["total_price"])
total_sale_formatted = "{:,}".format(total_sale) # formatting number
print(f"1. Total sales of the store: {total_sale_formatted}{rupee_symbol}\n")

# 2. Month wise sales totals.

# these are the months that are available
# 2019-01-01
# 2019-02-01
# 2019-03-01

months_sales = {}
for sales_obj in sales_data:
    date = sales_obj["date"]
    dt = datetime.strptime(date, '%Y-%m-%d')
    # if month not exist add that key with that value
    if dt.month not in months_sales:
        months_sales[dt.month] = int(sales_obj["total_price"])
    else:
        # if month exist keep updating total_price
        months_sales[dt.month] += int(sales_obj["total_price"])

print("2. Month wise sales totals.\n")
for key in months_sales.keys():
    months_sales_formatted = "{:,}".format(months_sales[key])
    print(f"Total sale in {months[key]}: {months_sales_formatted}{rupee_symbol}")

# 3. Most popular item (most quantity sold) in each month.

# ******************only for testing*******************
# sales_data[0]["qty"] = 8
# sales_data[7000]["qty"] = 68
# sales_data[10000]["qty"] = 7

months_max_qty = {}
months_max_qty_item = {}
months_popular_item = {}


def find_max(old_qty, new_qty, month, item, max_qty, max_item):
    if new_qty > old_qty:
        max_qty[month] = new_qty
        max_item[month] = item

for sales_obj in sales_data:
    date = sales_obj["date"]
    dt = datetime.strptime(date, '%Y-%m-%d')
    month = dt.month
    item = sales_obj["sku"]
    qty = int(sales_obj["qty"])
    # see if this month exist in months_max_rev obj if not add it
    if month not in months_max_qty:
        months_max_qty[month] = {
            item: qty
        }
    # if month already exist check if that item already exist or not in that month object(nested object)
    else:
        # if item not exist create that item with value as total_price of it
        if item not in months_max_qty[month]:
            months_max_qty[month][item] = qty
        # if item already exist add the total_price
        else:
            months_max_qty[month][item] += qty
# example
# months_max_qty = {
#     1: {
#         "Cake Fudge": 900,
#         "Vanilla": 600,
#         ...
#     },
#     2: {
#         "Cake Fudge": 900,
#         "Vanilla": 600,
#         ...
#     },
#     3: {
#         "Cake Fudge": 900,
#         "Vanilla": 600,
#         ...
#     },
# }
#

# #find max_rev each month
for sales in months_max_qty.keys():
    MAX_QTY = 0
    item_name = ''
    for item in months_max_qty[sales].keys():
        if months_max_qty[sales][item] > MAX_QTY:
            MAX_QTY = months_max_qty[sales][item]
            item_name = item
    months_max_qty_item[sales] = item_name + ": " + str(MAX_QTY)
    months_popular_item[sales] = item_name

print("\n3. Most popular item (most quantity sold) in each month.\n")
for key in months_max_qty.keys():
    print(f"{months[key]}: {months_max_qty_item[key]}")

# 4. Items generating most revenue in each month.

# **************only for testing************
# sales_data[0]["total_price"] = 800000
# sales_data[7000]["total_price"] = 680000
# sales_data[10000]["total_price"] = 700000

months_max_rev = {}
months_max_rev_item = {}

for sales_obj in sales_data:
    date = sales_obj["date"]
    dt = datetime.strptime(date, '%Y-%m-%d')
    month = dt.month
    item = sales_obj["sku"]
    total_price = int(sales_obj["total_price"])
    # see if this month exist in months_max_rev obj if not add it
    if month not in months_max_rev:
        months_max_rev[month] = {
            item: total_price
        }
    # if month already exist check if that item already exist or not in that month object(nested object)
    else:
        # if item not exist create that item with value as total_price of it
        if item not in months_max_rev[month]:
            months_max_rev[month][item] = total_price
        # if item already exist add the total_price
        else:
            months_max_rev[month][item] += total_price

# example
# months_max_rev = {
#     1: {
#         "Cake Fudge": 900,
#         "Vanilla": 600,
#         ...
#     },
#     2: {
#         "Cake Fudge": 900,
#         "Vanilla": 600,
#         ...
#     },
#     3: {
#         "Cake Fudge": 900,
#         "Vanilla": 600,
#         ...
#     },
# }
#
# #find max_rev each month
for sales in months_max_rev.keys():
    MAX_REV = 0
    item_name = ''
    for item in months_max_rev[sales].keys():
        if months_max_rev[sales][item] > MAX_REV:
            MAX_REV = months_max_rev[sales][item]
            item_name = item
    months_max_rev_item[sales] = item_name + ": " + str(MAX_REV)

# print Items generating most revenue in each month.
print("\n4. Items generating most revenue in each month\n")
for key in months_max_rev_item.keys():
    print(f"{months[key]}: {months_max_rev_item[key]}")

# 5. For the most popular item, find the min, max and average number of orders each month.
pop_months_max_min_avg = {}
total_qty = 0

for sales_obj in sales_data:
    date = sales_obj["date"]
    dt = datetime.strptime(date, '%Y-%m-%d')
    month = dt.month
    item = sales_obj["sku"]
    qty = int(sales_obj["qty"])
    # see if this month exist in pop_months_max_min obj if not add it
    if month not in pop_months_max_min_avg:
        pop_months_max_min_avg[month] = {
            "max_order": qty,
            "min_order": qty,
            "count": 1
        }
    # if month already exist check if that item already exist or not in that month object(nested object)
    else:
        if item == months_popular_item[month]:
            # 1. find max
            pop_months_max_min_avg[month]["max_order"] += qty
            # 2. find min
            if pop_months_max_min_avg[month]["min_order"] > qty:
                pop_months_max_min_avg[month]["min_order"] = qty
            # 3. find avg
            pop_months_max_min_avg[month]["count"] += 1


# add avg order
for max_min_obj in pop_months_max_min_avg.keys():
    pop_months_max_min_avg[max_min_obj]["avg"] = pop_months_max_min_avg[max_min_obj]["max_order"]/pop_months_max_min_avg[max_min_obj]["count"]

print("\n5. For the most popular item, find the min, max and average number of orders each month.\n")
for key in pop_months_max_min_avg.keys():
    print(f"{months[key]}: max_order - {pop_months_max_min_avg[key]['max_order']}, min_order - {pop_months_max_min_avg[key]['min_order']}, average - {pop_months_max_min_avg[key]['avg']}")




