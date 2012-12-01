from array import Array

# Create an array for the counters and initialize each element to 0.
theCounters = Array(127)
theCounters.clear(0)

# Open the text file for reading and counting
theFile = open('Frankenstein.txt','r')
for line in theFile:
	for letter in line:
		code = ord(letter)
		theCounters[code] += 1
theFile.close()

# Print the results
for i in range(26):
	print ("%c - %4d                %c - %4d" % (chr(65+i), theCounters[65+i], chr(97+i), theCounters[97+i]))

