import os
import time

# Sysname
def sysname():
  sysname = os.uname()[0]
  print("\t·System type: " + sysname)

# Release (Distribution)
def release():
  release = os.uname()[2]
  print("\t·Release: " + release)

# Architecture
def machine():
  machine = os.uname()[4]
  print("\t·Architecture: " + machine)

# System Information
def systemInfo():
  print("\n·Your machine information:\n")
  sysname()
  release()
  machine()

# Main Window
def mainWindow():
  os.system("clear")
  os.system("cd install && cat banner.txt")
  systemInfo()
  option = input("\nOption?(1/2/3/4/5/6) --> ")
  # Options
  if option == "1": # Debian
    os.system("clear")
    os.system("python install/distros/debian.py")
  elif option == "2": # Fedora
    os.system("clear")
    os.system("python install/distros/fedora.py")
  elif option == "3": # OpenSuse
    os.system("clear")
    os.system("python install/distros/opensuse.py")
  elif option == "4": # Archlinux
    os.system("clear")
    os.system("python install/distros/archlinux.py")
  elif option == "5": # Back
    os.system("python main.py")
  elif option == "6": # Exit
    os.system("clear")
    print("HAPPY HACKING!")
    time.sleep(2)
    os.system("clear")
    exit()
  else:
    os.system("clear")
    print("Option 1, 2, 3, 4, 5 or 6.")
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
  mainWindow()
else:
  noroot()
