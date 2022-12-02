import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        print('Formato inválido', file=sys.stderr)
    try:
        with open(path_file, 'r') as patch:
            return patch.read().split('\n')
    except FileNotFoundError:
        # sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
