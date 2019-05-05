import data
import mysql.connector
from flask import request, url_for
from flask_api import FlaskAPI
from flask_cors import CORS

app = FlaskAPI(__name__)
CORS(app)

mydb = mysql.connector.connect(
    host='localhost',
    user='user',
    passwd='password',
    database='mydatabase',
    port = 3000
    )

mycursor = mydb.cursor()

@app.route("/listing")
def listing():
    """
    Gets items from database
    """
    items = data.getItems()
    cart = data.getShoppingCart(1)
    print(cart)
    #print(items)
    return items

@app.route("/popular")
def popular():
    """
    Gets items from database sorted by popularity
    """
    items = data.getItemRating()
    print(items)
    return items

@app.route("/addcart", methods =['POST'])
def addcart():
    """
    Adds items to shopping cart
    """
    d = request.data
    for key in d.keys():
        val = d[key]
        if val > 0:
            data.insertShoppingCart(1,int(key),val)
    return ""

@app.route("/cart")
def cart():
    """
    Gets items from shopping cart
    """
    cart = data.getShoppingCart(1)
    print(cart)
    return cart

@app.route("/purchase")
def purchase():
    """
    Purchases items from shopping cart
    """
    cart = data.getShoppingCart(1)
    print(cart)
    for items in cart:
        data.updateStock(items[2],-1*items[3])
    return ""
        
@app.route("/review/<int:idnum>")
def review(idnum):
    """
    Gets review of an item given id
    """
    reviews = data.getReview(idnum)
    print(reviews)
    return reviews

if __name__ == "__main__":
    app.run(debug = True)
