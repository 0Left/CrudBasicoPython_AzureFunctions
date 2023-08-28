from dotenv import load_dotenv
import os
import pymongo


def load_connection():
    load_dotenv()
    connection_string = os.environ.get("connection_string")
    client = pymongo.MongoClient(connection_string)
    return client

def get_collection():
    client = load_connection()
    return client.get_database("baseCollection").get_collection("baseCollection")

basicCollection = get_collection()