import socket

# Get the host name
hostname = socket.gethostname()

# Get the IP address associated with the host
ip_address = socket.gethostbyname(hostname)

print("Hostname:", hostname)
print("IP address:", ip_address)