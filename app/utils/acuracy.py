from sklearn import metrics


class Acuracy:
  def __init__(self, originalGroups, classifiedGroups):
    self.originalGroups = originalGroups
    self.classifiedGroups = classifiedGroups

  def calculate(self):
    return (metrics.rand_score(self.originalGroups, self.classifiedGroups) * 100)
