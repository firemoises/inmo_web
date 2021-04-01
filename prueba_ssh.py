import paramiko
from time import sleep
import random

def print_ssh(output):
    stdin, stdout, stderr = output
    stdout._set_mode("rb")
    lines = stdout.readlines()
    print(lines)

host = "148.0.3.66"
port = 22
username = "moise"

command = "cd Dropbox"
command2 = "cd GitHub dropbox"
command3 = "mkdir pruebassh"
#command3 = "dir"

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(host, port, username, password)

channel = ssh.get_transport().open_session()
channel.invoke_shell()

#channel.sendall(command)
#channel.sendall(command2)
channel.sendall(command3)

print(channel.recv(99999))