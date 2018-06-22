import time
import sys
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.error import HTTPError



menu='''
press 1 to check current date and time
press 2 to scan all your mac address in your current connected network
press 3 to shutdown your machine after 15 mins
press 4 to search something on google
press 5 to Logout your current machine
press 6 to shutdown all connected system in your network
press 7 to update status on facebook
press 8 to list ip address of a given website
'''
def cdatetime():

    print (time.ctime())
def connecter(link):

    try:

          html  = urlopen(link)
          return html.text
    except HTTPError as e:
            time.sleep(1)
            print("Trying to connect again")
            connecter(link)
            
def search_google():
    search_phrase = input("Enter the search phrase:")
    google_link =   "https://www.google.com/search?q="
    link    =   google_link+search_phrase
    html=connecter(link)
    print(html)
    
search_google()