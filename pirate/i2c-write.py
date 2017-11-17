#!/usr/bin/env python
# encoding: utf-8
"""
Adapted from i2c-test.py from Peter Huewe
"""
import sys
from pyBusPirateLite.I2C import *
import argparse
import time
from array import *


mydata = array('B', [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

def bytes(integer):
    return divmod(integer, 0x100)

def i2c_write_byte(address, data):
    haddress, laddress = bytes(address)
    global mydata
#    i2c.send_start_bit()
#    i2c.bulk_trans(1, [0xa2])
#    i2c.bulk_trans(1, [haddress])
#    i2c.bulk_trans(1, [laddress])
#    i2c.bulk_trans(1, [ord(data)])
#    print "data: %s" % hex(ord(data))
#    print "address: %s" % hex(address)
    if ((laddress % 16)) == 0 and (address != 0):
        print '%07x %03o %03o %03o %03o %03o %03o %03o %03o %03o %03o %03o %03o %03o %03o %03o %03o' % (address-16,mydata[0],mydata[1],mydata[2],mydata[3],mydata[4],mydata[5],mydata[6],mydata[7],mydata[8],mydata[9],mydata[10],mydata[11],mydata[12],mydata[13],mydata[14],mydata[15])
        mydata[laddress % 16] = ord(data)
#    elif laddress == 0:
#        mydata[0] = ord(data)
#        print 'yo'
    else:
        mydata[laddress % 16] = ord(data)
#        print 'yo'
#    i2c.send_stop_bit()


def i2c_read_bytes(address, numbytes, ret=False):
    data_out=[]
    i2c.send_start_bit()
    i2c.bulk_trans(len(address),address)
    while numbytes > 0:
        if not ret:
            print ord(i2c.read_byte())
        else:
            data_out.append(ord(i2c.read_byte()))
        if numbytes > 1:
            i2c.send_ack()
        numbytes-=1
    i2c.send_nack()
    i2c.send_stop_bit()
    if ret:
        return data_out

if __name__ == '__main__':
    parser = argparse.ArgumentParser(sys.argv[0])
    parser.add_argument("-i", "--input", dest="inputfile", metavar="INPUTFILE", type=argparse.FileType('rb'),
            required=True)
    parser.add_argument("-p", "--serial-port", dest="bp", default="/dev/ttyUSB0")
    parser.add_argument("-s", "--size", dest="size", type=int, required=True)
    parser.add_argument("-S", "--serial-speed", dest="speed", default=115200, type=int)
    parser.add_argument("-b", "--block-size", dest="bsize", default=256, type=int)

    args = parser.parse_args(sys.argv[1:])

       
   # Start dumping
#    for block in range(0, args.size, args.bsize):
    i = 0
    print args.size
    for i in range(0, args.size):
#        print i
        i2c_write_byte(i, args.inputfile.read(1))
    args.inputfile.close()


