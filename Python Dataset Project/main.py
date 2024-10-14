from customers import generate_customers
from products import initialize_products, calculate_prices
from orders import generate_orders
from save_to_excel import save_to_excel

location_data = {
    'USA': [('New York', 'NY'), ('Los Angeles', 'CA')],
    'Canada': [('Toronto', 'Ontario'), ('Vancouver', 'British Columbia')],
    'UK': [('London', 'Eng

base_shipping_fees = {'USA': 60, 'Canada': 45, 'UK': 40, 'Germany': 30, 'France': 20, 'Australia': 10}

# Generate Data
customers = generate_customers(location_data)
products, product_categories, product_skus = initialize_products()
retail_prices, production_costs = calculate_prices(products)
orders, shipping_details = generate_orders(customers, products, product_categories, product_skus, retail_prices, production_costs, base_shipping_fees)

# Save to Excel
save_to_excel(customers, orders, shipping_details)

# File End

# Hello world