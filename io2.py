# Abdelrahman M.

"""
IO functions
"""

import csv
import cPickle

def load_tsv(file_path):
	"""
	Read tsv files.
	Args:
		file_path (str): path to the file to be read
	Returns:
		list[list(str)]: content of the tsv file
	"""
	with open(file_path) as f:
		reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
		content = [row for row in reader]

	return content


def read_pkl(file_path):
	"""
	Read pkl files.

	params:
		file_path (str): path to the file to be read
	returns:
		obj: content of the pkl file
	"""
	with open(file_path, 'rb') as f:
		content = cPickle.load(f)

	return content


def write_pkl(content, file_path):
	"""
	Write content to a pkl format.

	params:
		content (obj): content of the file to be written
		file_path (str): path to the output file
	"""
	with open(file_path, 'wb') as f:
		cPickle.dump(content, f, 2)