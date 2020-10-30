import sys # In order to terminate the program
import socket
import os
import time
# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Assign a port number
serverPort = 9150

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))
MAXSIZE = 10
# Listen to at most 1 connection at a time
serverSocket.listen(500)

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
		# Receives the request message from the client
		message = connectionSocket.recv(1024).decode()
		print(f'{message}\n')
		
		connectionSocket.send(f'Received'.encode())
		message = connectionSocket.recv(1024).decode()
		print(f'{message}\n')

		minutes = 0
		fichier = open(f"{addr}_Request_state.txt","w") 
		fichier.write(f'No')
		fichier.close()
		# Answer the request from the client or timeout
		print('Waiting for you to treat the request\n')
		count = 0
		minutes = 0
		a = 0
		unconsidered = True
		while unconsidered:
			time.sleep(1)
			count = count + 1
			fichier = open(f"{addr}_Request_state.txt","r") 
			string = fichier.read()
			fichier.close()
			string = string.lower()
			pos1 = string.find('y')
			if (pos1 != -1):
				unconsidered = False
			if (count == 10):
				count = 0
				minutes = minutes + 1;
				a = 1
				if (minutes != 1): 
					os.remove(f"{addr}_{minutes-1}.txt")
				fichier = open(f"{addr}_{minutes}.txt","w")
				fichier.write(f'')
				fichier.close()
		
		print(f'You are beginning to treat this request:\n')
		connectionSocket.send(f"Considered".encode())
		message = connectionSocket.recv(1024).decode()
		print(f'{message}\n')
		
		html_object = ''
		newobj = True
		obj = True
		while obj:
			msg2 = connectionSocket.recv(1024)
			if newobj and len(msg2)!=0:
				objlength = int(msg2[:MAXSIZE])
				newobj = False
			html_object += msg2.decode()
			if len(html_object)-MAXSIZE == objlength:
				print(f'Users data :\r\n{html_object[MAXSIZE:]}')
				if (a==1) : 
					os.remove(f"{addr}_{minutes}.txt")
				fichier1 = open(f"Data_Current_client.txt","w")
				fichier1.write(f'{html_object[MAXSIZE:]}')
				fichier1.close()
				html_object = ''
				obj = False
				
		connectionSocket.send(f'In treatment, please wait for us to call you'.encode())	
		connectionSocket.close()
		string = input("All associated files closed? :")
		if (string != ''):
			os.remove(f"{addr}_Request_state.txt")
		
		fichier1 = open(f"Data_Current_client.txt","r")
		string = fichier1.read()
		fichier1.close()
		pos1 = string.find('Lab = ')
		Lab_nb = string[pos1+6:pos1+7]
		pos2 = string.find('Numberidentifier = ')
		User_nb = string[pos2+19:pos2+20]
		pos3 = string.find('Name = ')
		User_name1 = string[pos3+7:pos3+11]


		if (pos1 != -1) & (pos2 != -1):
			fichier1 = open(f"Record/person{User_nb}_{Lab_nb}.txt","r")
			string = fichier1.read()
			fichier1.close()
			pos = string.find('Name = ')
			User_name2 = string[pos+7:pos+11]
			if (User_name2 == User_name1):
				fichier1 = open(f"Data_Current_client.txt","w")
				fichier1.write(f'{string}')
				fichier1.close()
				print('Lab data found and now used')
			else :
				print('This user lab file hasn''t been found')
		else :
			print('This user hasn''t been in a lab')
			
	except IOError:
			# Send HTTP response message for file not found
			print('Connection lost with the client')
			# Close the client connection socket
			connectionSocket.close()

serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data