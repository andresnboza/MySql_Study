import random
from faker import Faker
import datetime
import mysql.connector  # MySQL connector to connect to the DB

# Create an instance of the Faker library to generate fake data
fake = Faker()

# Set the number of additional orders per user
additional_orders = 50

# Define possible statuses for the orders
order_statuses = ['Processing', 'Shipped', 'Delivered', 'Cancelled']

# Assume there are 100 users (user IDs 1 to 100)
total_users = 100

# Helper function to generate a random order date
def random_order_date():
    start_date = datetime.date(2015, 1, 1)
    end_date = datetime.date.today()
    return fake.date_between(start_date=start_date, end_date=end_date)

# Connect to the MySQL database running inside Docker
connection = mysql.connector.connect(
    host='127.0.0.1',   # or the name of the MySQL service in the Docker network
    port=3306,          # The exposed port from the container
    user='myuser',      # The MySQL user
    password='mypassword',  # The MySQL password
    database='mydatabase'   # The MySQL database name
)

cursor = connection.cursor()

# Generate and insert additional random orders for users
for user_id in range(1, total_users + 1):
    for _ in range(additional_orders):
        order_date = random_order_date()
        order_amount = round(random.uniform(20.00, 500.00), 2)
        shipping_address = fake.address().replace('\n', ', ')
        status = random.choice(order_statuses)
        
        # Insert the order into the Orders table
        sql = """
        INSERT INTO Orders (UserID, OrderDate, OrderAmount, ShippingAddress, Status) 
        VALUES (%s, %s, %s, %s, %s);
        """
        # values = (user_id, order_date, order_amount, shipping_address, status)
        
        # cursor.execute(sql, values)

        print(sql)

# Commit the transaction to make the changes in the database
# connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

print(f"Successfully inserted {additional_orders * total_users} random orders into the database.")
