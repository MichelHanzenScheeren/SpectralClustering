import numpy


class Data:
  def __init__(self, legend, ids, groups, values):
    self.legend = numpy.array(legend)
    self.ids = numpy.array(ids)
    self.groups = numpy.array(groups)
    self.values = numpy.array(values)
