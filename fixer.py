import os
import subprocess
import shlex
p = subprocess.run('systemctl status nodered | grep error', shell=True, capture_output=True).stdout
result = str(p, 'utf-8')
if "error" in result:
        os.system('systemctl restart nodered')







