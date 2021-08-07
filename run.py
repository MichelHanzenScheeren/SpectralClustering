from app.models.data_convertion import DataConvertion
from sys import argv


def run():
  try:
    if len(argv) < 2:
      return expectedArguments()
    argv.pop(0)
    k, d, text = getArguments()
    DataConvertion(text).convert()
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


def getArguments():
  k, d, text = None, None, None
  while len(argv) > 0:
    argument = argv.pop(0)
    if argument == '-k' or argument == '-d':
      k, d = getIntArguments(argument, k, d)
    else:
      text = getFileArgument(argument)
  return (k, d, text)


def getIntArguments(argument, k, d):
  if len(argv) == 0 or not argv[0].isnumeric():
    raise Exception(f'Argumento inválido. Esperava um valor inteiro depois de {argument}')
  if argument == '-k':
    k = int(argv.pop(0))
    if k <= 0:
      raise Exception(f'Argumento inválido. Esperava que "k" fosse maior do que zero (informado: {k})')
    return k, d
  d = int(argv.pop(0))
  if d not in [0, 1, 2]:
    raise Exception(f'Argumento inválido. Esperava que "d" fosse 0, 1 ou 2 (informado: {d})')
  return k, d


def getFileArgument(argument):
  with open(argument, "r") as myFile:
    return myFile.read()


# INICIO DA EXECUÇÃO
run()
