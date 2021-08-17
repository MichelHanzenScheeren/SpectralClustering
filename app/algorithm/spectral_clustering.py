from app.algorithm.k_means import KMeans
from app.algorithm.eigen_vectors import EigenVectors
from app.algorithm.degree_matrix import DegreeMatrix
from app.algorithm.adjacency_matrix import AdjacencyMatrix
from app.algorithm.distance_matrix import DistanceMatrix
from app.algorithm.distance import DistanceType


class SpectralClustering:
  """ Classe que encapsula toda a lógica do spectral clustering. """

  def __init__(self, numberOfCLusters, distanceType, neighbors):
    self.numberOfCLusters = numberOfCLusters if numberOfCLusters is not None else 2
    self.distanceType = distanceType if distanceType is not None else 2
    self.neighbors = neighbors if neighbors is not None else 10

  def generate(self, values):
    self.__validateArgs__(values)
    distanceMatrix = DistanceMatrix(values, DistanceType(self.distanceType)).generate()
    adjacencyMatrix = AdjacencyMatrix(distanceMatrix, self.neighbors).generate()
    degreeMatrix = DegreeMatrix(adjacencyMatrix).generate()
    eigenVectors = EigenVectors(degreeMatrix, adjacencyMatrix).generate()
    kmeans = KMeans(self.numberOfCLusters, DistanceType(self.distanceType))
    # Na versão do cluster que seguimos, utiliza-se no KMeans todos os autovetores, com as colunas de 1 até o número de clusters que se que dividir.
    return kmeans.generate(eigenVectors[:, 1:self.numberOfCLusters])

  def __validateArgs__(self, values):
    """ Validação básica dos dados, para evitar erros em tempo de execução. """
    if len(values) <= 2:
      raise Exception('São necessários pelo menos 2 dados para a aplicação da classificação')
    if len(values[0]) == 0:
      raise Exception('Os dados devem possuir pelo menos um atributo para a classificação')
    if not (type(self.numberOfCLusters) is int and self.numberOfCLusters >= 2):
      raise Exception(f'"{self.numberOfCLusters}" não é um valor válido para o número de Clusters (esperava um valor > 1)')
    if not (type(self.distanceType) is int and self.distanceType in [0, 1, 2]):
      raise Exception(f'O tipo de distância fornecido não é valido (esperava "0", "1", ou "2")')
    if not (type(self.neighbors) is int and self.neighbors > 1):
      raise Exception(f'"{self.neighbors}" não é um valor válido para o número de vizinhos no algoritmo KNN (esperava um valor > 1)')
