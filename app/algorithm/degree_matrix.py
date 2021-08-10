class DegreeMatrix:
  def __init__(self, matrix):
    self.matrix = matrix = matrix

  def generate(self):
    result = []
    for i, line in enumerate(self.matrix):
      somatory = sum(line)
      newLine = [somatory if current == i else 0 for current in range(len(line))]
      result.append(newLine)
    return result
