import os
import time

# banner
def banner():
  os.system("clear")
  os.system("cat banner.txt")
  time.sleep(2)
  mainWindow()

# mainWindow
def mainWindow():
  os.system("clear")
  os.system("cat mainWindow.txt")
  option = input("\nOption?(1/2/3) --> ")
  if option == "1":
    # Execute installation script!
    os.system("clear")
    os.system("python install/main.py")
  elif option == "2":
    # Continue FakeAP creation!
    os.system("clear")
    os.system("python creator/main.py")
  elif option == "3":
    # Exit!
    os.system("clear")
    print("HAPPY HACKING!")
    time.sleep(1)
    os.system("clear")
    exit()
  else:
    os.system("clear")
    print("Option 1, 2 or 3.")
    time.sleep(2)
    mainWindow()

# noRoot
def noroot():
  os.system("clear")
  print("RUN AS ROOT!")
  time.sleep(2)
  exit()

# Root verification
root = os.geteuid()
if root == 0:
  banner()
else:
  noroot()
