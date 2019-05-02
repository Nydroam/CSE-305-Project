import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='SeanChu',
    passwd='Rimewind13',
    )


mycursor = mydb.cursor()
def makeTables():
    global mycursor
    #mycursor.execute('CREATE TABLE Item ( Type CHAR(50), ItemName CHAR(50), ItemID INTEGER, Price FLOAT, Seller CHAR(50), PRIMARY KEY(ItemID))')
    mycursor.execute('CREATE TABLE Customer( CustomerID INTEGER, FirstName CHAR(50), LastName CHAR(50), Email CHAR(50), Phone CHAR(10), Address CHAR(50), PRIMARY KEY (CustomerID))')
    mycursor.execute('CREATE TABLE Payment( PaymentType CHAR(20), CardNumber INTEGER, CardExpiryDate DATE, ShoppingCartID INTEGER, PRIMARY KEY(CardNumber,ShoppingCartID))')
    mycursor.execute('CREATE TABLE Inventory(ItemID INTEGER, Quantity INTEGER, PRIMARY KEY (ItemID))')
    mycursor.execute('CREATE TABLE Shipment( ShipmentID INTEGER, ShipmentDetail CHAR(50), ShipmentType CHAR(20), DeliveryAddress CHAR(50), ShipmentCharge FLOAT, PRIMARY KEY(ShipmentID))')
    mycursor.execute('CREATE TABLE Employee( Designation CHAR(20), DateJoined DATE, FirstName CHAR(50), LastName CHAR(50), Email CHAR(50), Phone CHAR(10), Address CHAR(50), EmployeeID INTEGER, SupervisorID INTEGER, PRIMARY KEY (EmployeeID))')
    mycursor.execute('CREATE TABLE Review (Rating FLOAT, DetailedReview CHAR(50), ItemID INTEGER, SellerID INTEGER, CustomerID INTEGER, ReviewID INTEGER, PRIMARY KEY(ReviewID))')
    mycursor.execute('CREATE TABLE ShoppingCart( TotalPrice FLOAT, ShoppingCartID INTEGER, ItemID INTEGER, ItemQuantity INTEGER, PRIMARY KEY(ShoppingCartID,ItemID))')
    '''
    Relational TABLES
    mycursor.execute('CREATE TABLE Manages(EmployeeID INTEGER, ItemID INTEGER, PRIMARY KEY(EmployeeID, ItemID))')
    mycursor.execute('CREATE TABLE Supervises(SuperID INTEGER, SupervisedID INTEGER, PRIMARY KEY(SuperID,SupervisedID))')
    mycursor.execute('CREATE TABLE ProducesA(CardNumber INTEGER, ShoppingCartID INTEGER, ShipmentID INTEGER, PRIMARY KEY (CardNumber,ShoppingCartID,ShipmentID))')
    mycursor.execute('CREATE TABLE MakesA(CustomerID INTEGER, ShipmentID INTEGER, PRIMARY KEY (CustomerID,ShipmentID))')
    mycursor.execute('CREATE TABLE Gives(CustomerID INTEGER, ReviewID INTEGER, PRIMARY KEY(CustomerID, ReviewID))')
    mycursor.execute('CREATE TABLE ItemHasAReview(ItemID INTEGER, ReviewID INTEGER, PRIMARY KEY(ItemID,ReviewID))')
    '''
def makeKeyConstraints():
    mycursor.execute('ALTER TABLE Inventory ADD CONSTRAINT FOREIGN KEY (ItemID) REFERENCES Item(ItemID) ON DELETE CASCADE ON UPDATE CASCADE')
    mycursor.execute('ALTER TABLE Payment ADD CONSTRAINT FOREIGN KEY (ShoppingCardID) REFERENCES ShoppingCart(ShoppingCartID) ON DELETE CASCADE ON UPDATE CASCADE ')
    mycursor.execute('ALTER TABLE Review ADD CONSTRAINT FOREIGN KEY (ItemID) REFERENCES Item(ItemID) ON DELETE CASCADE ON UPDATE CASCADE')
    mycursor.execute('ALTER TABLE Review ADD CONSTRAINT FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID) ON DELETE SET NULL ON UPDATE CASCADE ')
    mycursor.execute('ALTER TABLE ShoppingCart ADD CONSTRAINT FOREIGN KEY (ItemID) REFERENCES Item(ItemID) ON DELETE CASCADE ON UPDATE CASCADE')
    '''
    Relational TABLES
    mycursor.execute('ALTER TABLE Manages ADD CONSTRAINT FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID) ON DELETE CASCADE ON UPDATE CASCADE')
    mycursor.execute('ALTER TABLE Manages ADD CONSTRAINT FOREIGN KEY (ItemID) REFERENCES Item(ItemID) ON DELETE CASCADE ON UPDATE CASCADE ')
    mycursor.execute('ALTER TABLE Supervises ADD CONSTRAINT FOREIGN KEY (SuperID) REFERENCES Employee(SupervisorID) ON DELETE CASCADE ON UPDATE CASCADE')
    mycursor.execute('ALTER TABLE Supervises ADD CONSTRAINT FOREIGN KEY (SupervisedID) REFERENCES Employee(EmployeeID) ON DELETE CASCADE ON UPDATE CASCADE ')
    mycursor.execute('ALTER TABLE ProducesA ADD CONSTRAINT FOREIGN KEY (CardNumber,ShoppingCartID) REFERENCES PAYMENT(CardNumber,ShoppingCartID) ON DELETE CASCADE ON UPDATE CASCADE ')
    mycursor.execute('ALTER TABLE ProducesA ADD CONSTRAINT FOREIGN KEY (ShipmentID) REFERENCES Shipment(ShipmentID) ON DELETE CASCADE ON UPDATE CASCADE')
    ''' 

#Run once to initalize database
def init():
    global mycursor
    mycursor.execute('CREATE DATABASE mydatabase')
    makeTables()
    makeKeyConstraints
init()
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
