import numpy


class DegreeMatrix:
  """ Classe que gera a matriz de graus a partir da matriz de adjacência.
  É uma matriz nXn diagonal em que a diagonal principal possui a soma dos valores da linha, e todos os outros valores são 0. """

  def __init__(self, matrix):
    self.matrix = matrix = matrix

  def generate(self):
    length = len(self.matrix)
    result = numpy.zeros(shape=(length, length))
    for i, line in enumerate(self.matrix):
      line[i] = sum(line)
    return result
