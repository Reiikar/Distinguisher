import sys

file_name="biblio.bib"



fout = open('Newbiblio.bib', 'w')

temp = sys.stdout

sys.stdout = fout

with open(file_name, 'r') as f:
	line = f.readline()
	while line:
		if "title" in line and "booktitle" not in line:
			i = 0
			while (line[i] != '{'):
				i += 1
				print(line[i], end = '')
			while (i < len(line) - 1):
				i += 1
				if (line[i].isupper()):
					print('{' + line[i] + '}', end = '')
				else:
					print(line[i], end = '')
			#print("{}".format(line.strip()))
		else:
			print("{}".format(line.strip()))
		line = f.readline()

sys.stdout = temp

fout.close()