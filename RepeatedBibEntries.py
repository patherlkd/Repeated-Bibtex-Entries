
# original file containing repeated entries that could be the result of joining multiple bib files
# this code assumes a well behaved bibtex file i.e. entry types are lowercase and the standard layout.
infile = "input.bib"

# the output bib file you want to contain the unique entries from 'infile' without repeats
outfile = "output.bib"

entries = []

# get the headers for each entry
with open(infile,'r') as fp:
	for line in fp:
		line = line.strip()
		if '@' in line:
			entries.append(line)

print("Original number of entries: "+str(len(entries)))

unique_entries = []

[unique_entries.append(x) for x in entries if x not in unique_entries ]

print("Number of unique entries: "+str(len(unique_entries)))

ofp = open(outfile,'w')

# This loop only outputs the unique entries from the infile
for entry in unique_entries:
	with open(infile,'r') as fp:
		collect_entry = 0
		for line in fp:

			line = line.rstrip("\n")
			if (collect_entry == 0) and (entry in line):
				collect_entry = 1
				ofp.write(entry+'\n')
			elif (collect_entry == 1) and ('}' == line):
				ofp.write(line+'\n')
				break
			elif collect_entry == 1:
				ofp.write(line+'\n')
			else:
				pass

ofp.close()
