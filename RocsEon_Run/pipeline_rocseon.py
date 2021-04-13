from __init__ import *
from time import sleep
import subprocess
import shutil
from fnmatch import fnmatch
from datetime import datetime
import os
import smtplib

# Para as funções do Menu

while True:
    resposta = menu(['IMPORTANTE!!! Leia antes de Usar', 'Ver Bases', 'Rodar Rocs e Eon', 'Sair do ROCS/EON RUN'])

# Resposta 1 abre o txt de instruções

    if resposta == 1:
        file = open('Leia_me.txt', 'r')
        print('\n O que o app faz\n')
        print(file.read())
        file.seek(0)
        file.close()

    elif resposta == 2:
# Resposta 2 lista as bases

# Procurar as palaras 300 ou 200 ou 100 entre os arquivos presentes nos sudiretorios de D:\Bases_de_dados e listar

        name = WalkDirs_ListPattern('*100*', '*200*', '*300*', os.path.join('D:\\', 'Bases_de_Dados') )
        c = 1
        for lst in name:
            print(f'{c} - {lst}')
            c += 1
            sleep(0.01)

    elif resposta == 3:

# Resposta que ira rodar os programas

        nome_usuario = str(input('Definir o usuário - O mesmo nome que está em sua pasta: '))
        nome_projeto = str(input('De um nome para o seu projeto, ele será impresso nas pastas de Reultados: '))

#Sim e não para e-mail

        envia_email = input(str('Gostaria de receber um e-mail quando o seu processo terminar? [s/n]')).strip().upper()
        print()
        if envia_email =='S':
            email = str(input('Por favor digite seu email: '))
            cabeçalho('Beleuza, quando o processo acabar enviaremos um email de'
                      '\nlcqfusp@gmail.com com o assunto: Processo Rocs e Eon'
                      '\nVamos continuar a brincadera! ')
            sleep(5)

        elif envia_email =='N':
            print(linha())
            print('Eeeeeeeeeeita, blz sem ressentimentos'
                  '\nVamos prosseguir! ')
            print(linha())
            sleep(3)

        elif (ValueError, TypeError):
            cabeçalho('ERRRRROOOUUUU: Presta atenção cabeção, essa opção não existe! \nVamos ter que começar de novo!')
            sleep(3)
            continue

        cabeçalho('Bases Disponíveis')

# listar bases quem contém 200 ou 300 no nome em todos os subdretórios a partir de Base_de_Dados
# Apresentar a lista ao usuário
# Abrir uma lista para o nome das bases outra para os endereços

        pattern1 = '*300*'
        pattern2 = '*200*'
        pattern3 = '*100*'
        c = 1
        name_base = []
        end_base = []
        for root, dirs, files in os.walk(os.path.join('D:\\', 'Bases_de_Dados')):
            for name in files:
                if fnmatch(name, pattern1) or fnmatch(name, pattern2) or fnmatch(name, pattern3):
                    print(f'{c} - {name}')
                    c += 1
                    sleep(0.01)

# juntar todos os resultados em listas de nomes e endereços

                    name_base.append(name)
                    end_base.append(os.path.join(root,name))
                    # print(name_base) # se necessario conferir se o grupo foi criado


        cabeçalho('Quais bases deseja utilizar em seu estudo? (Separe por virgula) ')

# selecionar bases dentro da lista a serem usadsa no estudo

        #base_proj = []
        end_proj = []
        w = input()
        # print(w.split(',')) #Se necessario conferir
        cabeçalho('As bases selecionadas para este estudo foram: ')
        list = w.split(',')
        for i in list:
            x = int(i) - 1
            print(name_base[x])
            #print(end_base[x])

# Juntar as bases selecionadas (name_base) em uma lista (base_proj)


            end_proj.append(end_base[x])

# Pedir para o usuario chegar as bases

        print(linha())
        k = str(input('Correto? Podemos prosseguir? [s/n] '))
        print()
        if k == 'n':
            cabeçalho('Eeeeeeeeeeeeeeelaia!!!\nTuuuudo de novo!!!!')
            sleep(3)
            continue

        elif k == 's':

#Obter as tags utilizadas pelos programas

            y = str(input('Digite o endereço completo onde seu query se encontra?\n(Ex.: D:\Leo\RocsEon\MDH): '))
            z = str(input('qual o nome do seu query, não esqueça a extensão?\n(Ex.: malato.mol2): '))
            f = str(input('quantos hits deseja obter para o ROCS? '))
            g = str(input('e para o EON? '))
            h = str(input('Qual a extensão que você deseja seus resultados?'
                          '\nEx.: sdf mol2 oeb - NÃO colocar PONTO: '))
            cabeçalho('Belezua cabeção...\nSe aparecer o logo da OpenEye esta tudo ok!!!'
                      '\nPode descer na cantina e se deliciar com um bolin'
                      '\nAh aproveita vai ali na copa e prepara um café pra gente')
            sleep(5)

# Criar diretório para os resultados do ROCS na pasta do usuário

            directory = '[Results]Rocs_' + str(nome_projeto)  # Pode colocar a data
            parent_dir = 'D:\\' + str(nome_usuario)
            path_out_rocs = os.path.join(parent_dir, directory)
            [os.makedirs(i, exist_ok=True) for i in [path_out_rocs]]

# hora de inicio

            now = datetime.now()
            day_inicio_proces = now.strftime('%d.%m.%Y')
            hour_inicio_proces = now.strftime('%H:%M:%S')

