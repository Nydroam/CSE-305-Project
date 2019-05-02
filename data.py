import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='user',
    passwd='password',
    database='mydatabase'
    )


mycursor = mydb.cursor()
#Add item to inventory of the shop
def addItem(idnum,name,price,itemtype,seller,quantity):
    global mycursor
    mycursor.execute('SELECT ItemID FROM Item')
    result = mycursor.fetchall()
    for x in result:
        if (idnum == x[0]):
            return False
    sql = 'INSERT INTO Item (Type,ItemName,ItemID,Price,Seller) VALUES (%s,%s,%s,%s,%s)'
    val = (itemtype, name, idnum, price,seller)
    mycursor.execute(sql,val)
    sql = 'INSERT INTO Inventory(ItemID,Quantity) VALUES (%s,%s)'
    val = (idnum,quantity)
    mycursor.execute(sql,val)
    mydb.commit()
def deleteItem():
    global mycursor
    mycursor.execute('DELETE FROM Item')
    mydb.commit()
#Get a dictionary of items in the shop inventory
#Returns a list of tuples, Each Tuple is (ItemID,ItemType,ItemName,Price,Seller,Quantity)
def getItems():
    global mycursor
    mycursor.execute('SELECT * FROM Item NATURAL JOIN Inventory')
    result = mycursor.fetchall()
    return result

#def insertShoppingCart(
#addItem(1,'Cup',1.24,'Utensil','Mikes',3)
getItems()

