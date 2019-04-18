# pylint: disable-all

# Import socket module 
import socket 


def Main(): 
	# local host IP '127.0.0.1' 
	host = '127.0.0.1'

	# Define the port on which you want to connect 
	port = 80

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

	# connect to server on local computer 
	s.connect((host,port)) 

	# message you send to server 
	msg = input("Enter Your URL >> ")
	msg += "\r\n";
	s.send(msg.encode()) 

	data = s.recv(1024)
	code = data.decode()
	if code == "200":
		type = s.recv(1024).decode()
		size = s.recv(1024)
		data = s.recv(int(size))
		file = open ("gotFile."+type, "wb")
		file.write(data)
	if code == "404":
		data = s.recv(1024).decode()
		print(data)
		

	# close the connection 
	s.close() 

if __name__ == '__main__': 
	Main() 
