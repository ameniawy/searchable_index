# Abdelrahman M.
'''
Here I use the polyglot text extractor to extract the entities.
It's possible here to count the occurence of the entities within each article.
But for the time being I'm only extracting the entities.
'''

from polyglot.text import Text as PolyglotExtractor

def extract(text, language):
	"""
	Function that extracts tokens and entities from text.
	Args:
		text(str)
		language(str)
	Returns:
		words(list(str)): list containg entities
	"""

	tagged_text = PolyglotExtractor(text, hint_language_code=language)
	entities = tagged_text.entities
	tokens = tagged_text.tokens

	words = set()

	for entity in entities:
		for token in entity:
			words.add(token.lower())

	words = list(words)

	return words
