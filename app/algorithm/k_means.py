from app.algorithm.distance import Distance
from random import randint
import numpy


class KMeans:
  def __init__(self, numberOfCLusters, distanceType, maxIterations=200):
    self.numberOfCLusters = numberOfCLusters
    self.distanceType = distanceType
    self.maxIterations = maxIterations

  def generate(self, values):
    centroids = self.kPlusPlusCentroids(values)
    groups = numpy.zeros(len(values), dtype=numpy.int8)
    iterations = 0
    while iterations < self.maxIterations:
      wasChanged = self.classifyPoints(values, centroids, groups, False)
      self.recalculateCentroids(values, centroids, groups)
      iterations += 1
      if not wasChanged: break
    return groups

  def kPlusPlusCentroids(self, values):
    copyValues = values
    centroids = [copyValues[randint(0, len(copyValues) - 1)]]
    distances = numpy.array([Distance(line, centroids[0]).solve(self.distanceType) for line in copyValues])
    numberOfCentroids = 1
    while True:
      maxDistanceindex = numpy.where(distances == numpy.amax(distances))[0][0]
      newCentroid = copyValues[maxDistanceindex]
      centroids.append(newCentroid)
      numberOfCentroids += 1
      if numberOfCentroids >= self.numberOfCLusters: break
      copyValues = numpy.delete(copyValues, maxDistanceindex, axis=0)
      distances = numpy.delete(distances, maxDistanceindex)
      distances = (distances + numpy.array([Distance(line, centroids[-1]).solve(self.distanceType) for line in copyValues])) / 2
    return centroids

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
      if len(groupValuesIds[0]) == 0: continue
      centroids[i] = numpy.average(numpy.take(values, groupValuesIds), axis=0)
