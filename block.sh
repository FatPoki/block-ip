#! /bin/sh

# colored text

yellow="\e[33m"
cayn="\e[36m"
purple="\e[95m"
red="\e[31m"
white="\e[37m"

# prerequesit installation 
# apt install figlet -y

#banner art

echo "${yellow}"
figlet  block 
sleep 1

echo " ▶ \e[31mPlease Note That This Tool Will Block The Ip From The Ip Table That Is Unauthoraised In Any Way " 
echo " ▶ \e[31mUse It On Your Own Risk."
echo '\nType Ip To Block ? \n '
echo "${cayn}"
read ip 
# tool
sudo iptables -I INPUT -s $ip -j DROP
sleep 1
sudo service iptables save
sleep 1
sudo iptables -L
echo "$white"
sleep 1
sudo iptables -L
echo "${cayn}"
echo " For more help type 'iptables -h' ."
echo " Thanks for using my tool ; ) "