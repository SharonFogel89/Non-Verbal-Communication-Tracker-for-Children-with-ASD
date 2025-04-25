from core.db_connection import get_connection

conn = get_connection()
print("Connection worked!!!")
conn.close()
