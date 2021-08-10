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
  except RuntimeError:
    expectedArguments()
  except Exception as error:
    print(error)


def expectedArguments():
  print('Parâmetro obrigatório ausente.')
  print('\t<path_arquivo_de_entrada.txt> (OBRIGATÓRIO)', end='\n\n')
  print('\t-k <numero_de_clusters> (OPCIONAL - padrão: 2)')
  print('\t-d <medida_de_distancia> (OPCIONAL - padrão: 2)')
  print('\t\t0 - suprema; 1 - manhattan; 2 - euclidiana')
  print('\t-n <numero_de_vizinhos_knn> (OPCIONAL - padrão: 8)')


def getArguments(arguments):
  k, d, n, path = None, None, None, None
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
