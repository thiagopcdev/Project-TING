import sys
import csv


def txt_importer(path_file):
    try:
        if 'txt' not in path_file:
            # sys.stderr.write('Formato inválido\n') outro método
            print('Formato inválido', file=sys.stderr)
        with open(path_file, 'r') as file:
            reader = csv.reader(file, delimiter='\n')
            list = []
            for row in reader:
                list.append(row[0])
            return list
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
