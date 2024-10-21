import minecraft_launcher_lib
import subprocess
import os
minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory().replace('minecraft', 'Legacy')
minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()

print(f'██╗░░░░░███████╗░██████╗░░█████╗░░█████╗░██╗░░░██╗')
print(f'██║░░░░░██╔════╝██╔════╝░██╔══██╗██╔══██╗╚██╗░██╔╝')
print(f'██║░░░░░█████╗░░██║░░██╗░███████║██║░░╚═╝░╚████╔╝░')
print(f'██║░░░░░██╔══╝░░██║░░╚██╗██╔══██║██║░░██╗░░╚██╔╝░░')
print(f'███████╗███████╗╚██████╔╝██║░░██║╚█████╔╝░░░██║░░░')
print(f'╚══════╝╚══════╝░╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░')

def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)
    if iteration == total:
        print()

def maximum(max_value, value):
    max_value[0] = value

version = input('Select version: ')
nickname = input('nickname : ')
os.system('cls')
print('░██╗░░░░░░░██╗░█████╗░██╗████████╗')
print('░██║░░██╗░░██║██╔══██╗██║╚══██╔══╝')
print('░╚██╗████╗██╔╝███████║██║░░░██║░░░')
print('░░████╔═████║░██╔══██║██║░░░██║░░░')
print('░░╚██╔╝░╚██╔╝░██║░░██║██║░░░██║░░░')
print('░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░░╚═╝░░░')
print('\n')
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
print('\n')
max_value = [0]

callback = {
        "setStatus": lambda text: print(text, end='r'),
        "setProgress": lambda value: printProgressBar(value, max_value[0]),
        "setMax": lambda value: maximum(max_value, value)
}
minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory=minecraft_directory, callback=callback)
options = {
	'username': nickname,
}

os.system('cls' if os.name == 'nt' else 'clear')

subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory=minecraft_directory, options=options))