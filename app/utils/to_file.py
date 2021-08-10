class ToFile:
  def __init__(self, path, data):
    maxs = [len(x) + 4 for x in data.legend]
    with open(path, 'w') as file:
      file.write('id' + (' ' * 6))
      for index, element in enumerate(data.legend):
        file.write(element + (' ' * (maxs[index] - len(element))))
      file.write('group')
      file.write('\n')
      for index, element in enumerate(data.values):
        spaces = ' ' * (8 - len(f'{index + 1}'))
        file.write(f'{index + 1}{spaces}')
        for i, e in enumerate(element):
          spaces = (' ' * (maxs[i] - len(f'{e}')))
          file.write(f'{e}{spaces}')
        if len(data.groups) > 0:
          file.write(data.groups[index])
        file.write('\n')
