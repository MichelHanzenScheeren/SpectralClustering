from app.algorithm.distance import Distance, DistanceType


class DistanceMatrix:
  def __init__(self, values, type):
    self.values = values
    self.type = type

  def generate(self):
    result = []
    for i, value1 in enumerate(self.values):
      line = []
      for j, value2 in enumerate(self.values):
        if j == i: line.append(0)
        elif j < i: line.append(result[j][i])
        else: line.append(Distance(value1, value2).solve(self.type))
      result.append(line)
    return result
