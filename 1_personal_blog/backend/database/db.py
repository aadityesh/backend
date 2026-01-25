from mongoengine import connect
from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv("MONGODB_URL"))


def init_db():
    connect(
        db='blog_app',
        host=os.getenv("MONGODB_URL"))
