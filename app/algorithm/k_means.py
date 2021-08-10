from app.algorithm.distance import Distance, DistanceType
from random import randint
import numpy


class KMeans:
  def __init__(self, numberOfCLusters, distanceType, maxIterations=150):
    self.numberOfCLusters = numberOfCLusters
    self.distanceType = distanceType
    self.maxIterations = maxIterations

  def generate(self, values):
    centroids = [values[randint(0, len(values) - 1)] for _ in range(self.numberOfCLusters)]
    groups = numpy.zeros(len(values), dtype=numpy.int8)
    iterations = 0
    while iterations < self.maxIterations:
      wasChanged = self.classifyPoints(values, centroids, groups, False)
      self.recalculateCentroids(values, centroids, groups)
      iterations += 1
      if not wasChanged: break
    return groups

  def classifyPoints(self, values, centroids, groups, wasChanged):
    for i, line in enumerate(values):
      distances = [Distance(line, centroids[x]).solve(self.distanceType) for x in range(len(centroids))]
      newGroup = numpy.where(distances == numpy.amin(distances))
      if newGroup[0][0] != groups[i]:
        groups[i] = newGroup[0][0]
        wasChanged = True
    return wasChanged

  def recalculateCentroids(self, values, centroids, groups):
    for i in range(len(centroids)):
      groupValuesIds = numpy.where(groups == i)
      centroids[i] = numpy.average(numpy.take(values, groupValuesIds), axis=0)
