import mysql.connector
#REVIEW METHODS
mydb = mysql.connector.connect(
    host='localhost',
    user='user',
    passwd='password',
    database='mydatabase',
    port=3000
    )


mycursor = mydb.cursor()
#Given an ItemID return a list of its reviews
def getReview(idnum):
    global mycursor
    sql = 'SELECT ItemName,Price,Seller,Type,AVGRating FROM Item WHERE ItemID = (%s)'
    val = (idnum,)
    mycursor.execute(sql,val)
    things = mycursor.fetchall()
    sql = 'SELECT * FROM Review WHERE ItemID = (%s)'    
    mycursor.execute(sql,val)
    result = mycursor.fetchall()
    things.append(result)
    return things

#Add a review
def addReview(rating,details,itemID,CustID,ReviewID):
    global mycursor
    sql = 'INSERT INTO Review (Rating,DetailedReview,ItemID,CustomerID,ReviewID) VALUES (%s,%s,%s,%s,%s)'
    val = (rating,details,itemID,CustID,ReviewID)
    mycursor.execute(sql,val)
    sql = 'SELECT AVGRating,NumReviews FROM Item WHERE ItemID = (%s)'
    val = (itemID,)
    mycursor.execute(sql,val)
    result = mycursor.fetchone()
    totalRating = result[0]*result[1]
    totalRating = totalRating + rating
    newAVG = totalRating / (result[1] + 1)
    sql = 'UPDATE Item SET AVGRating = (%s),NumReviews = (%s) WHERE ItemID = (%s)'
    val = (newAVG,result[1]+1,itemID)
    mycursor.execute(sql,val)
    mydb.commit()
    
#Returns a list of Items sorted by Rating
def getItemRating():
    global mycursor
    sql = 'SELECT ItemID,Type,ItemName,Price,Seller,Quantity,AVGRating FROM Item NATURAL JOIN Inventory ORDER BY AVGRating DESC '
    mycursor.execute(sql)
    return mycursor.fetchall()

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
    sql = 'INSERT INTO Item (Type,ItemName,ItemID,Price,Seller,AVGRating,NumReviews) VALUES (%s,%s,%s,%s,%s,%s,%s)'
    val = (itemtype, name, idnum, price,seller,0,0)
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
#Returns a list of tuples, Each Tuple is (ItemID,ItemType,ItemName,Price,Seller,Quantity,AVGRating)
def getItems():
    global mycursor
    mycursor.execute('SELECT ItemID,Type,ItemName,Price,Seller,Quantity,AVGRating FROM Item NATURAL JOIN Inventory')
    result = mycursor.fetchall()
    return result

#Given a ShoppingCart ID and a itemid and quantity
def insertShoppingCart(idnum, itemid,amount):
    global mycursor
    worked = True
    sql = 'SELECT Price FROM Item WHERE ItemID = (%s)'
    itemnum = (itemid,)
    mycursor.execute(sql,itemnum)
    result = mycursor.fetchone()
    price = result[0]
    sql = 'SELECT ItemID FROM ShoppingCart WHERE ShoppingCartID = (%s)'
    val = (idnum,)
    found = False
    mycursor.execute(sql,val)
    result = mycursor.fetchall()
    for x in result:
        if (x[0] == itemid):
            found = True
            break
    sql = 'SELECT Quantity FROM Inventory WHERE ItemID = (%s)'
    mycursor.execute(sql,itemnum)
    result = mycursor.fetchone()
    if (found):
        sql = 'SELECT ItemQuantity FROM ShoppingCart WHERE ItemID = (%s) AND ShoppingCartID = (%s)'
        val = (itemid,idnum)
        mycursor.execute(sql,val)
        curr = mycursor.fetchone()
        amount = amount + curr[0]
    if (result[0] < amount):
        amount = result[0]
        price = price * amount
        if(found):
            sql = 'UPDATE ShoppingCart SET ItemQuantity=(%s),TotalPrice=(%s) WHERE ItemID = (%s) AND ShoppingCartID = (%s)'
            val = (amount,price, itemid, idnum)
        else:
            sql = 'INSERT INTO ShoppingCart (TotalPrice,ShoppingCartID,ItemID,ItemQuantity) VALUES (%s,%s,%s,%s)'
            val = (price,idnum,itemid,amount)
        mycursor.execute(sql,val)
        worked = False
    else:
        price = price*amount
        if(found):
            sql = 'UPDATE ShoppingCart SET ItemQuantity=(%s),TotalPrice=(%s) WHERE ItemID = (%s) AND ShoppingCartID = (%s)'
            val = (amount,price, itemid, idnum)
        else:
            sql = 'INSERT INTO ShoppingCart (TotalPrice,ShoppingCartID,ItemID,ItemQuantity) VALUES (%s,%s,%s,%s)'
            val = (price,idnum,itemid,amount)
        mycursor.execute(sql,val)
    mydb.commit()
    return worked

#Given shoppingCart id gets a list of tuples of (TotalPrice,ItemID,Quantity,ItemName,Price)
def getShoppingCart(idnum):
    global mycursor
    sql = 'SELECT TotalPrice,ItemID,ItemQuantity FROM ShoppingCart WHERE ShoppingCartID = (%s)'
    val = (idnum,)
    mycursor.execute(sql,val)
    cartInfo = mycursor.fetchall()
    ids = []
    i = 0
    for x in cartInfo:
    	val = (x[1],)
    	sql = 'SELECT ItemName,Price FROM Item WHERE ItemID IN (%s)'
    	mycursor.execute(sql,val)
    	result = mycursor.fetchone()
    	cartInfo[i] = cartInfo[i] + result
    	i = i+1
    return cartInfo

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

#Given ShoppingCart id and itemID, removes that item from shoppingcart
def removeSinglefromShoppingCart(idnum,itemID):
    global mycursor
    sql = 'DELETE FROM ShoppingCart WHERE ShoppingCartID = (%s) AND itemID = (%s)'
    val = (idnum,itemID)
    mycursor.execute(sql,val)
    mydb.commit()
        
