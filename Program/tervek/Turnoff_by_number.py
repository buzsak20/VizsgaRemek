import subprocess

class Gepnev:
        def __init__(self,name):
                self.name = name

list = []
j = int(input("Mennyi gépet szeretene kikapcsolni? "))
for x in range(j):
    pc_name = input("Adj meg egy nevet (Test.test.lan): ")
    list.append(Gepnev(pc_name))

if pc_name != "localhost":
    for gepnev in list:
        command_logoff = ['powershell','Invoke-Command -ComputerName "{}" -ScriptBlock { logoff 2 }'.format(gepnev.name)]
        command_turnoff = ['powershell','Stop-Computer -ComputerName "{}"'.format(gepnev.name)]
        subprocess.run(command_logoff, command_turnoff, shell=True)
else:
    for gepnev in list:
        command_turnoff = ['powershell','Stop-Computer -ComputerName "{}"'.format(gepnev.name)]
        subprocess.run( command_turnoff, shell=True)
