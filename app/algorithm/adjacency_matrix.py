class AdjacencyMatrix:
  def __init__(self, distanceMatrix, neighbors):
    self.distanceMatrix = distanceMatrix
    self.neighbors = neighbors

  def generate(self):
    self.neighbors = self.neighbors if (self.neighbors < len(self.distanceMatrix) - 1) else (len(self.distanceMatrix) - 1)
    for i, line in enumerate(self.distanceMatrix):
      indexList = [x for x in range(len(line))]
      ordereds = [x for _, x in sorted(zip(line, indexList))]
      selecteds = ordereds[:self.neighbors + 1]
      for j in range(len(line)):
        if j != i and j in selecteds: line[j] = 1
        else: line[j] = 0
    return self.distanceMatrix
