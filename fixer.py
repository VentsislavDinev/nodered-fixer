import os

stat = os.system('systemctl show -p ActiveState --value nodered ')

if (stat != "active"):
    os.system('service restart nodered')
