# Python Dataset Project

This project generates a dataset of customer orders with product, customer, and shipping details, saving everything in an Excel file prepared for analysis in **Power BI**.

## 📂 Project Structure

- **main.py**  
  The main script that runs the entire data generation process and saves it in Excel. It calls functions from `customers.py`, `products.py`, `orders.py`, and `save_to_excel.py`.  
  **Output**: An Excel file with multiple sheets.

- **customers.py**  
  Generates customer data, including ID, name, phone number, address, city, state, and country.  
  Uses the **Faker** library to create random customer data.

- **products.py**  
  Defines products, categories, and SKUs for each product.  
  Includes the `calculate_prices` function to set prices per year, with both retail and production costs for each product.

- **orders.py**  
  Creates order data for each customer: order date, order ID, product type, price, production cost, quantity, and shipping fee.

- **save_to_excel.py**  
  Saves all generated data into an Excel file with separate sheets for **Customers**, **Orders**, and **Shipping**.  
  **Default Location**: `Documents/PBI_Dataset.xlsx`.

## 📦 Required Packages

- **Faker**: For generating customer data.
- **pandas**: For processing and saving the data in Excel.
- **openpyxl**: Required for saving data in Excel format.
