class UnableToFormatException(Exception):
	def __init__(self, *args):
		if args:
			self.message = args[0]
		else:
			self.message = None
	
	def __str__(self):
		if self.message:
			return 'Object failed to format with error with error: {0}'.format(self.message)
		else:
			return 'Object failed to format'
