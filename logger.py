
import logging

def init_logger():
	"""
	Initialize and return logger.
	"""
	logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(levelname)s : %(message)s')
	logger = logging.getLogger(__name__)
	return logger