# socket-programming-in-python
socket programming is a process in which we connects two nodes on network so that they can communicate each other. One socket(node) listens on a particular port at an IP, while other socket reaches out the other to form a connection. Server forms the listener socket while reaches out to the server.

server and client are real backbones behind web browsing.

Socket programming is started by importing the socket library and making a simple socket.
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Here we made a socket instance and passed it two parameters. The first parameter is AF_INET and the second one is SOCK_STREAM. AF_INET refers to the address family ipv4. The SOCK_STREAM means connection oriented TCP protocol.

We can only connect to a server by knowing it's ip. You can find the ip of the server by using this:$ ping www.google.com

You can also find the ip using python: 
import socket
ip = socket.gethostbyname('www.google.com')
print ip

You can see connect to the google server program in repository.
* First of all we made a socket.
* Then we resolved google's ip and lastly we connected to google.
* Now we need to know how can we send some data through a socket.
* For sending data the socket library has a sendall function. This function allows you to send data to a sever to which the socket is connected and server can also send data to client using this function.

## server
A server has a bind() method which binds it to a specific ip and port so that it can listen to incoming requests on that ip and port. A server has a listen() method which puts the server into listen mode. This allows the server to listen to incoming connections. And last a server has an accept() and close() method. The accept method initiates a connection with the client and the close method closes the connection with the client.

server.py this is server file in repository
how it works
* First of all we import socket which is necessary.
* Then we made a socket object and reserved a port on our pc.
* After that we binded our server to the specified port. Passing an empty string means that the server can listen to incoming connections from other computers as well. If we would have passed 127.0.0.1 then it would have listened to only those calls made within the local computer.
* After that we put the server into listen mode. 5 here means that 5 connections are kept waiting if the server is busy means 5 request can handel at a time one by one and if a 6th socket trys to connect then the connection is refused.
* At last we make a while loop and start to accept all incomming connections and close those connections after a thank you message to all connected sockets.

## client
client.py in repository
* First of all make a socket object.
* Then we connect to localhost on port 12345 (the port on which our server runs) and lastly we receive data from the server and close the connection.
* Now save this file as client.py and run it from the terminal after starting the server script.














