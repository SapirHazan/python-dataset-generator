import random

def initialize_products():
    products = {
        'Laptop': 700, 'Smartphone': 1500, 'Tablet': 400, 'Headphones': 200,
        'Monitor': 250, 'Camera': 450, 'Printer': 180, 'Keyboard': 130,
        'Mouse': 100, 'Speaker': 110, 'Router': 160, 'Smartwatch': 1000,
        'Game Console': 800, 'E-book Reader': 150, 'Portable Speaker': 120
    }

    product_categories = {
        'Laptop': 'Computers', 'Tablet': 'Computers', 'Keyboard': 'Computers', 'Mouse': 'Computers', 'Monitor': 'Computers',
        'Smartphone': 'Mobile Devices', 'Smartwatch': 'Wearable Technology', 'E-book Reader': 'Mobile Devices',
        'Headphones': 'Audio Equipment', 'Speaker': 'Audio Equipment', 
        'Camera': 'Cameras', 'Printer': 'Computer Peripherals', 'Game Console': 'Gaming Devices', 'Router': 'Networking Devices',
        'Portable Speaker': 'Audio Equipment'
    }

    product_skus = {product: f"{product[:3].upper()}-{random.randint(1000000000, 9999999999)}" for product in products}

    return products, product_categories, product_skus

def calculate_prices(products, years=[2020, 2021, 2022, 2023]):
    retail_prices = {year: {} for year in years}
    production_costs = {year: {} for year in years}

    # Set initial prices for 2020
    for product, price in products.items():
        retail_prices[2020][product] = price
        production_costs[2020][product] = price * random.uniform(0.7, 0.9)

    # Calculate prices for subsequent years with controlled growth
    for year in range(2021, 2024):
        for product in products:
            last_year_retail = retail_prices[year - 1][product]
            last_year_production = production_costs[year - 1][product]
            
            # Increase the retail price by 5% to 10% each year
            growth_rate_retail = random.uniform(0.05, 0.10)
            new_retail_price = last_year_retail * (1 + growth_rate_retail)
            
            # Increase the production cost by 5% to 10% each year, ensuring it's lower than retail price
            growth_rate_production = random.uniform(0.05, 0.10)
            new_production_cost = last_year_production * (1 + growth_rate_production)
            
            if new_production_cost >= new_retail_price:
                new_production_cost = new_retail_price * random.uniform(0.7, 0.9)
            
            retail_prices[year][product] = round(new_retail_price, 2)
            production_costs[year][product] = round(new_production_cost, 2)

            print(f"Year {year}, Product {product}: Retail Price = {new_retail_price:.2f}, "
                  f"Production Cost = {new_production_cost:.2f}, Retail Growth = {growth_rate_retail:.2%}, "
                  f"Production Growth = {growth_rate_production:.2%}")

    return retail_prices, production_costs
