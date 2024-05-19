"""
main.py file used as the main entry point for the program

######kindly use your own api key nd text file for input 
"""


from IPython.display import Markdown 
import os 
from dotenv import load_dotenv
from model import sentiment_analyser

load_dotenv()

def main():
  with open ("input.txt","r") as f :
   reviews = f.read()
  
  
  response= sentiment_analyser(reviews)
  print("starting the process")
  Markdown(response)

if __name__=="__main___":
  main()
