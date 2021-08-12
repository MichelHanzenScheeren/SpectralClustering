from app.algorithm.distance import Distance
from random import randint
import numpy


class KMeans:
  """ Implementação do algoritmo de clusterização KMeans. O Spectral cluster o utiliza após a redução da dimensionalidade dos dados e demais processos com as matrizes. """
  def __init__(self, numberOfCLusters, distanceType, maxIterations=200):
    self.numberOfCLusters = numberOfCLusters
    self.distanceType = distanceType
    self.maxIterations = maxIterations

  def generate(self, values):
    centroids = [values[randint(0, len(values) - 1)] for _ in range(self.numberOfCLusters)]  # Centróids são escolhidos a partir de pontos aleatórios dos próprios valores.
    groups = numpy.zeros(len(values), dtype=numpy.int8)
    iterations = 0
    while iterations < self.maxIterations:  # Controle para limite de iterações
      wasChanged = self.classifyPoints(values, centroids, groups, False)  # Reclassifica os pontos para seu centróide mais próximo.
      self.recalculateCentroids(values, centroids, groups)  # Recalcula os centróides.
      iterations += 1
      if not wasChanged: break  # Se nenhum ponto mudou de centróide, o algoritmo já convergiu e pode ser finalizado.
    return groups

  def classifyPoints(self, values, centroids, groups, wasChanged):
    for i, line in enumerate(values):
      distances = [Distance(line, centroids[x]).solve(self.distanceType) for x in range(len(centroids))]  # Lista com a distância do ponto até cada centróide.
      newGroup = numpy.where(distances == numpy.amin(distances))  # Pega o índice do centróide de menor distância
      if newGroup[0][0] != groups[i]:  # Se for diferente do centróide atual, muda-o e registra a mudança.
        groups[i] = newGroup[0][0]
        wasChanged = True
    return wasChanged

  def recalculateCentroids(self, values, centroids, groups):
    for i in range(len(centroids)):
      groupValuesIds = numpy.where(groups == i)  # Pega os índices de todos os pontos que estão nesse centróide.
      if len(groupValuesIds[0]) == 0: continue  # Se não há nenhum ponto, nada precisa ser feito
      centroids[i] = numpy.average(numpy.take(values, groupValuesIds), axis=0)  # Se existem pontos, recalcula o centróide como ponto médio destes.
