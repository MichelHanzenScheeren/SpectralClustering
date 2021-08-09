class AdjacencyMatrix:
  def __init__(self, distanceMatrix=[], neighbors=8):
    self.distanceMatrix = distanceMatrix
    self.neighbors = neighbors

  def generate(self):
    for i, line in enumerate(self.distanceMatrix):
      neighbors = self.neighbors if (self.neighbors < len(line) - 1) else (len(line) - 1)
      indexList = [x for x in range(len(line))]
      ordereds = [x for _, x in sorted(zip(line, indexList))]
      selecteds = ordereds[:neighbors + 1]
      for j in range(len(line)):
        if j != i and j in selecteds: line[j] = 1
        else: line[j] = 0
    return self.distanceMatrix
