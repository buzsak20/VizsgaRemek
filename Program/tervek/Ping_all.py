import subprocess

with open('ip.txt', encoding='utf8') as f:
    for line in f:
        ping = ['powershell','ping {}'.format(line.strip())]
        subprocess.run(ping, shell=True)
