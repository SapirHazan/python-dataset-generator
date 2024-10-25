Python Dataset Project
הפרויקט הזה מייצר סט נתונים של הזמנות לקוחות עם פרטי מוצרים, לקוחות ומשלוח, ושומר את הכל בקובץ אקסל המוכן לניתוח ב-Power BI.

📂 מבנה הפרויקט
main.py
הסקריפט הראשי שמריץ את כל תהליך יצירת הנתונים ושמירתם באקסל. מפעיל את הפונקציות מתוך customers.py, products.py, orders.py, ו-save_to_excel.py.
פלט: קובץ אקסל עם מספר גיליונות.

customers.py
מייצר נתוני לקוחות: מזהה לקוח, שם, טלפון, כתובת, עיר, מדינה וארץ.
משתמש בספרייה Faker כדי ליצור נתוני לקוחות אקראיים.

products.py
מגדיר מוצרים, קטגוריות, ו-SKU עבור כל מוצר.
כולל את הפונקציה calculate_prices לקביעת מחירים לפי שנים, כולל מחיר ייצור ומחיר קמעונאי לכל מוצר.

orders.py
יוצר נתוני הזמנות עבור כל לקוח: תאריך הזמנה, מזהה הזמנה, סוג מוצר, מחיר, עלות ייצור, כמות ומחיר משלוח.

save_to_excel.py
שומר את כל הנתונים שנוצרו בקובץ אקסל עם גיליונות נפרדים ללקוחות, הזמנות ופרטי משלוח.
מיקום ברירת מחדל: C:/Users/Matan/Desktop/Code/Python Dataset Project/PBI_Dataset.xlsx.

📦 התקנת חבילות נדרשות
Faker: להפקת פרטי לקוחות
pandas: לעיבוד ושמירה של הנתונים באקסל
openpyxl: שמירה בפורמט אקסל

הערה: אפשר לשנות את המיקום של הקובץ שנשמר בערך output_path ב-save_to_excel.py אם רוצים לשמור במקום אחר.