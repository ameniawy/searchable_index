# Abdelrahman M.

from tagger import extract
from collections import defaultdict


def _add_to_inverse_index(index_dict, tokens):
	"""
	Adds new tokens to inverse index.
	Params:
		index_dict: dict{word:list(ids)}
		tokens: tuple(id, list(words))
	returns:
		index_dict
	"""
	article_id = tokens[0]
	words = tokens[1]

	for word in words:
		if word in index_dict:
			index_dict[word].append(article_id)
		else:
			index_dict[word] = [article_id]

	return index_dict


def _load_tsv(path):
	"""
	Loads tsv file.
	Params: path(str): path to file
	Returns:
	"""


def tokenize():
	"""
	Load and tokenize the tsv file
	"""

	articles = load_tsv("simplewiki.tsv") # dict{id: text}
	index_dict = defaultdict(list)

	for article in articles:
		text = articles[article]
		words = extract(text, "en")
		index_dict = add_to_inverse_index(index_dict, words)

	return index_dict








