import mysql.connector
from faker import Faker
import datetime
import random

def main():
    #faker library for fake data
    fake = Faker()

    #database connection
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    auth_plugin="mysql_native_password"
    )

    mycursor = mydb.cursor()

    #creating database and selecting it to add data
    mycursor.execute("CREATE DATABASE deal_ordering_system")
    mycursor.execute("USE deal_ordering_system")

    #adding data on multiple table
    create_users(mydb, mycursor, fake)
    create_deals(mydb, mycursor)
    create_orders(mydb, mycursor)
    create_order_items(mydb, mycursor)

    # mycursor.execute("DROP DATABASE IF EXISTS deal_ordering_system")
    print(mydb) 

def create_users(mydb, mycursor, fake):
    #creating users and adding 1001 users
    mycursor.execute("CREATE TABLE users (id int NOT NULL AUTO_INCREMENT, first_name VARCHAR(255), last_name VARCHAR(255), email VARCHAR(255), PRIMARY KEY(id))")
    sql = "INSERT INTO users (first_name, last_name, email) VALUES(%s, %s, %s)"
    values = [('Suman', 'Koirala', 'suman.koirala.1@ndsu.edu')]
    for i in range(1000):
        values.append((fake.first_name(), fake.last_name(), fake.email()))
    mycursor.executemany(sql, values)
    mydb.commit()

def create_deals(mydb, mycursor):
    #creating deals table and adding 10 deal records
    mycursor.execute("CREATE TABLE deals (id int NOT NULL AUTO_INCREMENT, name VARCHAR(255), price int, PRIMARY KEY(id))")
    sql = "INSERT INTO deals (name, price) VALUES(%s, %s)"
    values = [("The Finest Coffee Deal", 1000),
    ("All Winter Ski Deal", 3000),
    ("Hawaii Cruise 3 Weeks", 1500000),
    ("Napa Trip", 200000),
    ("Unlimited Oil Change", 2500),
    ("Watch", 4500),
    ("Car Wash", 1000),
    ("Every Morning Doughnut", 1000),
    ("Friday Morning Zoo Visit", 400),
    ("Movie Ticket", 700)
    ]
    mycursor.executemany(sql, values)
    mydb.commit()

def create_orders(mydb, mycursor):
    #creating orders and adding 1 order for all users
    mycursor.execute("CREATE TABLE orders (id int NOT NULL AUTO_INCREMENT, user_id int, date DATE, PRIMARY KEY(id), FOREIGN KEY(user_id) REFERENCES users(id))")
    mycursor.execute("SELECT id FROM users")
    user_ids = mycursor.fetchall()
    sql = "INSERT INTO orders (user_id, date) VALUES(%s, %s)"
    values = []
    for items in user_ids:
        values.append((items[0], random_date()))
    mycursor.executemany(sql, values)
    mydb.commit()


def create_order_items(mydb, mycursor):
    #creating order items and adding order items for each order and referencing them to orders
    mycursor.execute("CREATE TABLE order_items (id int NOT NULL AUTO_INCREMENT, order_id int, deal_id int, PRIMARY KEY(id), FOREIGN KEY(order_id) REFERENCES orders(id), FOREIGN KEY(deal_id) REFERENCES deals(id))")
    mycursor.execute("SELECT id FROM orders")
    order_ids = mycursor.fetchall()
    sql = "INSERT INTO order_items (order_id, deal_id) VALUES(%s, %s)"
    values = []
    for items in order_ids:
        values.append((items[0], random.randrange(1,11)))
    mycursor.executemany(sql, values)
    mydb.commit()

def random_date():
    start_date = datetime.date(2000, 1, 1)
    end_date = datetime.date(2020, 2, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date.strftime("%Y-%m-%d")


if __name__ == "__main__":
    main()
