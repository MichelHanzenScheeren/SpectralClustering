import numpy
from app.algorithm.distance import DistanceType


class SimilarityMatrix:
  def __init__(self, distanceMatrix=[]):
    self.distanceMatrix = distanceMatrix

  def generate(self):
    for i, value in enumerate(self.distanceMatrix):
      for j in range(i, len(value)):
        if i == j: value[j] = 0
        else:
          value[j] = 1 / (1 + value[j])
          self.distanceMatrix[j][i] = value[j]
    return numpy.array(self.distanceMatrix)
