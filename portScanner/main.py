import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPV4 e TCP IP
client.settimeout(0.05)

ip = input('Enter the host or IP to be verify: ')
port = int(input('Enter the port to be verify: '))

code = client.connect_ex((ip, port))

if code == 0:
    print('Port is open')
else:
    print('Port is closed')