from ting_file_management.file_management import txt_importer
import sys


def is_the_file_not_duplicate(path_file, instance):
    stats = True
    for file in instance.data:
        if file['nome_do_arquivo'] == path_file:
            stats = False
    return stats


def process(path_file, instance):

    file = txt_importer(path_file)
    file_name = path_file
    file_qnt = len(file)
    output = {
        "nome_do_arquivo": file_name,
        "qtd_linhas": file_qnt,
        "linhas_do_arquivo": file
    }

    if is_the_file_not_duplicate(path_file, instance):
        instance.enqueue(output)
        print(output, file=sys.stdout)


def remove(instance):
    if(instance.__len__() <= 0):
        return print('Não há elementos', file=sys.stdout)
    file_removed = instance.dequeue()
    path_removed = file_removed['nome_do_arquivo']
    print(f'Arquivo {path_removed} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    try:
        get_processed_file = instance.search(position)
        print(get_processed_file, file=sys.stdout)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
