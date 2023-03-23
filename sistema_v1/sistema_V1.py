from sistema_v1.lib.interface import *
from sistema_v1.lib.arquivo import *
import time

arq = 'list_sistem_V1.txt'

if not arquivoExiste(arq):
      criarArquivo(arq)

while True:
      resposta = menu(['Cadastrar novo usuario',
                      'Ver lista de usuarios',
                      'Sair do programa'])

      if resposta == 1:
            cabeçalho('Cadastrar novo usuario')
      elif resposta == 2:
            cabeçalho('Lista de usuarios')
      elif resposta == 3:
            cabeçalho('Saindo do sistema... Até logo!')
            time.sleep(2)
            break
      else:
            print('\n\033[31mERRO! Digite uma opção válida!')
      time.sleep(2)
