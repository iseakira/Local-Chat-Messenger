import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/socket_file'
print('connecting to {}'.format(server_address))

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

input_message = input('please write your message: ')

try:
    
    sock.sendall(input_message.encode())

    sock.settimeout(2)

    try:
        while True:
            data = sock.recv(32)

            if data:
                print(data.decode('utf-8'))
            else:
                break
    
    except(TimeoutError):
        print('Socket timeout, ending listening for server messages')

finally:
    print('closing socket')
    sock.close()
