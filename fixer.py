import os

stat = os.system('service status nodered ')

if (stat != 0):
    os.system('service restart nodered ')
