import pandas as pd

def save_to_excel(customers, orders, shipping_details, output_path='C:/Users/Matan/Desktop/Code/Python Dataset Project/PBI_Dataset.xlsx'):
    df_customers = pd.DataFrame(customers)
    df_orders = pd.DataFrame(orders)
    df_shipping = pd.DataFrame(shipping_details)
    
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        df_customers.to_excel(writer, sheet_name='Customers', index=False)
        df_orders.to_excel(writer, sheet_name='Orders', index=False)
        df_shipping.to_excel(writer, sheet_name='Shipping', index=False)

    print("Data organized into multiple sheets and saved to", output_path)
