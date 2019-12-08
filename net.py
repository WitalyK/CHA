import subprocess


result = subprocess.run(['net use \\\\192.168.0.99\D$\Журналы\\', '/user:onair2', '3A9b'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

print(result.returncode)