import os
import time

# Aircrack install 64 bits.
def aircrackx64():
  os.system("cd downloads && wget http://packman.links2linux.org/download/aircrack-ng/1848829/aircrack-ng-1.2.beta2-1.11.x86_64.rpm && zypper install aircrack-ng-1.2.beta2-1.11.x86_64.rpm && rm -r aircrack-ng-1.2.beta2-1.11.x86_64.rpm && cd ..")

# Aircrack-ng install 32 bits.
def aircrackx86():
  os.system("cd downloads && wget http://packman.links2linux.org/download/aircrack-ng/1849213/aircrack-ng-1.2.beta2-1.11.i586.rpm && zypper install aircrack-ng-1.2.beta2-1.11.i586.rpm && rm -r aircrack-ng-1.2.beta2-1.11.i586.rpm && cd ..")

# DHCP server install 64 bits.
def dhcpx64():
  os.system("cd downloads && wget ftp://195.220.108.108/linux/opensuse/factory/repo/oss/suse/x86_64/dhcp-server-4.2.6-0.7.1.x86_64.rpm && zypper install dhcp-server-4.2.6-0.7.1.x86_64.rpm && rm -r dhcp-server-4.2.6-0.7.1.x86_64.rpm && cd ..")

# DHCP server install 32 bits.
def dhcpx86():
  os.system("cd downloads && wget ftp://195.220.108.108/linux/opensuse/factory/repo/oss/suse/i586/dhcp-server-4.2.6-0.7.1.i586.rpm && zypper install dhcp-server-4.2.6-0.7.1.i586.rpm && rm -r dhcp-server-4.2.6-0.7.1.i586.rpm && cd ..")

# DNS server install 64 bits.
def dnsx64():
  os.system("cd downloads && wget ftp.opensuse.org/distribution/13.1/repo/oss/suse/x86_64/dnsmasq-2.65-7.1.2.x86_64.rpm && zypper install dnsmasq-2.65-7.1.2.x86_64.rpm && rm -r dnsmasq-2.65-7.1.2.x86_64.rpm && cd ..")

# DNS server install 32 bits.
def dnsx86():
  os.system("cd downloads && ftp.opensuse.org/distribution/13.1/repo/oss/suse/i586/dnsmasq-2.65-7.1.2.i586.rpm && zypper install dnsmasq-2.65-7.1.2.i586.rpm && rm -r dnsmasq-2.65-7.1.2.i586.rpm && cd ..")

# Main
def main():
  os.system("clear")
  os.system("cat install/distros/banner.txt")
  option = input("\nContinue?(y/n) --> ") #Accept
  if option == "y":
    os.system("clear")
    arch = os.uname()[4]
    if arch == "x86_64":
      print("Installing for " + arch)
      time.sleep(1)
      aircrackx64() # Install Aircrack!
      dhcpx64() # Install DHCP server!
      dnsx64() # Install DNS server!
      os.system("clear")
      print("Everything is installed!")
      time.sleep(1)
      os.system("python main.py")
    elif arch == "i686":
      time.sleep(1)
      print("Installing for " + arch)
      aircrackx86() # Install Aircrack!
      dhcpx86() # Install DHCP server!
      dnsx86() # Install DNS server!
      os.system("clear")
      print("Everything is installed!")
      time.sleep(1)
      os.system("python main.py")
    else:
      os.system("clear")
      print("ERROR!\nINSTALL IT MANUALLY!")
      time.sleep(2)
      exit()
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
