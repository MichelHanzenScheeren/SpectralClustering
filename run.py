from app.utils.acuracy import Acuracy
from app.algorithm.spectral_clustering import SpectralClustering
from app.utils.from_file import FromFile
from sys import argv


def run():
  try:
    if len(argv) < 2: return expectedArguments()
    numberOfClusters, distanceType, neighbors, path = getArguments(argv[1:])
    data = FromFile(path).convert()
    classifiedGroups = SpectralClustering(numberOfClusters, distanceType, neighbors).generate(data.values)
    acuracy = Acuracy(data.groups, classifiedGroups).calculate()
    print(f'Precisão: {acuracy}%\n')
    print(data.groups, '\n\n')
    print(classifiedGroups)
  except FileNotFoundError:
    print('O arquivo informado não é valido')
  except Exception as error:
    print(error)


def expectedArguments():
  print('Parâmetro obrigatório ausente.')
  print('\t<path_completo_entrada.txt> (OBRIGATÓRIO)')
  print('\t-k <numero_de_vizinhos> (OPCIONAL)')
  print('\t-d <medida_de_distancia> (OPCIONAL)')
  print('\t\t0 - suprema; 1 - manhattan; 2 - euclidiana')


def getArguments(arguments):
  k, d, n, path = None, None, None, None
  while len(arguments) > 0:
    current = arguments.pop(0)
    if current == '-k': k = getIntArgument(arguments, current)
    elif current == '-d': d = getIntArgument(arguments, current)
    elif current == '-n': n = getIntArgument(arguments, current)
    else: path = getFileArgument(current)
  return (k, d, n, path)


def getIntArgument(arguments, current):
  if len(arguments) == 0 or not arguments[0].isnumeric():
    raise Exception(f'Argumento inválido. Esperava um valor inteiro depois de {current}')
  if current == '-k' or current == '-n':
    newArgument = int(arguments.pop(0))
    if newArgument == 0:
      raise Exception(f'Argumento inválido. Esperava que "{current}" fosse maior do que zero')
    return newArgument
  newArgument = int(arguments.pop(0))
  if newArgument not in [0, 1, 2]:
    raise Exception(f'Argumento inválido. Esperava que "-d" fosse 0, 1 ou 2 (informado: {newArgument})')
  return newArgument


def getFileArgument(argument):
  with open(argument, "r"):  # Check if file exists and can be decoded
    return argument


# INICIO DA EXECUÇÃO
run()
