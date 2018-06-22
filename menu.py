#!/usr/bin/python2
import sys
import time
import BeautifulSoup
import urllib 
import webbrowser
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
choice = int(raw_input("Enter your choice\n"))

def cdatetime():

    print time.ctime()

def search_google():
    search_phrase=raw_input("Enter the search phrase:")
    google_link =   "https://www.google.com/search?q="
    link    =   google_link+search_phrase
    html=urllib.urlopen(link)
    #print html.read()
    
    print html

    
    webbrowser.open_new_tab(link)
    sys.exit()
    # html = urllib.urlopen(google_link+search_phrase)
    # soup = BeautifulSoup(html,"lxml")
    # for link in soup.find_all('a'):
    #     content = links.get('href')
    #     if(content.__contains__('youtube')):
    #         webbrowser.open_new_tab(content)
    #     break



if choice == 1:
    cdatetime()
if choice == 4:
    search_google()