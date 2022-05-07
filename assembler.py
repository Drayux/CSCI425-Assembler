# assmebler.py

##################################
# OFFICIAL MAIN FOR CZAR PROJECT #
##################################

import os
import sys


# -- MAIN --
def main(numGeneral, numFloating, astPath, outPath):
	print("TODO: Main program logic!")


# -- ARG PARSING --
if __name__ == "__main__":
	if len(sys.argv) != 4:
		print(f"USAGE: {sys.argv[0]} <Rn,Fn> <ast path (input)> <czr path (output)>")
		print("\tRn\t->\tNumber of general purpose registers")
		print("\tFn\t->\tNumber of floating point registers")
		print("\tRn >= Fn >= 5")

	# Register counts
	counts = None
	tmp = sys.argv[1].split(',')
	try: counts = (int(tmp[0]), int(tmp[1]))
	except IndexError: pass

	# Syntax Tree input
	astPath = None
	if os.path.exists(sys.argv[2]): astPath = sys.argv[2]

	# Program file output
	# CONSIDER: Actually check if this path can be written before opening
	outPath = sys.argv[3]

	# Call primary program logic
	main(counts[0], counts[1], astPath, outPath)
