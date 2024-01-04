from dotenv import load_dotenv
import os
import pyodbc

load_dotenv()

server = os.getenv("AZURE_SERVER")
port = 1433
user = os.getenv("AZURE_ID")
password = os.getenv("AZURE_PASSWORD")
database = 'finaldatabase'

# Build connection string
conn_str = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={user};PWD={password}"
def conn():
    try:
        # Create a connection
        with pyodbc.connect(conn_str, timeout=15) as conn:
            return conn

    except pyodbc.Error as ex:
        sqlstate = ex.args[1]
        return f"Error connecting to the database. SQLState: {sqlstate}"
    
def requestDonorListFromDatabase(branch_name):
    # First get branch city
    # Then use this city to take donor_list in the city
    connection = conn()
    cursor = connection.cursor()

    cursor.execute("SELECT city FROM Users WHERE username = ?",(branch_name,))

    city = cursor.fetchone()
    # It returns tuple take first element
    city = city[0]
    cursor.execute("SELECT donor_name FROM Donors WHERE city = ?",(city,))
    donor_list = cursor.fetchall()
    # It returns list of tuple take first element
    donor_list = [donor[0] for donor in donor_list]
    
    return donor_list