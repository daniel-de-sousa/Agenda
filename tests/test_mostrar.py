import pytest
from src.Agenda import Agenda

@pytest.fixture
def agenda():
    return Agenda()

# Ciclo 11
def test_mostrar_sem_Evento(agenda, capsys):
    agenda.get_Eventos()
    out, _ = capsys.readouterr()
    assert len(agenda.eventos) == 0
    assert out.strip() == "Nenhum evento agendado."

# Ciclo 12
def test_mostrar_um_Evento(agenda, capsys):
    agenda.add_Evento("Final dos 100m", "2024-07-24 10:00", "2024-07-24 11:00")
    out, _ = capsys.readouterr()
    agenda.get_Eventos()
    out, _ = capsys.readouterr()
    assert len(agenda.eventos) == 1
    assert out.strip() == "Final dos 100m: 2024-07-24 10:00 a 2024-07-24 11:00"