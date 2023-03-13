import subprocess

class Gepnev:
        def __init__(self,name):
                self.name = name

list = []
j = int(input("Mennyi gépet szeretene kikapcsolni? "))
for x in range(j):
    pc_name = input("Adj meg egy nevet: ")
    list.append(Gepnev(pc_name))

for gepnev in list:
    command = ['powershell','Stop-Computer -ComputerName "{}"'.format(gepnev.name)]
    subprocess.run(command, shell=True)


