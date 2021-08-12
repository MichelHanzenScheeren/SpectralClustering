from app.algorithm.distance import Distance
import numpy


class DistanceMatrix:
  """ Classe que gera a matriz de distâncias, matriz nXn em que cada linha possui a distânia do ponto 'n' até todos os outros pontos. """

  def __init__(self, values, type):
    self.values = self.normalize(values)
    self.type = type

  def generate(self):
    """ Gera uma matriz numpy nXn, percorre todos os dados com 2 laços calculando a distância do ponto i ao ponto j. """
    length = len(self.values)
    result = numpy.zeros(shape=(length, length))
    for i, value1 in enumerate(self.values):
      for j, value2 in enumerate(self.values):
        if j == i: continue  # Ignora, pois a distância de um ponto até si mesmo é zero.
        elif j < i: result[i][j] = result[j][i]  # Se j é menor do que i, então a distância já foi calculada anteriormente.
        else: result[i][j] = Distance(value1, value2).solve(self.type)  # Encaminha os dois pontos a classe que calcula as distâncias a partir do tipo especificado.
    return result

  def normalize(self, values):
    """ Processo básico de normalização dos dados, que usa das facilitações disponibilizadas pelos arrays numpy. """
    mins, maxs = numpy.min(values, axis=0), numpy.max(values, axis=0)  # Vetores com os mínimos e máximos de cada coluna de dados.
    return (values - mins) / (maxs - mins)
