import os
from fnmatch import fnmatch

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRRRROOOUUUU: Presta atenção cabeção, essa opção não existe!!!')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n

def linha(tam = 80):
    return '~' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(80))
    print(linha())

def menu(lista):
    cabeçalho('ROCS EON Run')
    c = 1
    for item in lista:
        print('{} - {}'.format(c, item))
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc

def findfiles_ByExtension(path, extension):
    filenames = os.listdir(path)
    return [filename for filename in filenames if filename.endswith(extension)]

# Create list of files
#lista_bases = findfiles_ByExtension(
#    os.path.join('C:\\', 'Users', 'LeoRoke', 'Desktop', 'Artigo_tese'),
#    extension='.docx'
#)


def findfiles_ByPrefix(path, prefix):
    filenames = os.listdir(path)
    return [filename for filename in filenames if filename.startswith(prefix)]

find_prefix = findfiles_ByPrefix(os.path.join(os.getcwd()), 'EON')

def SearchFiles_andList(pattern1, pattern2, path):
    c = 1
    for root, dirs, files in os.walk(os.path.join(path)):
        for name in files:
            if fnmatch(name, pattern1) or fnmatch(name, pattern2):
                print('{} - {}'.format(c, name))
                c += 1
                sleep(0.01)