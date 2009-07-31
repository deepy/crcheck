#coding=latin1
import zlib
import array
import sys
import os
import time

crc = 0
t0 = time.time()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: python GenCrc.py filename filename ..."
    for fn in sys.argv[1:]:
	#print fn
        f = open(fn, "rb")
	while True:
		buffer = f.read(16000)
        	if buffer == "": break    # End of file
		else: crc = (zlib.crc32(buffer, crc) & 0xffffffff)
	f.close()
	#print "%08X"%(crc)
	if fn.find("%08X"%(crc)) > 0:
		print fn, "CRC matches: %08X"%(crc), "\n\n"
	else:
		print fn, "CRC doesn't match: %08X"%(crc), "\n\n"
	crc = 0
print "Execution took", time.time() - t0, "seconds"
var = raw_input("\nPress enter when done.\nwww.armchairs.be\n")
