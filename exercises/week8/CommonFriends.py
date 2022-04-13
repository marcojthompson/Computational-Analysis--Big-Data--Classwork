#Answer to 8.1.1.1-3
from mrjob.job import MRJob
class MRWordCounter(MRJob):

	def mapper(self, _, line):
		for ch in line.split():
			firstChars = []
			for i in range(len(line)):
				for j in range

	def reducer(self, key, values):
		yield key, sum(values)

if __name__ == '__main__':
	MRWordCounter.run()
