from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for item in instance._data:
        if item["nome_do_arquivo"] == path_file:
            return None  # 3.1

    string_file = txt_importer(path_file)

    structured_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(string_file),
        "linhas_do_arquivo": string_file,
    }

    instance.enqueue(structured_data)

    sys.stdout.write(f"{structured_data}")


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance._data) == 0 or not instance:
        return sys.stdout.write("Não há elementos")

    deleted_item = instance.dequeue()
    path_file = deleted_item["nome_do_arquivo"]

    sys.stdout.write(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
