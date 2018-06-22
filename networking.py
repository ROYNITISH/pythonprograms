import subprocess
from urllib.request import urlopen
from urllib.error import URLError
import webbrowser
def cable_checker():
    ls_output=(subprocess.check_output("ls /sys/class/net".split()))
    ls_output=(ls_output.decode('utf-8'))

    if(ls_output.__contains__("enp0s")):
        return True
    else:
        return False

#print(cable_checker())

def internet_checker():
    try:

        urlopen("http://www.google.com",timeout=1)
        return True

    except URLError as e:

        return False


def open_google():
    webbrowser.open("http://www.google.com",new=2)
#open_google()


str='''
1.Enter 1 to check ethernet-cable plugged or not
2.Enter 2 to check Internet Connectivity
3.Enter 3 to open google in a browser
4.Check just connectivity
'''
print(str)

choice=int(input("Enter the choice"))
if choice == 1:
    if cable_checker():
        print("Yes,Wire plugged in")
    else:
        print("No!!,Connect Ethernet")
elif choice == 2:
    if cable_checker():
        if internet_checker():
            print("Internet is on..")
        else:
            print("You are offline..")
    else:
        print("No source for the internet")
elif choice == 3:
    if internet_checker() and cable_checker():
        open_google()
    else:
        print("Computer offline")
elif choice == 4:
    print(internet_checker())



