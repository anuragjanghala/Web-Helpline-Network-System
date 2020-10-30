import socket

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverPort = 9150
serverSocket.connect((socket.gethostname(),serverPort))
MAXSIZE = 10

identification : ''

print(f'Connection established')

serverSocket.send(f"Ambulance request for emergency".encode())
try:
	msg1 = serverSocket.recv(1024)
	print(f'Request state : \r\n {msg1}\n')
	serverSocket.send('ACK received'.encode())
	
	msg1 = serverSocket.recv(1024)		
	print(f'Request state : \r\n {msg1}\n')
	serverSocket.send('ACK considered'.encode())
	
	fichier = open(f"me.txt","r")
	string = fichier.read()
		
	serverSocket.send(f'{len(string):<{MAXSIZE}}'.encode())
			
	for i in range(0, len(string)):  
		serverSocket.send(string[i].encode())
		#serverSocket.send("\r\n".encode()) 

	msg1 = serverSocket.recv(1024)
	print(f'Request state : \r\n {msg1}\n')	

	serverSocket.close()  
except IOError:
	# Send HTTP response message for file not found
	print('Something went wrong, please retry or call 112')
	# Close the client connection socket
	serverSocket.close()
