# Abdelrahman M.

from polyglot.text import Text as PolyglotExtractor


def extract(text, language):
	"""
	Function that extracts tokens and entities from text
	"""

	tagged_text = PolyglotExtractor(text, hint_language_code=language)
	entities = tagged_text.entities
	tokens = tagged_text.tokens

	words = set()

	for entity in entities:
		for token in entity:
			words.add(token)

	words = list(words)

	return words
