import os
from datetime import datetime
from time import sleep


def linha(tam = 62):
    return '~' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(62))
    print(linha())
    return

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRRRRRRRRROU Mamão...é numero não letra!')
        except(KeyboardInterrupt):
            print('o usuário preferiu não digitar esse número')
            return 0
        else:
            return n

def menu_iterativo(lista):
    cabeçalho('Filter -> Flipper -> Omega')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc


def list_append(arq):
    c = 1
    param = []
    for name in arq:
        print(f'{c} - {name}')
        c += 1
        param.append(name)
    print(linha())
    return param


def findfiles_ByExtension(path, *args):
    filenames = os.listdir(path)
    return [filename for filename in filenames if filename.endswith(args) or filename.endswith(args)]

def find_files_ByPrefix(path, *args):
    filenames = os.listdir(path)
    return [filename for filename in filenames if filename.startswith(args) or filename.startswith(args)]

def DataHora(processo):
    now = datetime.now()
    dia = now.strftime('%d.%m.%Y')
    hora = now.strftime('%H:%M:%S')
    return f'O Processo foi iniciado para {processo}\nno dia {dia} - {hora}h\n\n\n'

def CriarDiretorio(path, name):
    path_out_bases = os.path.join(path, name)
    [os.makedirs(i, exist_ok=True) for i in [path_out_bases]]



bases_baixadas = findfiles_ByExtension(os.path.join(os.getcwd()
                                                    )
                                       ,'.mol2'
                                       ,'.sdf'
                                       )



omega_param = findfiles_ByExtension(os.path.join(os.getcwd()
                                                 )
                                    ,'.parm'
                                    )



filtros_filter = find_files_ByPrefix(os.path.join(os.getcwd()
                                                  )
                                     ,'filtro'
                                     )







