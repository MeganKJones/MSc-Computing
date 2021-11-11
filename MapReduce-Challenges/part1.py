from mrjob.job import MRJob

class part1(MRJob):
	def mapper(self, key, document):
		for number in document.split(","):
			yield "The maximum is:", int(number)

	def reducer(self, key, number):
			yield key, max(number)

part1.run()
