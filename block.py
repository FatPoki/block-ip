import subprocess

# Colored text
YELLOW = "\033[33m"
CAYN = "\033[36m"
PURPLE = "\033[95m"
RED = "\033[31m"
WHITE = "\033[37m"

# Banner art
print(f"{YELLOW}")
subprocess.run(["figlet", "block"])
print(" ▶ \033[31mPlease Note That This Tool Will Block The Ip From The Ip Table That Is Unauthorized In Any Way")
print(" ▶ \033[31mUse It On Your Own Risk.")

ip = input("\nType Ip To Block: \n")

# Tool
subprocess.run(["sudo", "iptables", "-I", "INPUT", "-s", ip, "-j", "DROP"])
subprocess.run(["sudo", "service", "iptables", "save"])
subprocess.run(["sudo", "iptables", "-L"])
print(f"{WHITE}")
subprocess.run(["sudo", "iptables", "-L"])
print(f"{CAYN}")
print(" For more help type 'iptables -h' .")
print(" Thanks for using my tool ; )")
