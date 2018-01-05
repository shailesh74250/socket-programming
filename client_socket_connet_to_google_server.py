#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 11:56:04 2018

@author: shailesh
"""
# connect our client socket to the google server

import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket successfully created"
except socket.error as err:
    print "socket creation failed with errors %s" % (err)

# default port for socket
port = 80

# getting google host ip address through python 
try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print "there was an error resolving the host"
    sys.exit()

# connecting to the server
s.connect((host_ip, port))
print "the socket has successfully connected to google on port == %s" % (host_ip)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
