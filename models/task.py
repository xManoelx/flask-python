# id = id da tarefa
# title = título da tarefa  
# description = descrição da tarefa
# completed = status da tarefa (padrão é False)

class Task:
    
    # Inicializa a tarefa com id, título, descrição e status de conclusão
    def __init__(self, id, title, description, completed=False): 
        self.id = id 
        self.title = title 
        self.description = description 
        self.completed = completed 

    # Método para converter a tarefa em um dicionário
    def to_dict(self): 
            return {
                'id': self.id, 
                'title': self.title,
                'description': self.description,
                'completed': self.completed
        }