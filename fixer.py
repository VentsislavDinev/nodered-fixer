import os
import subprocess
from datetime import datetime
import shlex
now = datetime.now() # current date and time
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
p = subprocess.run('systemctl status nodered | grep error', shell=True, capture_output=True).stdout
result = str(p, 'utf-8')
if "error" in result: 
        f = open("logger.txt", "a")
        f.write("{} We restart nodered!".format(date_time))
        f.close()
        os.system('systemctl restart nodered')