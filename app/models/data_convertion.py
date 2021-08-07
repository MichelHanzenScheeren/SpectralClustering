class DataConvertion:
  def __init__(self, text):
    self.text = text
    self.legend = None
    self.id_index = -1
    self.ids = []
    self.group_index = -1
    self.groups = []
    self.data = []

  def convert(self, clean=True):
    lines = self.text.split('\n')
    for index in range(len(lines)):
      currentLine = lines[index].replace('\t', '').replace('\r', '')
      elements = currentLine.split(' ')
      for _ in range(elements.count('')): elements.remove('')
      if len(elements) > 0: self.saveElement(elements, index)
    if clean: self.clean()
    for e in self.data:
      print(e)
    print(self.legend)

  def saveElement(self, elements, index):
    if index == 0:
      if elements[0].replace('.', '', 1).isdigit(): self.legend = ['Unkown'] * len(elements)
      else:
        if elements.count('id') != 0:
          self.id_index = elements.index('id')
          elements.pop(self.id_index)
        if elements.count('group') != 0:
          self.group_index = elements.index('group')
          elements.pop(self.group_index)
        self.legend = elements
    else:
      converted = []
      for index, element in enumerate(elements):
        if self.id_index == index: self.ids.append(element)
        elif self.group_index == index: self.groups.append(element)
        elif element.isdigit(): converted.append(int(element))
        elif element.replace('.', '', 1).isdigit(): converted.append(float(element))
        else: converted.append('-1')
      self.data.append(converted)

  def clean(self):
    self.data = list(filter(lambda x: len(x) == len(self.legend), self.data))
