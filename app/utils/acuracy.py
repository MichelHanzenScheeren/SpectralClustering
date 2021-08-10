class Acuracy:
  def __init__(self, originalGroups, classifiedGroups):
    self.originalGroups = originalGroups
    self.classifiedGroups = classifiedGroups

  def calculate(self):
    currentLabels = {}
    errors = 0
    for i, value in enumerate(self.originalGroups):
      if currentLabels.get(f'{value}') is None:
        currentLabels[f'{value}'] = self.classifiedGroups[i]
      elif currentLabels[f'{value}'] != self.classifiedGroups[i]:
        errors += 1
        currentLabels[f'{value}'] = self.classifiedGroups[i]
    return (100 - (errors * 100 / len(self.originalGroups)))
