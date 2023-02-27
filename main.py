import socket
import keyboard
from colorama import init
from colorama import Fore, Back, Style

# Config init ============== STARTS
IP_ADDRESS = "192.168.43.100" 
PORT = 12484
moveFront = "up_arrow"
moveBack = "down_arrow"
moveLeft = "left_arrow"
moveRight = "right_arrow"
moveUTurn = ""
moveStop = ""
autoMode = "a"
manualMode = "m"
allControlKey = [moveFront,moveBack,moveLeft,moveRight,autoMode,manualMode]
modeState = False # Defaule is False means its in Manual Mode
info = Fore.LIGHTYELLOW_EX + '\033[1m' + """
╭━━━┳━━━╮╱╭╮╱╱╱╱╭━━━┳━━━┳━━━╮
┃╭━╮┃╭━╮┃╭╯╰╮╱╱╱┃╭━━┫╭━╮┃╭━╮┃
┃╰━╯┃┃╱╰╯╰╮╭╋━━╮┃╰━━┫╰━━┫╰━╯┃
┃╭━━┫┃╱╭╮╱┃┃┃╭╮┃┃╭━━┻━━╮┃╭━━╯
┃┃╱╱┃╰━╯┃╱┃╰┫╰╯┃┃╰━━┫╰━╯┃┃
╰╯╱╱╰━━━╯╱╰━┻━━╯╰━━━┻━━━┻╯
\033[0m""" + Fore.LIGHTYELLOW_EX + """Hi, I will be helping you to control ESP32 
over WiFi through Socket Connection
@Author : Sukarna jana
@Version: v1.0.1

Trying to connect to Network:""" + Fore.LIGHTMAGENTA_EX +"""
Network : {}
Port    : {}\033[0m
""".format(IP_ADDRESS,PORT)
# Config init ============== ENDS

def main():
    global modeState
    while True:
        # Robot in Automation Mode
        while modeState:
            if(keyboard.is_pressed(manualMode)):
                print(Fore.LIGHTBLUE_EX + '\033[1m' + "\n\n[Bot Mode]" + '\033[0m' + Fore.BLUE + " >>> Manual Mode...")
                modeState = False
            data = host.recv(1024)
            if data:
                print(Fore.LIGHTMAGENTA_EX + '\033[1m' + "[RECEIVED] : " + '\033[0m', data.decode())
            #host.close()
        # Robot on Manual Mode 
        while not modeState:
            if keyboard.is_pressed(moveFront):
                print(Fore.LIGHTGREEN_EX + '\033[1m' + "[Manual Mode]" + '\033[0m' + " >>> Moving Front")
                host.sendall(b"F\n")
            elif keyboard.is_pressed(moveBack):
                print(Fore.LIGHTGREEN_EX + '\033[1m' + "[Manual Mode]" + '\033[0m' + " >>> Moving Back")
                host.sendall(b"B\n")
            elif keyboard.is_pressed(moveLeft):
                print(Fore.LIGHTGREEN_EX + '\033[1m' + "[Manual Mode]" + '\033[0m' + " >>> Moving Left")
                host.sendall(b"L\n")
            elif keyboard.is_pressed(moveRight):
                print(Fore.LIGHTGREEN_EX + '\033[1m' + "[Manual Mode]" + '\033[0m' + " >>> Moving Right")
                host.sendall(b"R\n")
            elif(keyboard.is_pressed(autoMode)):
                print(Fore.LIGHTBLUE_EX + '\033[1m' + "\n\n[Bot Mode]" + '\033[0m' + Fore.BLUE + " >>> Automation Mode...")
                modeState = True
            elif(keyboard.read_key() not in allControlKey): 
                print(Fore.RED + '\033[1m' + "[ERROR] :" + '\033[0m' + " Invalid Input")
            data = host.recv(1024)
            if data:
                print(Fore.LIGHTMAGENTA_EX + '\033[1m' + "[RECEIVED] : " + '\033[0m', data.decode())
            #host.close()

if(__name__=="__main__"):
    print(info)
    init(autoreset=True)
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as host:
            host.connect((IP_ADDRESS, PORT))
            print(Fore.LIGHTGREEN_EX + '\033[1m' + "Connected to ESP32" + '\033[0m')
            main()
    except socket.error:
        print(Fore.RED + '\033[1m' + "[ERROR] : Fail to connect to ESP" + '\033[0m')
