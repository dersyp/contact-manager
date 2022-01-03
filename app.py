from flask import Flask
from database import DatabaseManager

app = Flask(__name__)

from views import *

if __name__ == '__main__':
    database = DatabaseManager("contact.db")
    database.create_database()
    database.connexion.close()
    app.run(debug=True, host='127.0.0.2', port=9000)
