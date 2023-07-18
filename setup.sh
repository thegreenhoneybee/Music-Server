sudo mkdir /mnt
echo '//192.168.2.1/Network /mnt cifs user=simon,pass=paradigm 0 0' | sudo tee -a /etc/fstabsmb_network_share





sudo mount -t cifs //192.168.2.1/Network /mnt -o username=simon,password=paradigm
sudo umount /mnt