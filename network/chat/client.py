import threading
import socket

# The input() function allows user input.
nickname = input('Choose a nickname ')
# client socket with IPV4 address family , and TCP connetion type
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# The client calls .connect() to establish a connection to the server and initiate the three-way handshake.
client.connect( ('127.0.0.1' , 55552) )
# receive the message 
def receive():
    while True: # infinite loop
        try: 
            message = client.recv(1024).decode('ascii') # client message which will be limited to 1024
            if message == "NICK": 
                client.send(nickname.encode('ascii'))
            else:
                print(message)

        except:
            print("An error occurred!")
            client.close()
            break


# client write a message which will be sent to all clients
def write():
    while True:
        message = f'{nickname} : {input("")}' # get that message
        client.send(message.encode('ascii')) # send that message in ascii format

# start thread with reveive function
receive_thread = threading.Thread(target=receive)
receive_thread.start()
#  start thread with reveive write
write_thread = threading.Thread(target=write)
write_thread.start()
