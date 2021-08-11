import numpy


class DegreeMatrix:
  def __init__(self, matrix):
    self.matrix = matrix = matrix

  def generate(self):
    length = len(self.matrix)
    result = numpy.zeros(shape=(length, length))
    for i, line in enumerate(self.matrix):
      line[i] = sum(line)
    return result
