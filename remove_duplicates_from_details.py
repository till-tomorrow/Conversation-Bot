import sys

def remove_duplicates(fname):
	new_details = set()
	f = open(fname,'r')
	for line in f:
		new_details.add(line)

	f.close()
	new_details = list(new_details)
	return new_details


def write_file(new_details,fname):
	f = open(fname,'w')
	for line in new_details:
		f.write(line)
	f.close()

if __name__ == '__main__':
	fname = sys.argv[1]
	new_details = remove_duplicates(fname)
	write_file(new_details,fname)

	print 'done!'