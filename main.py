#Windows 10
import os
import time
import server
import build
global homescreen
homescreen = """
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
└──────────────────────────────────────────────────────────────┘"""

def main():
    global listener_choice
    global payload_choice
    listener_choice = False
    payload_choice = False
    startup()
    options()
    action()



def startup():
    global direct
    direct = str(os.getcwd())
    try:
        os.chdir("C:/")
        os.mkdir("Py-Shell-Files")
    except FileExistsError:
        pass
    os.system("cls")
    print(homescreen)
    print("Loading ...")
    time.sleep(3)


def options():
    global listener_choice
    global payload_choice
    while True:
        os.system("cls")
        print(homescreen)
        try:
            choice = int(input("[1] Create payload file\n[2] Setup port listener\n\n[?] Choose an option: "))
            if choice == 2:
                listener_choice = True
                break
            elif choice == 1:
                payload_choice = True
                break
        except Exception as e:
            pass


def action():
    if listener_choice == True:
        server.create()


    elif payload_choice == True:
        os.chdir(direct)
        build.setup()

    else:
        wait = input("A choice error occurred")
        exit()




main()
