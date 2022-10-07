import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
# Use the socket object without calling s.close().
# AF_INET is the Internet address family for IPv4. SOCK_STREAM is the socket type for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) # The .bind() method is used to associate the socket with a specific network interface and port number
    s.listen() # listen() enables a server to accept connections
    """
        The .accept() method blocks execution and waits for an incoming connection.
        When a client connects, it returns a new socket object representing the connection and a tuple holding the address of the client
    """
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024) # data the client sends
            if not data:
                break
            conn.sendall(data) # echo the data