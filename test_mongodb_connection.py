import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables
load_dotenv()

def test_mongodb_connection():
    try:
        # Get connection string from environment
        mongo_uri = os.getenv("MONGO_URI")
        
        if not mongo_uri:
            print("❌ MONGO_URI not found in .env file")
            return False
            
        print(f"🔗 Connecting to MongoDB Atlas...")
        print(f"📡 URI: {mongo_uri.split('@')[1]}")  # Show only cluster part for security
        
        # Create client
        client = MongoClient(mongo_uri)
        
        # Test connection
        client.admin.command('ping')
        print("✅ Successfully connected to MongoDB Atlas!")
        
        # List databases
        databases = client.list_database_names()
        print(f"📊 Available databases: {databases}")
        
        # Test your specific database
        db_name = mongo_uri.split('/')[-1].split('?')[0]
        db = client[db_name]
        
        # Test collection access
        collections = db.list_collection_names()
        print(f"📁 Collections in {db_name}: {collections}")
        
        client.close()
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    test_mongodb_connection() 