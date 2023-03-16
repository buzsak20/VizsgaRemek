import subprocess

with open('gepnev.txt', encoding='utf8') as f:
    for line in f:
        command_logoff = ['powershell','Invoke-Command -ComputerName "{}" -ScriptBlock { logoff 2 }'.format(line.strip())]
        command_turnoff = ['powershell','Stop-Computer -ComputerName "{}"'.format(line.strip())]
        subprocess.run(command_logoff, command_turnoff, shell=True)
