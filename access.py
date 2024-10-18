#sudo apt-get -y install hostapd dnsmasq


#sudo nano /etc/dhcpcd.conf
#denyinterfaces wlan0


#sudo nano /etc/network/interfaces
'''auto lo
iface lo inet loopback

auto eth0
iface eth0 inet dhcp

allow-hotplug wlan0
iface wlan0 inet static
    address 192.168.5.1
    netmask 255.255.255.0
    network 192.168.5.0
    broadcast 192.168.5.255
'''

#sudo nano /etc/hostapd/hostapd.conf
'''interface=wlan0
driver=nl80211
ssid=MyPiAP
hw_mode=g
channel=6
ieee80211n=1
wmm_enabled=1
ht_capab=[HT40][SHORT-GI-20][DSSS_CCK-40]
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_key_mgmt=WPA-PSK
wpa_passphrase=raspberry
rsn_pairwise=CCMP
'''

#sudo nano /etc/default/hostapd
#DAEMON_CONF="/etc/hostapd/hostapd.conf"



#two commands 
#sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.bak
#sudo nano /etc/dnsmasq.conf
'''interface=wlan0 
listen-address=192.168.5.1
bind-interfaces 
server=8.8.8.8
domain-needed
bogus-priv
dhcp-range=192.168.5.100,192.168.5.200,24h
'''
#sudo systemctl enable hostapd 
#sudo systemctl enable dnsmasq 

#sudo systemctl start hostapd 
#sudo systemctl start dnsmasq 


#sudo reboot 

