#Answer to 8.1.1.1-3
from mrjob.job import MRJob
class MRWordCounter(MRJob):

        def mapper(self, _, line):
                for ch in list(line):
                        yield ch, 1
                for word in line.split():
                        yield word, 1
                yield "lines", 1

        def reducer(self, key, values):
                yield key, sum(values)

if __name__ == '__main__':
        MRWordCounter.run()
