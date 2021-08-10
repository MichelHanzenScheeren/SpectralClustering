from app.algorithm.k_means import KMeans
from app.algorithm.eigen_vectors import EigenVectors
from app.algorithm.degree_matrix import DegreeMatrix
from app.algorithm.adjacency_matrix import AdjacencyMatrix
from app.algorithm.distance_matrix import DistanceMatrix
from app.algorithm.distance import DistanceType


class SpectralClustering:
  def __init__(self, numberOfCLusters, distanceType, neighbors):
    self.numberOfCLusters = numberOfCLusters or 2
    self.distanceType = DistanceType(distanceType) if distanceType is not None else DistanceType.Euclidean
    self.neighbors = neighbors or 8

  def generate(self, values):
    distanceMatrix = DistanceMatrix(values, self.distanceType).generate()
    adjacencyMatrix = AdjacencyMatrix(distanceMatrix, self.neighbors).generate()
    degreeMatrix = DegreeMatrix(adjacencyMatrix).generate()
    eigenVectors = EigenVectors(degreeMatrix, adjacencyMatrix).generate()
    return KMeans(self.numberOfCLusters, self.distanceType).generate(eigenVectors[:, 1:self.numberOfCLusters])
