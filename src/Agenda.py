import datetime
class Agenda:
    def __init__(self):
        self.eventos = []
        pass
    
    # Ciclo 5
    def add_Evento(self, nome, inicio, fim):
        if any(valor == "" for valor in (nome, inicio, fim)):
            print("Existe algum campo vazio.")
            return


        try:
            inicio_dt = datetime.datetime.strptime(inicio, "%Y-%m-%d %H:%M")
            fim_dt = datetime.datetime.strptime(fim, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Formato de data e hora inválido. Use 'YYYY-MM-DD HH:MM'.")
            return
        
        self.eventos.append({
            'nome': nome,
            'inicio': inicio_dt,
            'fim': fim_dt
        })

        print("Evento adicionado com sucesso.")

    # Ciclo 1
    def sair(self):
        return 0