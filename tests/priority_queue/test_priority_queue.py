from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    """Aqui irá sua implementação"""
    priority_queue = PriorityQueue()

    mafumafu = {
        "nome_do_arquivo": "mafumafu.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": [
            "yume no mata yume",
            "inochi ni kirawareteiru",
            "onna no ko ni naritai",
            "hitomodoki",
        ],
    }

    kuroneko = {
        "nome_do_arquivo": "96neko.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": [
            "nisemononingen40gou",
            "vita",
        ],
    }

    ado = {
        "nome_do_arquivo": "ado.txt",
        "qtd_linhas": 6,
        "linhas_do_arquivo": [
            "fleeting lullaby",
            "usseewa",
            "odo",
            "lucky bruto",
            "ashura-chan",
            "atashi wa mondai sa ku",
        ],
    }

    priority_queue.enqueue(mafumafu)
    priority_queue.enqueue(ado)
    priority_queue.enqueue(kuroneko)

    assert len(priority_queue) == 3

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(3)

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(-1)

    assert priority_queue.is_priority(ado) is False
    assert priority_queue.is_priority(kuroneko) is True

    assert priority_queue.search(2) == ado
    assert priority_queue.dequeue() == mafumafu
    assert priority_queue.search(0) == kuroneko
