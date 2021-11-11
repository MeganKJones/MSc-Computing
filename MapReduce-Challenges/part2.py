from mrjob.job import MRJob

class part2(MRJob):
	def mapper(self, key, document):
		for lines in document.split("\n"):
			for animal in document.split(","):
				yield animal, lines

	def reducer(self, animal, lines):
		sublists=[]
		for line in lines:
			sublists.append(line)
		yield animal, sublists

part2.run()
