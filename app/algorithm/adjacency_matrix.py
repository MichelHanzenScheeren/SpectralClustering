class AdjacencyMatrix:
  """ Classe que gera a matriz de adjacência a partir da matriz de distâncias.
  É uma matriz nXn em que cada linha possui valor '1' para os n-vizinhos mais próximos do ponto n, e '0' para todos os outros. """

  def __init__(self, distanceMatrix, neighbors):
    self.distanceMatrix = distanceMatrix
    self.neighbors = neighbors

  def generate(self):
    # A quantidade de vizinhos será o parâmetro recebido se existirem dados suficientes para isso, se não será o tamanho do vetor.
    self.neighbors = self.neighbors if (self.neighbors < len(self.distanceMatrix) - 1) else (len(self.distanceMatrix) - 1)
    for i, line in enumerate(self.distanceMatrix):
      indexList = [x for x in range(len(line))]  # Gera uma lista de indices, de 0 .. qtd de dados.
      ordereds = [x for _, x in sorted(zip(line, indexList))]  # Ordena a lista de indices a partir das distâncias da matriz de distâncias.
      selecteds = ordereds[:self.neighbors + 1]  # Peka os n vizinhos definidos do parâmetro (+ 1 pois o vizinho mais próximo é o próprio ponto)
      for j in range(len(line)):  # Se está na lista dos vizinhos mais próximos, recebe 1, do contrário 0.
        if j != i and j in selecteds: line[j] = 1
        else: line[j] = 0
    return self.distanceMatrix  # A matriz de adjacência sobrescreve a matriz de distância, ja que a mesma não seria mais usada.
