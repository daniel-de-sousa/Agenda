import datetime
class Agenda:
    def __init__(self):
        self.eventos = []
        pass
    
    # Ciclo 2
    def add_Evento(self, nome, inicio, fim):
        inicio_dt = datetime.datetime.strptime(inicio, "%Y-%m-%d %H:%M")
        fim_dt = datetime.datetime.strptime(fim, "%Y-%m-%d %H:%M")
        
        self.eventos.append({
            'nome': nome,
            'inicio': inicio_dt,
            'fim': fim_dt
        })

        print("Evento adicionado com sucesso.")

    # Ciclo 1
    def sair(self):
        return 0