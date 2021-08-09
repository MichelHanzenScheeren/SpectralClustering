import numpy


class EigenVectors:
  def __init__(self, degreeMatrix, adjacencyMatrix):
    self.degreeMatrix = degreeMatrix
    self.adjacencyMatrix = adjacencyMatrix

  def generate(self):
    laplacian = []
    for degree, adjacency in zip(self.degreeMatrix, self.adjacencyMatrix):
      line = [(value1 - value2) for value1, value2 in zip(degree, adjacency)]
      laplacian.append(line)
    eigenValues, eigenVectors = numpy.linalg.eig(laplacian)
    eigenValues, eigenVectors = eigenValues.real, eigenVectors.real
    return eigenVectors[:, numpy.argsort(eigenValues)]
