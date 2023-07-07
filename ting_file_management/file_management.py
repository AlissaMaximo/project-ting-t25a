import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if path_file.endswith(".txt"):
        try:
            with open(path_file) as file:
                return file.read().split("\n")
        except FileNotFoundError:
            return print(
                f"Arquivo {path_file} não encontrado", file=sys.stderr
            )
    else:
        return print("Formato inválido", file=sys.stderr)
