from flask import Flask, request
from models.task import Task

app = Flask(__name__)

# CRUD 
# Create, Read, Update, Delete = Criar, Ler, Atualizar, Deletar
# Tabela: Tarefas

tasks = []

# Rota para criar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()

if __name__ == "__main__":
    app.run(debug=True)