class Config(object):
	def __init__(self, model_name=None):
		self.model_name = model_name

		if self.model_name == 'bert-base-chinese':
			self.max_epochs = 30
			self.lr = 0.00001
			self.batch_size = 128
			self.cuda = True
			self.max_len = 50
		elif self.model_name == 'bert-base-english':
			self.max_epochs = 30
			self.lr = 0.00001
			self.batch_size = 128
			self.cuda = True
			self.max_len = 50
		elif self.model_name == 'bert-base-french':
			self.max_epochs = 30
			self.lr = 0.00001
			self.batch_size = 128
			self.cuda = True
			self.max_len = 30
		else:
			self.max_epochs = 30
			self.lr = 0.0001
			self.batch_size = 128
			self.cuda = True
			self.max_len = 50