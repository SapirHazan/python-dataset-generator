import random
import pandas as pd  # Add this import statement
from datetime import timedelta
from data_generation import random_dates

def generate_orders(customers, products, product_categories, product_skus, retail_prices, production_costs, base_shipping_fees, years=[2020, 2021, 2022, 2023]):
    orders = []
    shipping_details = []
    order_ids = set()  # Track all generated OrderIDs

    for year in years:
        for customer in customers:
            product = random.choice(list(products.keys()))
            date = random_dates(pd.to_datetime(f'{year}-01-01'), pd.to_datetime(f'{year}-12-31'), 1)[0]

            # Generate a unique OrderID
            while True:
                order_id = f"{customer['Country'][:2].upper()}-{random.randint(10000, 99999)}"
                if order_id not in order_ids:
                    order_ids.add(order_id)
                    break

            quantity = random.randint(1, 6)
            shipping_fee = base_shipping_fees[customer['Country']] + (year - 2020) * 5

            orders.append({
                'OrderDate': date, 'OrderID': order_id, 'CustomerID': customer['CustomerID'],
                'Product': product, 'ProductCategory': product_categorie

    return orders, shipping_details
