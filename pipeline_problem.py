import sys
import csv
import json
from os import path
if (len(sys.argv) <= 2):
	print('Usage: %s input_file.csv output_file.json' % sys.argv[0])
	sys.exit()
input_file = sys.argv[1]
output_file = sys.argv[2]
output = []
if (not path.isfile(input_file)):
	print('Error: Could not find %s' % input_file)
	sys.exit()

def main():

	
	output = convert_input(input_file)
	write_output(output_file, output)
		
def convert_input(input_file):
	output = []
	with open(input_file, 'rb') as f:
		print('Converting input to json')
		reader = csv.reader(f)
		headers = reader.next()
		print('Headers: %s' % headers)
		for row in reader:
			obj = dict.fromkeys(headers)
			for i in range(len(row)):
				obj[headers[i]] = row[i]
			output.append(obj)
		print('Finished converting, starting to write output ')
	return output
	
def write_output(output_file, output):
	with open(output_file, 'wb') as f:
		print('Writing file')
		f.write(json.dumps(output, indent=4))
		print('Done!')
		


if (__name__ == '__main__'):
	main()