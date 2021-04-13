import argparse
import os
import subprocess
import shutil


def findfiles_ByExtension(path, *args):
    filenames = os.listdir(path)
    return [filename for filename in filenames if filename.endswith(args) or filename.endswith(args)]

def find_files_ByPrefix(path, *args):
    filenames = os.listdir(path)
    return [filename for filename in filenames if filename.startswith(args) or filename.startswith(args)]


parser = argparse.ArgumentParser()

parser.add_argument('-db', '--database', help='all or list')
parser.add_argument('-q', '--query', help='Path Query')
parser.add_argument('-bhr', '--besthitsrocs', help='Number of ROCS best Hits')
parser.add_argument('-bhe', '--besthitseon', help='Number of EON best Hits')
parser.add_argument('-oformat', '--oformat', help='output format')
parser.add_argument('-mpi_np', '--mpi_mp', help='Number of Processors')

args = parser.parse_args()

if args.database == 'list':
    all_bases = findfiles_ByExtension(os.path.join('../Filter_Flipper_Omega/lib'
                                                   )
                                      , '.mol2'
                                      , '.sdf'
                                      )
    c = 0
    base_project = []
    print('Select datbases: ')
    for base in all_bases:
        print(f'{c} - {base}')
        c += 1
    choice = input()
    list = choice.split(',')
    for number in list:
        number_int = int(number)
        base_project.append(all_bases[number_int])

elif args.database == 'all':
    base_project = findfiles_ByExtension(os.path.join('../Filter_Flipper_Omega/lib'
                                                   )
                                      , '.mol2'
                                      , '.sdf'
                                      )
directory = '[Results]Rocs_EON'
path_out_rocs = os.path.join(os.getcwd(), directory)
[os.makedirs(i, exist_ok=True) for i in [path_out_rocs]]

for base in base_project:
    directory = '[Results]_'+ base.split('.')[0]
    path_out_base = os.path.join(path_out_rocs, directory)
    [os.makedirs(i, exist_ok=True) for i in [path_out_base]]

    subprocess.run(['rocs.bat',
                    '-dbase', base,
                    '-query', os.path.join(args.query),
                    '-outputdir', os.path.join(path_out_base),
                    '-prefix', 'Results_ROCS',
                    '-oformat', args.oformat,
                    '-besthits', args.besthitsrocs,
                    '-mpi_np', args.mpi_mp
                    ])

    subprocess.run(['eon.bat',
                    '-dbase', 'Results_ROCS' + args.oformat,
                    '-query', os.path.join(args.query),
                    '-prefix', 'Results_EON',
                    '-oformat',args.oformat,
                    '-besthits', args.besthitseon,
                    '-mpi_np', args.mpi_mp
                    ])
    find_prefix = findfiles_ByPrefix(os.path.join(os.getcwd()), 'Results_ROCS', 'Results_EON')
    for results in find_prefix:
        shutil.move(os.path.join(os.getcwd(), results), path_out_base)





