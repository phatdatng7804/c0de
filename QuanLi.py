import pyodbc 
import pandas as pd 
server = 'PHATDAT'
database = 'QuanLi'
username = ''
password = ''

connection_String = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};password={password}'

try: 
    conn = pyodbc.connect(connection_String)
    query = 'SELECT * FROM users'
    df_sanpham = pd.read_sql(query,conn)
    print(df_sanpham.head())
except pyodbc.Error as e:
    print(f'Error: {e}')
finally:
    if 'conn' in locals() and conn:
        conn.close()