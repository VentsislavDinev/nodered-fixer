import os
import subprocess
import shlex

#result = subprocess.run(shlex.split('journalctl -u systemd-udevd --since 1min ago'))
#raw_output = result.stdout
#output = unicode(raw_output, 'UTF-8')
#if 'ERROR' in output:
#    os.system('systemctl restart nodered')
    
#response = subprocess.Popen(["journalctl", "-u nodered", "--since", "60 seconds ago", "--no-pager"], stdout=subprocess.PIPE).stdout.read()
#print(response)
response = subprocess.Popen(["systemctl", " status node-red"], stdout=subproces>
print("response return: ")
print(response) 

