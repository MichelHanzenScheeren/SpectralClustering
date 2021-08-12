from app.utils.data import Data


class FromFile:
  """ Classe que encapsula a lógica de obtenção dos dados a partir do arquivo de dataset. """

  def __init__(self, path):
    self.path = path  # Caminho (relativo ou absoluto) do arquivo de dataset.
    self.validColumns = -1  # Quantidade de colunas válidas, usado para remover colunas que tenham dados ausentes.
    self.columnOfIds = -1  # Index da coluna que contêm o id dos dados.
    self.columnOfGroups = -1  # Index da coluna que contêm o grupo dos dados.
    self.legend = []
    self.ids = []
    self.groups = []
    self.values = []

  def convert(self):
    with open(self.path) as file:
      for line in file:
        # lista a partir de cada linha do arquivo, após quebrá-la em partes separadas a partir de espaços em branco. Remove caracteres especiais.
        elements = list(filter(lambda x: x not in ['\t', '\n', '\r', ''], line.strip().split(' ')))
        if len(elements) == 0: continue  # Ignorar linhas em branco
        elif len(self.legend) == 0: self.saveLegend(elements)  # Se ainda não rejistrou a legenda, tenta
        else: self.saveElements(elements)  # registra cada linha de valores do arquivo
    return Data(self.legend, self.ids, self.groups, self.values)  # Gera a a instância da classe Data a partir das listas criadas.

  def saveLegend(self, elements):
    self.validColumns = len(elements)  # A legenda (ou primeira linha) é usada como parâmetro para saber a qtd de colunas válidas.
    if self.isValidValue(elements[0]):  # Caso a primiera linha ja seja de dados (não possui legenda)
      self.legend = [f'column_{x}' for x in range(len(elements))]  # Gera uma legenda simplificada
      self.saveElements(elements)  # Como a primeira linha já é de dados, encaminha para que seja salva como dado.
    else:  # Se vier pra cá, possui legenda.
      if elements.count('id') != 0:   # Se possui coluna de ids, registra para que esta possa ser removida dos dados.
        self.columnOfIds = elements.index('id')
        elements.pop(self.columnOfIds)
      if elements.count('group') != 0:  # Se possui coluna de grupos, registra para que esta possa ser removida dos dados.
        self.columnOfGroups = elements.index('group')
        elements.pop(self.columnOfGroups)
      self.legend = elements

  def saveElements(self, elements):
    # Se linha do arquivo possui coluna que não é numérica ou se um dado estiver ausente, ignora essa linha
    if len(elements) != self.validColumns or len([x for x in elements if self.isValidValue(x)]) != self.validColumns: return
    if self.columnOfIds != -1: self.ids.append(elements.pop(self.columnOfIds))  # Se possui coluna de ids, remove dos dados e salva na lista de ids.
    if self.columnOfGroups != -1: self.groups.append(elements.pop(self.columnOfGroups))  # Se possui coluna de grupos, remove dos dados e salva na lista de grupos.
    self.values.append([self.convertValue(x) for x in elements])  # Cria uma lista com cada coluna restante, conv. para float e as salva em uma lista de valores.

  def isValidValue(self, value):
    return value.replace('.', '', 1).replace('-', '', 1).isdigit()

  def convertValue(self, value):
    if value.replace('-', '', 1).isdigit(): return int(value)
    return float(value)
