from dotenv import load_dotenv
import os

load_dotenv()
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_DATABASE_URI_IN_FOLDER = os.getenv('SQLALCHEMY_DATABASE_URI_IN_FOLDER')