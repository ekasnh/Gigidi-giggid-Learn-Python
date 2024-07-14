#from csv import reader
#with open('file.csv','r') as f:
#	csv_reader = reader(f)
#	next(csv_reader)
#	for row in csv_reader:
#		print(row)

from csv import DictReader
with open('file.csv','r') as f:
	csv_reader = DictReader(f,delimiter = '|')
	for row in csv_reader:
		print(row['email'])