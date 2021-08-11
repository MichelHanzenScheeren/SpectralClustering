from app.algorithm.distance import Distance
import numpy


class DistanceMatrix:
  def __init__(self, values, type):
    self.values = self.normalize(values)
    self.type = type

  def generate(self):
    length = len(self.values)
    result = numpy.zeros(shape=(length, length))
    for i, value1 in enumerate(self.values):
      for j, value2 in enumerate(self.values):
        if j == i: continue
        elif j < i: result[i][j] = result[j][i]
        else: result[i][j] = Distance(value1, value2).solve(self.type)
    return result

  def normalize(self, values):
    mins, maxs = numpy.min(values, axis=0), numpy.max(values, axis=0)
    return (values - mins) / (maxs - mins)
