#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:12:21 2018

@author: shailesh
"""
# server-client program
# this is server.py
import socket

# next create a socket object
s = socket.socket()         # by default family= AF_INET and type= SOCK_STREAM
print "socket successfully created"

# reserve a port on your computer in out case it is 12345 but it can be anything
port = 12345

# next bing to the port
# we have not typed any ip in the ip field instead we have inputed an empty string
# this makes the server listen to requests coming from other computers on the network
s.bind(('',port))
print "socket binded to %s" %(port)

# put the socket into listening mode
s.listen(0)
print "socket is listening"

# a forever loop until we interrupt it or an error occurs
while True:
    # establish connection with client
    c, addr = s.accept()
    print  c, addr
    
    # send a thank you message to the client
    c.send("Thank you for connecting")
    
    # Close the connection with the client
    c.close()




























































