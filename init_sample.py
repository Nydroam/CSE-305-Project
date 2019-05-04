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
data.addItem(304, "Paper Clips (600)", 9.59, "Office Supplies", "JPSOR", 400) 
data.addItem(444, "Shampoo", 10.86, "Personal Care", "Pantene", 234)
data.addItem(854, "Sorry!", 12.99, "Toys and Games", "Hasbro", 333)
data.addItem(865, "Jenga", 14.99, "Toys and Games", "Jenga", 210)
data.addItem(802, "Teddy Bear", 10.99, "Toys and Games", "WILDREAM", 89)
data.addItem(335, "Why My Cat Is More Impressive Than Your Baby", 9.55, "Books", "The Oatmeal",52)
data.addItem(760, "Oh the Places You'll Go!", 10.78, "Books", "Dr. Seuss", 7516)
data.addItem(703, "The Very Hungry Caterpillar", 8.91, "Books", "Eric Carle", 5897)
data.addItem(1234, "16 GB USB 3.0 Flash Drive", 14.99, "Electronics", "SanDisk", 3494)
data.addItem(1223, "64 GB USB 2.0 Flash Drive", 39.99, "Electronics", "SanDisk", 17683)
data.addItem(1210, "32 GB USB 3.0 Flash Drive", 24.99, "Electronics", "Samsung", 5069)
print(data.getItems())
data.addReview(3,'test',456,1,1)
data.addReview(4,'test',456,1,2)
data.addReview(2,'test',304,1,3)
data.addReview(1,'test',1234,1,4)
data.addReview(1,'test',1210,1,5)
data.addReview(5,'test',111,1,6)
data.addReview(4,'test',1234,1,7)
data.addReview(3,'test',1223,1,8)
data.addReview(4,'test',335,1,9)
print(data.getItemRating())
