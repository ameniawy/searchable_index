# Abdelrahman M.

import searchable_index


LOAD = 0


def _start_index():
	"""
	 Calls the function tokenize from searchable_index to get an inverse dict of the data
	"""

	index_dict = searchable_index.tokenize()