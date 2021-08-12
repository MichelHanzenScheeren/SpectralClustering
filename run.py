from app.utils.to_file import ToFile
from app.utils.data import Data
from app.utils.acuracy import Acuracy
from app.algorithm.spectral_clustering import SpectralClustering
from app.utils.from_file import FromFile
from sys import argv
import numpy


def run():
  """ Método que inicia toda a lógica do programa """
  try:
    numberOfClusters, distanceType, neighbors, path = getArguments(argv[1:])  # Obtenção dos argumentos
    data = FromFile(path).convert()  # Conversão do arquivo para o formato de dado usado no programa
    spectral = SpectralClustering(numberOfClusters, distanceType, neighbors)  # Criação do cluster com os arg. de configuração
    classifiedGroups = spectral.generate(data.values)  # Execução. Recebe valores manipuláveis e devolve uma lista com os grupos classificados.
    newData = Data(data.legend, data.ids, classifiedGroups, data.values)  # Criação de classe "Data" com os novos grupos da classificação.
    ToFile(f'./output/saida_{path.split("/")[-1]}', newData)  # Geração do arquivo de saída.
    acuracy = Acuracy(data.groups, classifiedGroups).calculate()  # Precisão do algoritmo. REMOVER
    print(f'Precisão: {acuracy:.2f}%')  # Precisão do algoritmo. REMOVER
  except FileNotFoundError:
    print('O arquivo informado não é valido')
  except RuntimeError as error:
    expectedArguments(error)
  except Exception as error:
    print(error)


def expectedArguments(error):
  """ Descrição dos parâmetros aceitos na execução pelo terminal. """
  if str(error) == '': print('Parâmetro obrigatório ausente.')
  print('\t(OBRIGATÓRIO) <path_arquivo_de_entrada.txt>')
  print('\t(OPCIONAL) -k <numero_de_clusters> (padrão: 2)')
  print('\t(OPCIONAL) -d <medida_de_distancia> (padrão: 2)')
  print('\t\t0 (suprema); 1 (manhattan); 2 (euclidiana)')
  print('\t(OPCIONAL) -n <numero_de_vizinhos_knn> (padrão: 10)')


def getArguments(arguments):
  """ Método que encapsula a lógica de extração dos parâmetros. """
  if len(arguments) < 1: raise RuntimeError()
  k, d, n, path = None, None, None, None
  if arguments[0] == '-h': raise RuntimeError('-h')  # Mostra a lista de parÂmetros
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
