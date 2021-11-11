from mrjob.job import MRJob

class part3(MRJob):
	def mapper(self, key, document):
		i=0
		words = document.split(" ")
		while i < len(words)-3:
			sequence = ' '.join(words[i:i+4])
			i+=1
			yield sequence, 1

	def reducer(self, sequence, occurrences):
		yield sequence, sum(occurrences)

part3.run()