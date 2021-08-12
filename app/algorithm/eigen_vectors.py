import numpy


class EigenVectors:
  """ Classe que gera a matriz de autovetores a partir da matriz laplaciana. """
  def __init__(self, degreeMatrix, adjacencyMatrix):
    self.degreeMatrix = degreeMatrix
    self.adjacencyMatrix = adjacencyMatrix

  def generate(self):
    laplacian = self.degreeMatrix - self.adjacencyMatrix  # Geração da matriz laplaciana a partir da subtração da matriz de graus pela matriz de adjacência.
    eigenValues, eigenVectors = numpy.linalg.eig(laplacian)  # O numpy gera os autovalores e autovetores da matriz laplaciana.
    eigenValues, eigenVectors = eigenValues.real, eigenVectors.real  # Garantir que apenas valores reais serão usados (o numpy pode retornar valores imaginários também)
    return eigenVectors[:, numpy.argsort(eigenValues)]  # retorna os autovetores, após ordená-los de acordo com a ordenação dos autovalores.
