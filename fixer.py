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
        f.write(date_time,"We restart nodered!")
        f.close()
        os.system('systemctl restart nodered')