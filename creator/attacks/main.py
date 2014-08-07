import os
import time

def attack(): # Launch Attack!!!
  os.system("clear")
  os.system("cat creator/attacks/avalible.txt")
  attackType = input("\nOption?(1/2/3) --> ")
  if attackType == "1":
    os.system("clear")
    os.system("python creator/attacks/sslstrip.py")
  elif attackType == "2":
    os.system("clear")
    os.system("python creator/attacks/dnspoof.py")
  elif attackType == "3":
    os.system("clear")
    os.system("python creator/attacks/dsniff.py")
  else:
    os.system("clear")
    print("Option 1, 2, or 3.")
    time.sleep(2)
    os.system("clear")
    attack()

def main():
  attack()

def noroot(): # noRoot
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
