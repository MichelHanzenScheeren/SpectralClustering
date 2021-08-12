import numpy


class Data:
  """ Classe que separa e guarda os dados obtidos a partir do arquivo de dataset. """

  def __init__(self, legend, ids, groups, values):
    self.legend = legend
    self.ids = ids
    self.groups = groups
    self.values = numpy.array(values)
