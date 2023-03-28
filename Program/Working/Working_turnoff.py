import subprocess

command_connect  = ['powershell', 'Enter-PSSession TESZT']
command_logoff = ['powershell','Invoke-Command -ComputerName TESZT -ScriptBlock { logoff console }']
command_turnoff = ['powershell','Invoke-Command -ComputerName TESZT -ScriptBlock { Stop-Computer }']
subprocess.run(command_connect, shell=True)
subprocess.run(command_logoff, shell=True)
subprocess.run(command_turnoff, shell=True)

