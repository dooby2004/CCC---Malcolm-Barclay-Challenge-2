import os
f = open("stegpass.txt",'r')
f = f.readlines()
for line in f:
    if line[-1] == "\n" or line[-1] == "\r":
        line = line[:-1]
    if line[-1] == "\n" or line[-1] == "\r":
        line = line[:-1]
    os.system('steghide --extract -sf Keyboard.jpg.pdf -p ' + line)
