import mysql.connector
from mysql.connector import Error 
from dotenv import load_dotenv 
import os 

load_dotenv()

DB_CONFIG = {
    'host': os.getenv("MYSQL_LOCALHOST"),
    'port': int(os.getenv("MYSQL_PORT")),
    'user': os.getenv("MYSQL_USER"),
    'password': os.getenv("MYSQL_PASSWORD"),
    'database': os.getenv("MYSQL_DATABASE") 
}

def get_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print(f"Error: {e}")
        return None

def get_compra():
    try:
        #lo primero crear la conexion
        conn = get_connection()
        cursor = conn.cursor(dictionary=True) 
        cursor.execute('SELECT * FROM productos')
        return cursor.fetchall() 
    except Error as e:
        print (f"Error {e}")
    finally:
        conn.close()
result = get_compra()
print(result)



