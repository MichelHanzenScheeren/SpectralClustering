from app.utils.acuracy import Acuracy
from app.algorithm.spectral_clustering import SpectralClustering
from app.utils.from_file import FromFile
from sys import argv


def run():
  try:
    if len(argv) < 2: raise RuntimeError()
    numberOfClusters, distanceType, neighbors, path = getArguments(argv[1:])
    data = FromFile(path).convert()
    classifiedGroups = SpectralClustering(numberOfClusters, distanceType, neighbors).generate(data.values)
    acuracy = Acuracy(data.groups, classifiedGroups).calculate()
    print(f'Precisão: {acuracy:.2f}%')
  except FileNotFoundError:
    print('O arquivo informado não é valido')
  except RuntimeError as error:
    expectedArguments(error)
  except Exception as error:
    print(error)


def expectedArguments(error):
  if str(error) == '': print('Parâmetro obrigatório ausente.')
  print('\t(OBRIGATÓRIO) <path_arquivo_de_entrada.txt>')
  print('\t(OPCIONAL) -k <numero_de_clusters> (padrão: 2)')
  print('\t(OPCIONAL) -d <medida_de_distancia> (padrão: 2)')
  print('\t\t0 (suprema); 1 (manhattan); 2 (euclidiana)')
  print('\t(OPCIONAL) -n <numero_de_vizinhos_knn> (padrão: 8)')


def getArguments(arguments):
  k, d, n, path = None, None, None, None
  if arguments[0] == '-h': raise RuntimeError('-h')
  while len(arguments) > 0:
    current = arguments.pop(0)
    if current == '-k': k = getIntArgument(arguments, current)
    elif current == '-d': d = getIntArgument(arguments, current)
    elif current == '-n': n = getIntArgument(arguments, current)
    else: path = getFileArgument(current)
  if path is None: raise RuntimeError()
  return (k, d, n, path)


def getIntArgument(arguments, current):
  if len(arguments) == 0 or not arguments[0].isnumeric():
    raise Exception(f'Argumento inválido. Esperava um valor inteiro positivo depois de {current}')
  return int(arguments.pop(0))


def getFileArgument(argument):
  with open(argument, "r"):  # Check if file exists and can be decoded
    return argument


# INICIO DA EXECUÇÃO
run()
