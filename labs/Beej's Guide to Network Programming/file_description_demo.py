""" Defindo que sockets são file descriptors."""
import socket
import sys
 
print('stdin :', sys.stdin.fileno())
print('stdout :', sys.stdout.fileno())
print('stderr :', sys.stderr.fileno())

with open(__file__, 'rb') as f:
    print('arquivo:', f.fileno())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print('socket :', s.fileno())

