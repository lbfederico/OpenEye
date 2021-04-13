from __init2__ import *
import os
from time import sleep
import subprocess
from datetime import datetime
import shutil
import smtplib

def principal():

    #pergunta para o email
    while True:
        envio_email = str(input('Antes de começarmos, '
                      '\ngostaria de receber um e-mail quando o seu processo terminar? [s/n]')).strip().upper()
        print()
        if envio_email == 'S':
            email = str(input('Por favor digite seu email: '))
            cabeçalho('Beleuza, quando o processo acabar enviaremos um email de'
                      f'\nlcqfusp@gmail.com com o assunto: {assunto}'
                      '\nVamos continuar a brincadera! ')
            sleep(1)
            break
        elif envio_email == 'N':
            print(linha())
            print('Eeeeeeeeeeita, blz sem ressentimentos'
                  '\nVamos prosseguir!')
            sleep(3)
            break
        else:
            cabeçalho('ERRRRRRRRRROU Mamão...'
                      '\n Presta atenção mané...só vale s ou n')

    # Listar as opções de filtros do filter
    cabeçalho('Os filtros disponíves para o Filter são:')
    param_f_proj = list_append(filtros_filter)

    # selecionar o filtro para o estudo
    print(linha())
    w = int(input('Qual filtro você deseja utilizar em seu estudo? '))
    y = int(w) - 1
    print(f'Sua Opção: {w} - {param_f_proj[y]}')  # So aquele confere - o parametro para a linha de comando será opçoes_param[y]
    sleep(2)

    # Apresentar as opções de parametros 300, 100, 25 e 3D
    cabeçalho('Para o OMEGA os parametros são: ')
    list_append(omega_param)

    # selecionar o parametro para o estudo com e sem ext
    print(linha())
    j = input('Qual(ais) parametro(s) você deseja utilizar?'
              '\n(Separar por virgulas. Ex.: 1, 2) ').split(',')
    print(linha())
    print('Ok! Seguiremos os estudos com os paramentros: ')

    param_o_proj = []
    param_without_extension = []
    for x in j:
        k = int(x) - 1
        param_o_proj.append(omega_param[k]) # juntar os parametros que irão ser utilziados em uma lista

    # retirar o .parm
    for x in param_o_proj:
        z = x.split('.')[0]
        print(z)
        param_without_extension.append(z)
    sleep(3)

    # Listar as bases disponiveis para o preparo
    cabeçalho('As bases processadas serão: ')
    list_append(bases_baixadas)
    sleep(2)
    cabeçalho('Belezua cabeção...\nSe aparecer o logo da OpenEye esta tudo ok!!!'
              '\nPode descer na cantina e se deliciar com um bolin'
              '\nAh aproveita vai ali na copa e prepara um café pra gente')
    sleep(2)

    # Colocar data e hora para o inicio do processo
    x = DataHora('preparo das bases')
    print(x)

    # Loop para cada base de dados
    for bases in bases_baixadas:

        # Colocar data e hora de início para cada base e obter year para nome do diretório
        now = datetime.now()
        year = now.strftime('%Y_')
        x = DataHora(bases)
        cabeçalho(x)

        # Criar arquivo txt para data e hora
        with open('PreparoBases.txt', 'a') as f:
            f.writelines(x)

        # Separar os nomes das bases das extensões
        index_of_dot = bases.index('.')
        bases_without_extension = bases[:index_of_dot]

        # Criar os diretorios (ano, nome da base)
        directory = str(year) + str(bases_without_extension)  # Se quiser é possível colocar a data
        parent_dir = '..\\'
        path_out_bases = os.path.join(parent_dir, directory)
        [os.makedirs(i, exist_ok=True) for i in [path_out_bases]]

        # Subdir Filter
        directory = 'Results_Filter'
        parent_dir = path_out_bases
        path_out_filter = os.path.join(parent_dir, directory)
        [os.makedirs(i, exist_ok=True) for i in [path_out_filter]]

        # Subdir para as bases baixadas
        directory = 'Baixada'
        parent_dir = path_out_bases
        path_out_baixada = os.path.join(parent_dir, directory)
        [os.makedirs(i, exist_ok=True) for i in [path_out_baixada]]

        # Start Filter
        subprocess.run(['filter.bat',
                        '-filter', param_f_proj[y],
                        '-in', bases,
                        '-out', 'filter_' + str(bases_without_extension) + '.oeb.gz',
                        ])

        # #Mover base baixada para o diretorio baixadas
        shutil.move(os.path.join(os.getcwd(),
                                 bases
                                ),
                                 path_out_baixada
                                )

        #Para cada parametro
        # Criar o diretorio Omega_Param
        for param in param_without_extension:
            directory = 'Omega_' + str(param)
            parent_dir = path_out_bases
            path_out_omega = os.path.join(parent_dir, directory)
            [os.makedirs(i, exist_ok=True) for i in [path_out_omega]]

            #Rodar o Omega
            subprocess.run(['omega2.bat',
                            '-in', 'filter_' + str(bases_without_extension) + '.oeb.gz',
                            '-out', 'omega_' + str(param) + '_' + str(bases_without_extension) + '.oeb.gz',
                            '-param', str(param) + '.parm',
                            '-flipper', 'true',
                            '-mpi_np', '8',
                            '-progress', 'percent'
                            ])

            #Procurar pelo prefix OMEGA e Oeomega
            find_prefix_omega = find_files_ByPrefix(os.path.join(os.getcwd()
                                                                 )
                                                                  , 'omega'
                                                                  , 'oeomega'
                                                    )

           #Mover tudo mundo que tem omega para o diretorio Omega do respectivo paramentro
            for omega_file in find_prefix_omega:
                shutil.move(os.path.join(os.getcwd(),
                                        omega_file
                                       ),
                                         path_out_omega
                            )

        #Procurar os arquivos gerados pelo Filter e mover para o respectivo diretorio
        find_prefix_filter = find_files_ByPrefix(os.path.join(os.getcwd()
                                                                      ),
                                                                        'filter'
                                                )
        for filter_file in find_prefix_filter:
            shutil.move(os.path.join(os.getcwd(),
                                                filter_file
                                     ),
                                                path_out_filter
                        )

    #Data e hora finais
    x = DataHora('para todas as bases')
    cabeçalho(x)

    # Criar arquivo txt para data e hora final
    with open('PreparoBases.txt', 'a') as f:
        f.writelines(x)

    # Enviar email ----->  Mudar o comando colocar anexo ---> Resolver esse problema pois se colocar n vai dar erro
    if envio_email == 'S':

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login('login', 'senha')
        server.sendmail("lcqfusp@gmail.com", str(email), 'OMEGA Terminou')
        server.quit()


    #Mover data e hora para a pasta da base
    find_prefix_time = find_files_ByPrefix(os.path.join(os.getcwd()
                                                        )
                                                         ,'PreparoBases'
                                          )

    destino = os.path.join(os.getcwd(), 'arquivos_times')
    for time in find_prefix_time:
        shutil.move(os.path.join(os.getcwd(),
                                 time
                                 ),
                                    destino
                    )

        cabeçalho('Seu processo terminou pode fechar o terminal'
                  '\nAbraaaaaaaaaaaaaaaaaaas')


# MENU#

while True:
# #Menu

    resposta = menu_iterativo(['Instruções e parametros',
                               'listar bases disponíveis para preparar',
                               'Preparar',
                               'Sair do Script'
                               ])

#Para a resposta 1 - abrir o txt de instruções
    if resposta == 1:
        with open('Instrucoes.txt', 'r') as f:
            f.read()
            f.seek(0)
            print(f.read())
            f.close()

# Resposta 2 = listar as bases deisponiveis para preparo
    elif resposta == 2:
        list_append(bases_baixadas)
        str(input('pressione ENTER para voltar ao menu principal'))
        # Não sei se essa é uma opção valida para voltar ao menu, seria interessante limpar o terminal e voltar c o menu

# Resposta 3 email e principal
    elif resposta == 3:
       principal()

# Resposta 4 = Sair
    elif resposta == 4:
        cabeçalho('Saindo do sistema...Abraaaaaaaas!')
        sleep(5)
        exit()


    else:
        print('Aeeeeeeee cabeção...presta atenção e digita um número correto')
        sleep(2)
