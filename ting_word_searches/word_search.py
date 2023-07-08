import re


def exists_word(word, instance):
    """Aqui irá sua implementação"""
    result = []

    for file in instance._data:
        word_occurence = []

        for line_index, line in enumerate(file["linhas_do_arquivo"], start=1):
            if re.search(word, line, re.IGNORECASE):
                word_occurence.append({"linha": line_index})

        if word_occurence:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": word_occurence,
                }
            )

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
