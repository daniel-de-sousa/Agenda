from src.Agenda import Agenda

# Ciclo 1
def test_sair():
    agenda = Agenda()
    assert agenda.sair() == 0