from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables

app = Flask(__name__)

# Configure MongoDB
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

# Test MongoDB connection
try:
    mongo.db.command('ping')  # Simple command to test connection
    print("✅ Connected to MongoDB successfully!")
except Exception as e:
    print("❌ Failed to connect to MongoDB:", e)

@app.route('/')
def home():
    return "MongoDB Connected Successfully!"

if __name__ == '__main__':
    app.run(debug=True)