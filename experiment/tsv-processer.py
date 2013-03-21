# Process TSV files and check duration within an AOI and outside. Uses raw data from Tobii Studios.
import sys

if len(sys.argv) > 2:
	total = 0
	duration = 0	# on HUD

	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()
		for line in lines[1:]:
			line = line.strip()
			columns = line.split('\t')
			
			if int(columns[2]) == 1:
				duration += int(columns[1])
			total += int(columns[1])
	
	with open(sys.argv[2], 'w') as o:
		p = (float(duration) / total) * 100.0
		
		print >> o, "%f" % p