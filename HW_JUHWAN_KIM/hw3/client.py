import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9000))

sock.send('김주환'.encode())  
student_id = int.from_bytes(sock.recv(4), 'big')
print('Received student number:', student_id)

sock.close()
