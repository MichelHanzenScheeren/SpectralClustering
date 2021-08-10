from app.algorithm.distance import Distance, DistanceType
from random import randint
import numpy


class KMeans:
  def __init__(self, values=[], k=5, distanceType=DistanceType.Euclidean, maxIterations=100):
    self.values = values
    self.k = k
    self.distanceType = distanceType
    self.maxIterations = maxIterations

  def generate(self):
    centroids = [self.values[randint(0, len(self.values) - 1)] for _ in range(self.k)]
    groups = numpy.zeros(len(self.values))
    wasChanged = True
    iterations = 0
    while wasChanged and iterations < self.maxIterations:
      wasChanged = self.classifyPoints(centroids, groups, wasChanged)
      self.recalculateCentroids(centroids, groups)
      iterations += 1
    return groups

  def classifyPoints(self, centroids, groups, wasChanged):
    for i, line in enumerate(self.values):
      distances = [Distance(line, centroids[x]).solve(self.distanceType) for x in range(len(centroids))]
      newGroup = numpy.where(distances == numpy.amin(distances))
      if newGroup[0][0] != groups[i]:
        groups[i] = newGroup[0][0]
        wasChanged = True
    return wasChanged

  def recalculateCentroids(self, centroids, groups):
    for i in range(len(centroids)):
      groupValuesIds = numpy.where(groups == i)
      centroids[i] = numpy.average(numpy.take(self.values, groupValuesIds), axis=0)
