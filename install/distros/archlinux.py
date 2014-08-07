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
    os.system("pacman -S aircrack-ng") # Install Aircrack!
    os.system("pacman -S dhcp") # Install DHCP server!
    os.system("pacman -S dnsmasq") # Install DNS server!
    os.system("pacman -S dsniff") # Install Dsniff!
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
