host = "148.0.3.66"
port = 22
username = "moise"
password = "Secundario@444"

command = "dir"

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(host, port, username, password)


stdin, stdout, stderr = ssh.exec_command(command)

lines = stdout.readlines()

print(lines)