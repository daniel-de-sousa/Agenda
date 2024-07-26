import pytest
from datetime import datetime
from src.Agenda import Agenda

@pytest.fixture
def agenda():
    return Agenda()

# Ciclo 2
def test_adicionar_Evento_Sucesso(agenda, capsys):
    agenda.add_Evento("Final dos 100m", "2024-07-24 10:00", "2024-07-24 11:00")
    out, _ = capsys.readouterr()
    assert out.strip() == "Evento adicionado com sucesso."
    assert len(agenda.eventos) == 1
    assert agenda.eventos[0]['nome'] == "Final dos 100m"
    assert agenda.eventos[0]['inicio'] == datetime(2024, 7, 24, 10, 0)
    assert agenda.eventos[0]['fim'] == datetime(2024, 7, 24, 11, 0)

# Ciclo 3
def test_adicionar_Evento_data_invalida(agenda, capsys):
    agenda.add_Evento("Final dos 100m", "data_invalida", "2024-07-24 11:00")
    out, _ = capsys.readouterr()
    assert out.strip() == "Formato de data e hora inválido. Use 'YYYY-MM-DD HH:MM'."
    assert len(agenda.eventos) == 0

# Ciclo 4
def test_adicionar_Evento_hora_invalida(agenda, capsys):
    agenda.add_Evento("Final dos 100m", "2024-07-24 10:00", "hora_inválida")
    out, _ = capsys.readouterr()
    assert out.strip() == "Formato de data e hora inválido. Use 'YYYY-MM-DD HH:MM'."
    assert len(agenda.eventos) == 0

# Ciclo 5
def test_adicionar_Evento_invalido(agenda, capsys):
    agenda.add_Evento("", "", "")
    out, _ = capsys.readouterr()
    assert out.strip() == "Existe algum campo vazio."
    assert len(agenda.eventos) == 0

# Ciclo 6
def test_adicionar_Evento_hora_inicio_maior_que_fim(agenda, capsys):
    agenda.add_Evento("Final dos 100m", "2024-07-24 12:00", "2024-07-24 11:00")
    out, _ = capsys.readouterr()
    assert out.strip() == "A hora de início deve ser anterior à hora de término."
    assert len(agenda.eventos) == 0

# Ciclo 7
def test_adicionar_Evento_data_inicio_maior_que_fim(agenda, capsys):
    agenda.add_Evento("Final dos 100m", "2024-07-25 10:00", "2024-07-24 11:00")
    out, _ = capsys.readouterr()
    assert out.strip() == "A hora de início deve ser anterior à hora de término."
    assert len(agenda.eventos) == 0

# Ciclo 8
def test_add_Eventos_conflito(agenda, capsys):
    agenda.add_Evento("Final dos 100m", "2024-07-24 10:00", "2024-07-24 11:00")
    out, _ = capsys.readouterr()
    assert out.strip() == "Evento adicionado com sucesso."
    agenda.add_Evento("Final dos 200m", "2024-07-24 10:30", "2024-07-24 11:30")
    out, _ = capsys.readouterr()
    assert out.strip() == "Conflito de agendamento detectado."
    assert len(agenda.eventos) == 1

# Ciclo 9
def test_add_Eventos_sem_conflito(agenda, capsys):
    agenda.add_Evento("Final dos 100m", "2024-07-24 10:00", "2024-07-24 11:00")
    out, _ = capsys.readouterr()
    assert out.strip() == "Evento adicionado com sucesso."
    agenda.add_Evento("Final dos 200m", "2024-07-24 11:30", "2024-07-24 12:30")
    out, _ = capsys.readouterr()
    assert out.strip() == "Evento adicionado com sucesso."
    assert len(agenda.eventos) == 2

# Ciclo 10
def test_add_Eventos_com_mesmo_horario(agenda, capsys):
    agenda.add_Evento("Final dos 100m", "2024-07-24 10:00", "2024-07-24 11:00")
    out, _ = capsys.readouterr()
    assert out.strip() == "Evento adicionado com sucesso."
    agenda.add_Evento("Final dos 200m", "2024-07-24 10:00", "2024-07-24 11:00")
    out, _ = capsys.readouterr()
    assert out.strip() == "Conflito de agendamento detectado."
    assert len(agenda.eventos) == 1