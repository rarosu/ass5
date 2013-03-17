# Process TSV files and check duration within an AOI and outside. Uses raw data from Tobii Studios.
import sys

if len(sys.argv) > 2:
	total = 0
	durations = [0, 0]

	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()
		for line in lines[1:]:
			line = line.strip()
			columns = line.split('\t')
			
			durations[int(columns[2])] += int(columns[1])		
			total += int(columns[1])
	with open(sys.argv[2], 'w') as o:
		for d in durations:
			print >> o, "%f" % (float(d) / total)