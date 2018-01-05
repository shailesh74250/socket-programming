#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 13:38:37 2018

@author: shailesh
"""
# clien.py
import socket

# create socket object
s = socket.socket()

# define a port on which port you want to connect to the server
port = 12345

# connect socket to the local server which is having port number 12345
s.connect(('', port))

# receive message from server
print s.recv(1024)

# close the connection
s.close()
print "hello world"
