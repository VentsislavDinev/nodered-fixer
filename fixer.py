import os
import subprocess
import shlex

result = subprocess.run(shlex.split('journalctl -u nodered.service --since 1min ago'))
raw_output = result.stdout
output = raw_output.decode() 
if 'ERROR' in output:
    os.system('systemctl restart nodered')
