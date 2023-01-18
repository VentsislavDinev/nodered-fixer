import os

stat = os.system('service ndoered status')

if (stat != 0):
    os.system('service ndoered restart')