from mrjob.job import MRJob

class part4(MRJob):
	def mapper(self, key, document):
		(link0, link1) = document.split(',')
		yield ' ', (link0, link1)
		
	def reducer(self, key, list_of_urls):
		urlList = []
		for line in list_of_urls:
			urlList.append(line)
		for routes in urlList:
			for urls in urlList:
				if urls[0]==routes[1]:
					path = routes[0] + ", " + routes[1] + ", " + urls[1]
					yield key, path
part4.run()