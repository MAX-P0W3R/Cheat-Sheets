#!/bin/python3

import sys
import socket
from datetime import datetime

# Define our target
if len(sys.argv) == 2:
  target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
else:
  print("Invalid amount of arguments.")
  print("Syntax: python3 scanner.py <ip>")

# Banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now))
print("-" * 50)
