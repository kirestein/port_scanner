import socket

ip = input('Enter the host or IP to be verify: ')

ports = []
count = 0

while count < 10:
    ports.append(int(input('Enter the port to be verify: ')))
    count += 1
print('')
print('---------------OUTPUT---------------')
print('')
for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPV4 e TCP IP
    client.settimeout(0.05)
    code = client.connect_ex((ip, port))

    if code == 0:
        print(f'Port {port} is open')
    else:
        print(f'Port {port} is closed')

print('')
print('Scan finished!')