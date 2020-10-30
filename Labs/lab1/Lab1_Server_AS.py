import sys # In order to terminate the program
import socket
# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

filename1 = '/list1.html';
f1 = open(filename1[1:])
contentList = str(f1.read()).lower()
pos1 = contentList.find('Version : ')
versionnb = contentList[pos1+10:pos1+13]
vnbServer = float(versionnb)
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Assign a port number
serverPort = 9351

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))
MAXSIZE = 10

# Listen to at most 1 connection at a time
serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections
print('The server is ready to receive')
while True:
	# Set up a new connection from the client
	connectionSocket, addr = serverSocket.accept()
	print(f'Connection established with {addr}')
	# If an exception occurs during the execution of try clause
	# the rest of the clause is skipped
	# If the exception type matches the word after except
	# the except clause is executed
	try:
		message = connectionSocket.recv(1024).decode()
		a = len(message)
		# Receives the request message from the client
		if (a < 10): 
			connectionSocket.send(f'ACK'.encode())
			vnbClient = float(message)
			print(f'Version of the client : {vnbClient}')
			print(f'Version of the server : {vnbServer}')
			message = connectionSocket.recv(1024).decode()
			print(f'Same version? : {vnbClient == vnbServer}')
		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
			if len(message)>1:
				filename = message.split()[1]
				print(f'Sent Data {filename}\r\n')
		# Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character 
				f = open(filename[1:])
			# Store the entire contenet of the requested file in a temporary buffer
				outputdata = f.read()
				
			# Send the HTTP response header line to the connection socket
				connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
				message = connectionSocket.recv(1024)
				print(f'Answer from the client :\n {message}\r\n')
				print(f'Sending data :\n{outputdata}\r\n')
				if (vnbClient == vnbServer):
					connectionSocket.send(f'{10:<{MAXSIZE}}'.encode())
					connectionSocket.send("Uptodate\r\n\r\n".encode())
				else:
					connectionSocket.send(f'{len(outputdata):<{MAXSIZE}}'.encode())
			# Send the content of the requested file to the connection socket
					for i in range(0, len(outputdata)):  
						connectionSocket.send(outputdata[i].encode())
					#connectionSocket.send("\r\n".encode()) 
			# Close the client connection socket
			connectionSocket.send("\r\n\r\n".encode()) 
			connectionSocket.close()
		else:
			print(f'Request message {message}')
			# Extract the path of the requested object from the message
			# The path is the second part of HTTP header, identified by [1]
			if len(message)>1:
				filename = message.split()[1]
			# Because the extracted path of the HTTP request includes 
			# a character '\', we read the path from the second character 
				f = open(filename[1:])
			# Store the entire contenet of the requested file in a temporary buffer
				outputdata = f.read()
				print(f'Sent Data {outputdata}\r\n')
			# Send the HTTP response header line to the connection socket
				connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
				message = connectionSocket.recv(1024)
				print(f'Answer from the client :\n {message}\r\n')
				connectionSocket.send(f'{len(outputdata):<{MAXSIZE}}'.encode())
			# Send the content of the requested file to the connection socket
				for i in range(0, len(outputdata)):  
					connectionSocket.send(outputdata[i].encode())
					#connectionSocket.send("\r\n".encode()) 
			# Close the client connection socket
			connectionSocket.send("\r\n\r\n".encode()) 
			connectionSocket.close()

	except IOError:
			# Send HTTP response message for file not found
			connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
			connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
			# Close the client connection socket
			connectionSocket.close()

serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data
