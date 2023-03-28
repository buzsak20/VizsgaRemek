import subprocess

class Gepnev:
    def __init__(self, name):
        self.name = name

list = []
j = int(input("Mennyi gépet szeretene kikapcsolni? "))
for x in range(j):
    pc_name = input("Adj meg egy nevet: ")
    list.append(Gepnev(pc_name))

for gepnev in list:
        command_connect  = ['powershell', 'Enter-PSSession {}'.format(gepnev.name)]
        command_logoff = ['powershell','Invoke-Command -ComputerName {} -ScriptBlock {{ logoff console }}'.format(gepnev.name)]
        command_turnoff = ['powershell','Invoke-Command -ComputerName {} -ScriptBlock {{ Stop-Computer }}'.format(gepnev.name)]
        subprocess.run(command_connect, shell=True)
        subprocess.run(command_logoff, shell=True)
        subprocess.run(command_turnoff, shell=True)
