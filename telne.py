import telnetlib
import  time

with telnetlib.Telnet('10.111.10.2') as t:
    t.read_until(b'Username')
    t.write(b'admin\n')
    t.read_until(b'Password')
    t.write(b'cisco\n')
    t.write(b'terminal length 0\n')
    t.write(b'sh cdp ne\n')
    time.sleep(1)
    output = t.read_very_eager().decode('utf-8')
    print(output)