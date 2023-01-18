import os
import subprocess
import shlex

result = subprocess.run(shlex.split('journalctl -u systemd-udevd --since 1min ago'))
raw_output = result.stdout
output = result(raw_output, 'UTF-8')
if 'ERROR' in output:
    os.system('systemctl restart nodered')
