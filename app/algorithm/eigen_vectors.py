import numpy


class EigenVectors:
  def __init__(self, degreeMatrix, adjacencyMatrix):
    self.degreeMatrix = degreeMatrix
    self.adjacencyMatrix = adjacencyMatrix

  def generate(self):
    laplacian = self.degreeMatrix - self.adjacencyMatrix
    eigenValues, eigenVectors = numpy.linalg.eig(laplacian)
    eigenValues, eigenVectors = eigenValues.real, eigenVectors.real
    return eigenVectors[:, numpy.argsort(eigenValues)]
