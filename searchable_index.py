# Abdelrahman M.

from collections import defaultdict

from io2 import load_tsv
from tagger import extract
from logger import init_logger


def _add_to_inverse_index(index_dict, tokens):
	"""
	Adds new tokens to inverse index.
	Args:
		index_dict: dict{word:list(ids)}
		tokens: tuple(id, list(words))
	Returns:
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


def _load_content(file_path):
	"""
	Calls _load_tsv and organizes the data in a dict format
	Args:
		file_path (str): path to the file to be read
	Returns:
		articles_dict (dict{id: text}) : contains id: text of each row in the corpus

	"""
	two_dim = load_tsv(file_path)
	articles_dict = {}

	for row in two_dim:
		# row[0] = id, row[1] = title, row[2] = text
		text_id = row[0]

		# append the title and the text together
		text = row[1] + ' ' + row[2]
		articles_dict[text_id] = text

	return articles_dict


def tokenize(file_path):
	"""
	Load and tokenize the tsv file
	Args:
		file_path(str): the tsv file path.
	Returns:
		index_dict (dict{word:list(ids)}) : contains the inverse indices
	"""
	logger = init_logger()

	logger.info("Will start loading the tsv corpus..")
	articles = _load_content(file_path) # dict{id: text}
	index_dict = defaultdict(list)
	logger.info("Done loading corpus..")
	i = 0

	for article in articles:
		i = i + 1
		if i % 1000 == 0:
			logger.info("Now processing at %s", i)

		text = articles[article]
		words = extract(text, "en")
		index_dict = _add_to_inverse_index(index_dict, (article, words))

	logger("Done.. successfuly created inverse index")

	return index_dict
