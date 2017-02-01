#!/usr/bin/env python
# Parse input report
# Input file is a report from http://cello.life.nctu.edu.tw

# Select all GIs from Extracellular records
# 
# Build a FASTA record of all Mouse Proteins with those GIs

from Bio import SeqIO

# I manually removed the first line of the input file as it contains column definitions
#input_file_name = "sample-input.txt"
input_file_name = "test-input.txt" # Real input

# Store all mouse protein records in a Dict indexed on gi number
#mice = {}
#for seq_record in SeqIO.parse("mouse.fasta", "fasta"):
#		mice[seq_record.id.split('|')[1]] = seq_record

outfile = open("test-output.fasta","w")

with open(input_file_name, "r") as infile:
	for line in infile:
		if line.startswith("SeqID"):
			# new record
			gi = line.split('|')[0].split(' ')[1]
		elif len(line.split()) > 2 and line.split()[0] == "Extracellular" and line.split()[2] == "*":# split on whitespace
			print gi
			
	


#			SeqIO.write(mice[gi], outfile, "fasta")
