# Example data
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]

def total_sales_by_product(data, product_key):
    """Calculates the total sales of a specific product in 30 days."""
    total = 0
    for sale in data:
        total += sale[product_key] 
    return total
    

def average_daily_sales(data, product_key):
    """Calculates the average daily sales of a specific product."""
    total = 0
    n = 0
    for sale in data:
        total += sale[product_key]
        n += 1
    Aver = total/n
    return Aver


def best_selling_day(data):
    """Finds the day with the highest total sales."""
    high = 0
    best_day = None
    for sale in data:
        total_day = sale["product_a"]+sale["product_b"]+sale["product_c"]
        if total_day > high:
            high = total_day
            best_day = sale["day"]
    return best_day


def days_above_threshold(data, product_key, threshold):
    """Counts how many days the sales of a product exceeded a given threshold."""
    count = 0
    for sale in data:
        if sale[product_key] > threshold:
            count += 1
    return count


def top_product(data):
    """Determines which product had the highest total sales in 30 days."""
    total_a = 0
    total_b = 0
    total_c = 0
    for sale in data:
        total_a += sale["product_a"]
        total_b += sale["product_b"]
        total_c += sale["product_c"]
    highest = total_a
    best_prod = "product_a"
    if total_b > highest:
        highest = total_b
        best_product = "product_b"
    if total_c > highest:
        highest = total_c
        best_product = "product_c"
    return best_product


# Agrega una función para encontrar el día con las peores ventas
def worst_selling_day(data):
    low = data[0]["product_a"] + data[0]["product_b"] + data[0]["product_c"]
    worst_day = data[0]["day"]
    for sale in data:
        total_day = sale["product_a"]+sale["product_b"]+sale["product_c"]
        if total_day < low:
            low = total_day
            worst_day = sale["day"]
    return worst_day


# Ordena los días por ventas totales y muestra los 3 mejores.
def top_three_days(data):
    daily_totals = [(sale["day"], sale["product_a"] + sale["product_b"] + sale["product_c"]) for sale in data]
    daily_totals_copy = daily_totals[:]
    for i in range(len(daily_totals_copy)):
        for j in range(i + 1, len(daily_totals_copy)):
            if daily_totals_copy[j][1] > daily_totals_copy[i][1]:
                daily_totals_copy[i], daily_totals_copy[j] = daily_totals_copy[j], daily_totals_copy[i]
    top_3 = daily_totals_copy[:3]
    return top_3


# Calcula el rango (máximo - mínimo) de las ventas de un producto.
def min_max_product(data,product_key):
    min = data[0][product_key]
    max = 0
    for sale in data:
        if min > sale[product_key]:
            min = sale[product_key]
    for sale in data:
        if max < sale[product_key]:
            max = sale[product_key]
    return min, max



# Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest total sales:", top_product(sales_data))
# New funtions
print("Day with the lowest total sales:", worst_selling_day(sales_data))
print("Best sales days:", top_three_days(sales_data))
print("Minimum and maximun sales of product_b:", min_max_product(sales_data,"product_b"))