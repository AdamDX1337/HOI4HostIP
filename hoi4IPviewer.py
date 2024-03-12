#MADE BY MASTOID, UPDATED BY SilverXK

#1. Install python.
#2. Open an administrator command prompt.
#3. Type 'pip install pydivert' into cmd. (first time use only) #Skip this if you already have it
#4. Type 'python'. Python should now be running.
#5. Run the script. Type exec(open("C:/path_to_script_here.py").read()) in the python terminal or another way.

import pydivert
import threading
import socket

HostIPs = set()

HostIPs.add(socket.gethostbyname(socket.gethostname()))

def networking():
	with pydivert.WinDivert("udp.PayloadLength > 0") as w:
		for packet in w:
			Hex1 = packet.payload.hex()
			if packet.dst_addr not in HostIPs:
				if "34cff6b0d8fdf8ca69a44f" in Hex1 or "010000000400" in Hex1:
					print("\nThe host IP is: " + packet.dst_addr + " | Port: " + str(packet.dst_port))
					HostIPs.add(packet.dst_addr)

			w.send(packet)

def dumpIPs():
	print(HostIPs)

threading.Thread(name='networking', target=networking).start() # required multithreading to allow user input without pausing windivert

print("\nHOI4 Host IP Revealer by SilverXK loaded.\nHost IP will be revealed when trying to make any connection to the game.\nType dumpIPs() to dump the HostIPs set.")
