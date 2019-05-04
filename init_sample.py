import data
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='user',
    passwd='password',
    database='mydatabase',
    port=3000
    )
mycursor = mydb.cursor()

data.addItem(111, "Toothpaste", 4.55, "Personal Care", "Colgate", 103)
data.addItem(290, "Mouthwash", 6.57, "Personal Care", "Listerine", 247)
data.addItem(424, "Pencil", 1.99, "Office Supplies", "Dixon", 2836)
data.addItem(456, "Stapler", 5.99, "Office Supplies", "Swingline", 517)
