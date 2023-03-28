import subprocess

with open('gepnev.txt', encoding='utf8') as f:
    for line in f:
        command_connect  = ['powershell', 'Enter-PSSession {}'.format(line.strip())]
        command_logoff = ['powershell','Invoke-Command -ComputerName {} -ScriptBlock {{ logoff console }}'.format(line.strip())]
        command_turnoff = ['powershell','Invoke-Command -ComputerName {} -ScriptBlock {{ Stop-Computer }}'.format(line.strip())]
        subprocess.run(command_connect, shell=True)
        subprocess.run(command_logoff, shell=True)
        subprocess.run(command_turnoff, shell=True)
