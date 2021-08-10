from app.utils.data import Data


class FromFile:
  def __init__(self, path):
    self.path = path
    self.validColumns = -1
    self.columnOfIds = -1
    self.columnOfGroups = -1
    self.legend = []
    self.ids = []
    self.groups = []
    self.values = []

  def convert(self):
    with open(self.path) as file:
      for line in file:
        elements = list(filter(lambda x: x not in ['\t', '\n', '\r', ''], line.strip().split(' ')))
        if len(elements) == 0: continue
        elif len(self.legend) == 0: self.saveLegend(elements)
        else: self.saveElements(elements)
    return Data(self.legend, self.ids, self.groups, self.values)

  def saveLegend(self, elements):
    self.validColumns = len(elements)
    if self.isValidValue(elements[0]):
      self.legend = [f'column_{x}' for x in range(len(elements))]
    else:
      if elements.count('id') != 0:
        self.columnOfIds = elements.index('id')
        elements.pop(self.columnOfIds)
      if elements.count('group') != 0:
        self.columnOfGroups = elements.index('group')
        elements.pop(self.columnOfGroups)
      self.legend = elements

  def saveElements(self, elements):
    if len(elements) != self.validColumns or len([x for x in elements if self.isValidValue(x)]) != self.validColumns: return
    if self.columnOfIds != -1: self.ids.append(elements.pop(self.columnOfIds))
    if self.columnOfGroups != -1: self.groups.append(elements.pop(self.columnOfGroups))
    self.values.append([self.convertValue(x) for x in elements])

  def isValidValue(self, value):
    return value.replace('.', '', 1).replace('-', '', 1).isdigit()

  def convertValue(self, value):
    if value.isdigit(): return int(value)
    return float(value)
