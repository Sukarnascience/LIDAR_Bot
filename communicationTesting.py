import socket

# Set the IP address and port number of the ESP32
ip = '192.168.1.100'
port = 12345

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the ESP32
s.connect((ip, port))

# Send a message to the ESP32
message = "Hello from PC!"
s.sendall(message.encode())

# Receive a response from the ESP32
data = s.recv(1024)
print('Received:', data.decode())

# Close the socket
s.close()
