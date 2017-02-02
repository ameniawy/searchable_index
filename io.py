# Abdelrahman M.

"""
IO functions
"""

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