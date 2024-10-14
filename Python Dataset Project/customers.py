import random  # Add this import statement
from faker import Faker
from data_generation import format_phone_number

faker = Faker()

def generate_customers(location_data, num_customers=5000):
    customers = []
    customer_ids = set()
    while len(customers) < num_customers:
        customer_id = random.randint(100000000, 999999999)
        if customer_id not in customer_ids:
            country = random.choice(list(location_data.keys()))
            city, state = random.choice(location_data[country])
            customer = {
                'CustomerID': customer_id,
                'CustomerName': faker.name(),
                'PhoneNumber': format_phone_number(),
                'Address': faker.street_address(),
                'City': city,
                'State': state,
                'Country': country
            }
            customers.append(customer)
            customer_ids.add(customer_id)
    return customers
