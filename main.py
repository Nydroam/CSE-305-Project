import data
import mysql.connector
from flask import request, url_for
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

mydb = mysql.connector.connect(
    host='localhost',
    user='user',
    passwd='password',
    database='mydatabase'
    )

mycursor = mydb.cursor()

@app.route("/listing")
def listing():
    """
    Gets items from database
    """
    items = data.getItems()
    print(items)
    return items

if __name__ == "__main__":
    app.run(debug = True)
