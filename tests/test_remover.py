import pytest
from src.Agenda import Agenda

@pytest.fixture
def agenda():
    return Agenda()

# Ciclo 14
def test_remover_Evento_existente(agenda, capsys):
    agenda.add_Evento("Final dos 100m", "2024-07-24 10:00", "2024-07-24 11:00")
    out, _ = capsys.readouterr()
    assert len(agenda.eventos) == 1
    agenda.remove_Evento("Final dos 100m")
    out, _ = capsys.readouterr()
    assert len(agenda.eventos) == 0
    assert out.strip() == "Evento removido com sucesso."

# Ciclo 15
def test_remover_Evento_sem_ter_Eventos(agenda, capsys):
    agenda.remove_Evento("Final dos 100m")
    out, _ = capsys.readouterr()
    assert len(agenda.eventos) == 0
    assert out.strip() == "Não existem eventos cadastrados"

# Ciclo 16
def test_remover_Evento_que_nao_existe(agenda, capsys):
    agenda.add_Evento("Final dos 100m", "2024-07-24 10:00", "2024-07-24 11:00")
    out, _ = capsys.readouterr()
    qtd = len(agenda.eventos)
    agenda.remove_Evento("Evento")
    out, _ = capsys.readouterr()
    assert len(agenda.eventos) == qtd
    assert out.strip() == "Não existem evento com esse nome"