# Loop das bases no ROCS Files

            for base in end_proj:

# Apresentar no terminal Data e hora de inicio para cada processo do ROCS
                #i = os.path.basename(os.path.join(base))
                file_name = os.path.basename(os.path.join(base))
                index_of_dot = file_name.index('.')
                i = file_name[:index_of_dot]
                onlyname = i.split(']')[1]
                ligname = z.split('.')[0]
                now = datetime.now()
                day_inicio = now.strftime('%d.%m.%Y')
                hour_inicio = now.strftime('%H:%M:%S')
                print(linha())
                print()
                print('Iniciado para a base', i)
                print('dia {} as {}'.format(day_inicio, hour_inicio))
                print()
                print(linha())

# Criar arquivo txt para enviar datas e horas de cada processo

                arquivo = open('time_process.txt', 'a')
                arquivo.writelines(['\nProcesso iniciado para a base: ', i,
                                    '\nno dia {} as {}'.format(day_inicio, hour_inicio),
                                    '\n',
                                    ])
                arquivo.close()

# Process_ROCS

                subprocess.run(['rocs.bat',
                                '-dbase', os.path.join(base),
                                '-query', os.path.join(y, z),
                                '-outputdir', os.path.join(path_out_rocs),
                                '-prefix', '[ROCS_' + ligname + ']' + onlyname,
                                '-oformat', h,
                                '-besthits', f,
                                '-mpi_np', '8'
                                ])
#Fim do loop do Rocs inicio do EON
# Criar diretório para os resultados do EON

            directory = '[Results]EON_' + str(nome_projeto)
            parent_dir = 'D:\\' + str(nome_usuario)
            path_out_eon = os.path.join(parent_dir, directory)
            [os.makedirs(i, exist_ok=True) for i in [path_out_eon]]

# Procurar os resultados do ROCS pela extensão .mol2 e fazer uma lista (rocs_results) para a entrada no EON

            rocs_results = findfiles_ByExtension(os.path.join(path_out_rocs), extension= h, )

            # print(rocs_results) #se precisar de um confere

# Loop para rodar os Resultados do ROCS no EON

            for hits_rocs in rocs_results:

# Data e hora para cada processo do Eon

                now = datetime.now()
                day_inicio = now.strftime('%d.%m.%Y')
                hour_inicio = now.strftime('%H:%M:%S')
                print(linha())
                print()
                print('Iniciado para - ', hits_rocs)
                print('dia {} as {}'.format(day_inicio, hour_inicio))
                print()
                print(linha())

# Escrever data e hota EON no arquivo de texto ja criado (time_process)

                arquivo = open('time_process.txt', 'a')
                arquivo.writelines(['\nProcesso iniciado para a base: ' + hits_rocs,
                                    '\nno dia {} as {}'.format(day_inicio, hour_inicio),
                                    '\n'])
                arquivo.close()

# Process_EON
                hits_eon = hits_rocs.split(']')[1].split('_hits')[0]
                subprocess.run(['eon.bat',
                                '-dbase', os.path.join(path_out_rocs, hits_rocs),
                                '-query', os.path.join(y, z),
                                '-prefix', '[EON_' +ligname+ ']'+ hits_eon,
                                '-oformat', h,
                                '-besthits', g,
                                '-mpi_np', '8'
                                ])

# Procurar os resultados do EON pelo profixo e fazer uma lista para move-los ao diretorio de resultados

            find_prefix = findfiles_ByPrefix(os.path.join('D:\\', 'openeye', 'ROCS_RUN'), '[EON')

# Mover arquivos

            for results in find_prefix:
                shutil.move(os.path.join('D:\\', 'openeye', 'ROCS_RUN', results), path_out_eon)

# Mensagem com o  fim do processo
            now = datetime.now()
            day_final = now.strftime('%d.%m.%Y')
            hour_final = now.strftime('%H:%M:%S')
            print(linha())
            print('O aplicativo "EON" terminou de rodar para todos os arquivos listados')
            print('Inicio em {} ás {}'.format(day_inicio_proces, hour_inicio_proces))
            print('Finalizado em {} às {}'.format(day_final, hour_final))

# Escrever mensagem final no arquivo txt

            arquivo = open('time_process.txt', 'a')
            arquivo.writelines(['\nO aplicativo "EON" terminou de rodar para todos os arquivos listados',
                                '\nInicio em {} ás {}'.format(day_inicio_proces, hour_inicio_proces),
                                '\nFinalizado em {} às {}'.format(day_final, hour_final)])
            arquivo.close()

# enviar email
            if envia_email == 'S':
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login('login', 'senha')
                server.sendmail(
                    'email',
                    str(email),
                    'seu processo Rocs/ Eon finalizou'
                )
                server.quit()
            elif envia_email == 'N':
                continue

# Procurar pelo arquivo de texto com o prefixo 'time'

            find_prefix = findfiles_ByPrefix(os.path.join('D:\\', 'openeye', 'ROCS_RUN'), 'time')

# Mover o arquivo para a pasta de resultados do EON
            for results in find_prefix:
                shutil.move(os.path.join('D:\\', 'openeye', 'ROCS_RUN', results), path_out_eon)

#Resultado para a resposta 4

    elif resposta == 4:
        cabeçalho('Saindo do sistema...Abraaaaaaaas!')
        sleep(5)
        break

    else:
        print('Aeeeeeeee cabeção...presta atenção e digita um número correto')
        sleep(2)
