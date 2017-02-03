#!/usr/bin/env python
# Parse input report
# Input file is a report from http://cello.life.nctu.edu.tw

# Select all GIs from Extracellular records
# 
# Build a FASTA record of all Mouse Proteins with those GIs

from Bio import SeqIO

#input_file_name = "sample-input.txt"
input_file_name = "full-input.txt" # Real input

# Store all mouse protein records in a Dict indexed on gi number
mice = {}
for seq_record in SeqIO.parse("mouse.fasta", "fasta"):
		mice[seq_record.id.split('|')[1]] = seq_record

outfile = open("output.fasta","w")

with open(input_file_name, "r") as infile:
	for line in infile:
		if line.startswith("SeqID"):
			# new record, store its GI number, but only keep if it's "Extracellular"
			gi = line.split('|')[1]
		else:
			# lines we want look like this:
			#  	    Extracellular	    2.632  *
			# three white-space-delimited columns, with "Extracellular" in the first 
			# column, and "*" in the third, last column
			cols = line.split()	
			if len(cols) > 2 and cols[0] == "Extracellular" and cols[2] == "*":
				# Print FASTA records only for those GI's whose CELLO records are 
				# "Extracellular"
				SeqIO.write(mice[gi], outfile, "fasta")
