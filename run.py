from app.algorithm.adjacency_matrix import AdjacencyMatrix
from app.algorithm.similarity_matrix import SimilarityMatrix
from app.algorithm.distance import DistanceType
from app.algorithm.distance_matrix import DistanceMatrix
from sys import argv


def run():
  try:
    if len(argv) < 2: return expectedArguments()
    k, d, _ = getArguments(argv[1:])
    numbers = [[1, 2], [3, 7], [2, 0], [6, 3]]
    matrix = DistanceMatrix(numbers, type=DistanceType.Supreme).generate()
    for line in matrix:
      print(line)
    print()
    matrix = AdjacencyMatrix(matrix, neighbors=1).generate()
    for line in matrix:
      print(line)
    print(f'\nk: {k}, d: {d}')
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
  k, d, text = None, None, None
  while len(arguments) > 0:
    current = arguments.pop(0)
    if current == '-k' or current == '-d':
      k, d = getIntArguments(arguments, current, k, d)
    else:
      text = getFileArgument(current)
  return (k, d, text)


def getIntArguments(arguments, current, k, d):
  if len(arguments) == 0 or not arguments[0].isnumeric():
    raise Exception(f'Argumento inválido. Esperava um valor inteiro depois de {current}')
  if current == '-k':
    k = int(arguments.pop(0))
    if k == 0:
      raise Exception(f'Argumento inválido. Esperava que "k" fosse maior do que zero')
    return k, d
  d = int(arguments.pop(0))
  if d not in [0, 1, 2]:
    raise Exception(f'Argumento inválido. Esperava que "d" fosse 0, 1 ou 2 (informado: {d})')
  return k, d


def getFileArgument(argument):
  with open(argument, "r"):  # Check if file exists and can be decoded
    return argument


# INICIO DA EXECUÇÃO
run()
