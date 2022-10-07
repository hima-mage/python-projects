import threading
# Sockets and the socket API are used to send messages across a network
import socket

host = '127.0.0.1' # localhost
port = 55552 # port to listen to
"""
create a socket object using socket.socket(),
pecifying the socket type as socket.SOCK_STREAM : TCP  Transmission Control Protocol (TCP)
"""
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind((host, port))
# It listens for connections from clients. When a client connects, the server calls
server.listen()

clients =[]
nicknames = []

# here i send any message sent by any user to all user online
def broadcast(message):
    # for clients connected send that message
    for client in clients:
        client.send(message)

# how to handle client add or remove 
def handle(client):
    # infinite loop
    while True:
        try:
            message = client.recv(1024) # message received from the client max 1024 bytes
            broadcast(message) # broadcast that message
        except:
            index = client.index(client) # get index of that client
            clients.remove(client) # remove it
            client.close() # close his connection
            nickname = nicknames[index] # get his nickname
            broadcast(f'{nickname} left the chat! '.encode('ascii')) # broadcast message that he left
            nicknames.remove(nickname) # remove that customer for the list
            break

# receive function
def receive():
    while True:
        # accept() to accept, or complete, the connection.
        client , address = server.accept() # accept all connection comming
        print(f"connected with {str(address)}") # display who is connected
        # send message to client to enter his nickname
        client.send("NICK".encode('ascii'))
        nickname = client.recv(1024).decode('ascii') # get nickname client entered with 1024 bytes max value
        nicknames.append(nickname) # add nickname to list of nicknames
        clients.append(client)

        print(f'Nickname of the client is  {nickname}!') # display on server who connected
        broadcast(f'{nickname} joined the chat! ' .encode('ascii')) # tell all clients who joined
        client.send('Connected to the chat! '.encode('ascii')) # send to that client display message on server
        
        thread = threading.Thread(target=handle , args=(client,))
        thread.start()


print("Server is Listening .....")
receive()



