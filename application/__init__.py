# from flask import Flask
# from flask_pymongo import PyMongo

# # Create the Flask app
# app = Flask(__name__)   

# # Set up configuration
# app.config["SECRET_KEY"] = "ac1a44b0a0708f5d6ceb40b81df6ebe0a88e1e72"
# app.config["MONGO_URI"] = "mongodb+srv://nithin:p7LVO4RTQpkmOLUu@cluster0.sfjud.mongodb.net/"

# # Initialize PyMongo
# mongodb_client = PyMongo(app)
# db = mongodb_client.db

# # Import routes after initializing the app and db
# from application import routes


from flask import Flask
from flask_pymongo import PyMongo

# Create the Flask app
app = Flask(__name__)

# Set up configuration
app.config["SECRET_KEY"] = "ac1a44b0a0708f5d6ceb40b81df6ebe0a88e1e72"
app.config["MONGO_URI"] = "mongodb+srv://nithin:ulzoMk6fPef4SNfF@cluster0.sfjud.mongodb.net/"

# Initialize PyMongo
mongodb_client = PyMongo(app)

# Test MongoDB connection
try:
    # This will throw an exception if the connection is not successful
    mongodb_client.cx.server_info()
    print("MongoDB Connected")
    # Select the database
    db = mongodb_client.cx["todo_flask"]  # You can use 'mongodb_client.cx["<your_db>"]' if you want to explicitly select the database
except Exception as e:
    db = None
    print(f"MongoDB Connection Error: {e}")

# Import routes after initializing the app and db
from application import routes