from IPython.display import Markdown 
import os 
from dotenv import load_dotenv
from model import sentiment_analyser

load_dotenv()


with open ("input.txt","r") as f :
  reviews = f.read()
  
  
response= sentiment_analyser(reviews)
print("starting the process")
Markdown(response)