import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host='localhost',  # change if needed
        user='root',
        password='Tejas@789$',
        database='db'
    )
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM office;")  # Change 'office' to your table name
        rows = cursor.fetchall()
        
        for row in rows:
            print(row)
        cursor.close()

except Error as e:
    print("Error:", e)

finally:
    if conn.is_connected():
        conn.close()
        print("Connection closed.")
