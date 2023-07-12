#!/usr/bin/env python3 
import sys,time,socket
ip = "192.168.1.63" 
port = 9999
timeout = 5
prefix = "" 
string = prefix + "ABC123ABC123..."
try:
	with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
		s.settimeout(timeout)
		s.connect((ip,port))
		s.send(bytes(string,"latin-1"))
except:
	print ("Could not connect")