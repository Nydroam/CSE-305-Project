import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='user',
    passwd='password',
    database='mydatabase',
    port=3000
    )


mycursor = mydb.cursor()
#Given an ItemID and a number, updates the quantity in Inventory of that item
def updateStock(idnum,change):
    global mycursor
    sql = 'SELECT Quantity FROM Inventory WHERE ItemID = (%s)'
    val = (idnum,)
    mycursor.execute(sql,val)
    result = mycursor.fetchone()
    sql = 'UPDATE Inventory SET Quantity = (%s) WHERE ItemID = (%s)'
    newQuant = result[0] + change
    val = (newQuant,idnum)
    mycursor.execute(sql,val)
    mydb.commit()
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
#Given a ShoppingCart ID and a dictionary of ItemID:Quantity
def insertShoppingCart(idnum, items):
    global mycursor
    prices = []
    for x in items:
        sql = 'SELECT Price FROM Item WHERE ItemID = (%s)'
        itemnum = (x,)
        mycursor.execute(sql,itemnum)
        result = mycursor.fetchone()
        price = result[0] * items[x]
        prices.append(price)
    i = 0
    for y in prices:
        sql = 'INSERT INTO ShoppingCart (TotalPrice,ShoppingCartID,ItemID,ItemQuantity) VALUES (%s,%s,%s,%s)'
        key = (list)(items.keys())[i]
        val = (y,idnum,key,items[key])
        mycursor.execute(sql,val)
    mydb.commit()
#Given shoppingCart id gets a list of tuples of (TotalPrice,ShoppingCartID,ItemID,Quantity)
def getShoppingCart(idnum):
    global mycursor
    sql = 'SELECT * FROM ShoppingCart WHERE ShoppingCartID = (%s)'
    val = (idnum,)
    mycursor.execute(sql,val)
    result = mycursor.fetchall()
    return result
#Given Shoppingcart id, removes all entries with that id from shoppingCart, then updates Inventory
def removeShoppingCart(idnum):
    global mycursor
    sql = 'SELECT ItemID,ItemQuantity FROM ShoppingCart WHERE ShoppingCartID = (%s)'
    val = (idnum,)
    mycursor.execute(sql,val)
    purchased = mycursor.fetchall()
    sql = 'DELETE FROM ShoppingCart WHERE ShoppingCartID = (%s)'
    mycursor.execute(sql,val)
    for x in purchased:
        sql = 'SELECT Quantity FROM Inventory WHERE ItemID =(%s) '
        val = (x[0],)
        mycursor.execute(sql,val)
        currQ = mycursor.fetchone()
        newQ = currQ[0] - x[1]
        sql = 'UPDATE Inventory SET Quantity = (%s) WHERE ItemID = (%s)'
        val = (newQ,x[0])
        mycursor.execute(sql,val)
    mydb.commit()
        

