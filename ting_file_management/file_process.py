from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return None

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": (file),
    }

    print(f'{data}', file=sys.stdout)
    instance.enqueue(data)
    return data

def remove(instance):
    if instance.__len__() == 0:
        print(f'Não há elementos', file=sys.stdout)
    else:
        file_deleted = instance.dequeue()
        path_file = file_deleted['nome_do_arquivo']
        print(f'Arquivo {path_file} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
