import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPV4 e TCP IP

code = client.connect_ex(('google.com', 80))

print(f'{code=}')