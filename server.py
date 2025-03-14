from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

app = Flask(__name__)
mysql = MySQL(app)

load_dotenv()

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')




if __name__ == '__main__':
    app.run(port=5000, debug=True)