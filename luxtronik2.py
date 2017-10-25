#!/usr/bin/python
# Script to read values from Luxtronik 2.0 heat pump control units (used by Alpha Innotec and other vendors)
# Temperature values are displayed in degrees Celsius
#
# by Stefan Prokop
# Version 1.0
# 
# Set IP of your Luxtronik 2.0 device below

import sys
if len(sys.argv) > 1:
 input=(str(sys.argv[1]))

import socket
import struct
import datetime
import httplib
import datetime, time

#####################
# Luxtronik 2.0 IP
hostHeatpump = '127.0.0.1'
# Luxtronik 2.0 port (standard 8888)
portHeatpump = 8888
#####################

def ts2string(ts, fmt="%Y-%m-%d %H:%M:%S"):
    dt = datetime.datetime.fromtimestamp(ts)
    return dt.strftime(fmt)

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
s.connect( (hostHeatpump, portHeatpump))

######################################################
s.send( struct.pack( '!i', 3004))
s.send( struct.pack( '!i', 0))
if struct.unpack( '!i', s.recv(4))[0] != 3004:
        print 'Error: REQ_CALCULATED CMD'
        exit()
stat = struct.unpack( '!i', s.recv(4))[0]
len = struct.unpack( '!i', s.recv(4))[0]
array_calculated = []
for i in xrange(len):
        array_calculated.append(struct.unpack( '!i', s.recv(4))[0])
s.close ()

if input == 'ambtemp':
 print(str(float(array_calculated[15])/10))
elif input == 'avetemp':
 print(str(float(array_calculated[16])/10))
elif input == 'servicewateract':
 print(str(float(array_calculated[17])/10))
elif input == 'servicewatertarget':
 print(str(float(array_calculated[18])/10))
elif input == 'flow':
 print(str(float(array_calculated[10])/10))
elif input == 'return':
 print(str(float(array_calculated[11])/10))
elif input == 'returntarget':
 print(str(float(array_calculated[12])/10))
elif input == 'hotgas':
 print(str(float(array_calculated[14])/10))
elif input == 'datelastfailure':
 print(str(int(array_calculated[95])/1))
elif input == 'datelastfailurenice':
 print(ts2string(float(int(array_calculated[95])/1)))
elif input == 'codelastfailure':
 print(str(int(array_calculated[100])/1))
else :
 print "Usage: {ambtemp|avetemp|servicewateract|servicewatertarget|flow|return|returntarget|hotgas|datelastfailure|datelastfailurenice|codelastfailure}"


############ RAW Data as returned from Luxtronik 2.0
#print array_calculated
############
