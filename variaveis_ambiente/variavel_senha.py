# !pip install python-dotenv

from dotenv import load_dotenv
import os

load_dotenv()

# print(os.environ)
print(os.getenv('BD_PASSWORD'))