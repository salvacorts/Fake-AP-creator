import os
import time

# Main
def main():
  os.system("clear")
  os.system("cat install/distros/banner.txt")
  option = input("\nContinue?(y/n) --> ") #Accept
  if option == "y":
    os.system("clear")
    print("Installing!")
    os.system("yum install -y aircrack-ng") # Install Aircrack!
    os.system("yum install -y dhcp") # Install DHCP server!
    os.system("yum install -y dnsmasq") # Install DNS server!
    os.sysytem("yum install -y dsniff") # Install Dsniff!
    os.system("clear")
    print("Everything is installed!")
    time.sleep(1)
    os.system("python main.py")
  elif option == "n": # Go back!
    os.system("clear")
    print("Back to menu")
    time.sleep(1)
    os.system("clear")
    os.system("python main.py")
  else:
    os.system("clear")
    print("Yes(y) or No(n).")
    time.sleep(1)
    main()

# noRoot
def noroot():
  os.system("clear")
  print("RUN AS ROOT!")
  time.sleep(2)
  exit()

# Root verification
root = os.geteuid()
if root == 0:
  main()
else:
  noroot()
