class Question:
	def __init__(self, prompt, answer, info): # Added an info attribute for the Question class, so that users can learn why their answer was correct/incorrect.
		self.prompt = prompt
		self.answer = answer
		self.info = info