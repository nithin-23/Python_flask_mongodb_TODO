from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["SECRET_KEY"] = "ac1a44b0a0708f5d6ceb40b81df6ebe0a88e1e72"
app.config["MONGO_URI"] = "mongodb+srv://nithin:vCr0n5WVtHZgZ7vB9@cluster0.sfjud.mongodb.net/"

#setup mongodb
mongodb_client = PyMongo(app)
db = mongodb_client.db
 
 
from application import routes

