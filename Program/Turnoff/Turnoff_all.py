import subprocess

with open('gepnev.txt', encoding='utf8') as f:
    for line in f:
        command = ['powershell','Stop-Computer -ComputerName "{}"'.format(line.strip())]
        subprocess.run(command, shell=True)

'''
def Process(name):
    command = ['powershell', 'Stop-Computer -ComputerName "localhost" ']
    subprocess.run(command, shell=True)
        
command = "alma"
Process(command)
'''