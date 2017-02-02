# Abdelrahman M.

import searchable_index

import io2


LOAD = 0


def start_index(load):
	"""
	 Calls the function tokenize from searchable_index to get an inverse dict of the data
	"""

	if load == 0:
		index_dict = searchable_index.tokenize('simplewiki.tsv')
		io2.write_pkl(index_dict, 'reverse_index.pkl')
	else:
		io2.read_pkl('reverse_index.pkl')


#def search(load):

