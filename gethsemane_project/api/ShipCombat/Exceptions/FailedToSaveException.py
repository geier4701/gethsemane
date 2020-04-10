class FailedToSaveException(Exception):
	def __init__(self, *args):
		if args:
			self.message = args[0]
		else:
			self.message = None
		
	def __str__(self):
		if self.message:
			return 'Failed to save object with error: {0}'.format(self.message)
		else:
			return 'Failed to save object'
