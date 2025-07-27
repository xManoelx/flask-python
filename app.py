from flask import Flask, request, jsonify
from models import task
from models.task import Task

app = Flask(__name__)

# CRUD 
# Create, Read, Update, Delete = Criar, Ler, Atualizar, Deletar
# Tabela: Tarefas

tasks = []
taskIdControl = 1

# Rota para criar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():

    global taskIdControl, tasks

    # Recebe os dados da tarefa do corpo da requisição
    data = request.get_json()

    # Valida os dados recebidos
    new_task = Task(id=taskIdControl, title=data.get('title'), description=data.get('description', ''))
    taskIdControl += 1
    tasks.append(new_task)
    print(tasks)

    # Retorna uma resposta JSON com a mensagem de sucesso
    return jsonify({
        'message': 'Tarefa criada com sucesso'
    })

# Rota para ler todas as tarefas
@app.route('/tasks', methods=['GET']) 
def get_tasks():

    # Converte as tarefas para dicionários
    task_list = [task.to_dict() for task in tasks] 
    output = {
                'tasks': task_list,
                'total_tasks': len(task_list),
            }
    return jsonify(output)

# Rota para ler uma tarefa específica pelo ID
@app.route('/tasks/<int:id>', methods=['GET']) 
def get_task(id):
    task = None
    for t in tasks: # t é cada atividade em tasks
        if t.id == id:
            return jsonify(t.to_dict())
            
        return jsonify({'message': 'Tarefa não encontrada'}), 404    

# Rota para atualizar uma tarefa pelo ID
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):

    task = None
    for t in tasks: # t é cada atividade em tasks

        # Verifica se o ID da tarefa corresponde ao ID fornecido
        if t.id == id:
            task = t

    # Se a tarefa não for encontrada
    if task == None: 
        return jsonify({'message': 'Tarefa não encontrada'}), 404

    # Recebe os dados da tarefa do corpo da requisição
    data = request.get_json()

    # Atualiza os dados da tarefa
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']

    print(task)

    return jsonify({'message': 'Tarefa atualizada com sucesso'})

# Rota para deletar uma tarefa pelo ID
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):

    task = None
    for t in tasks: # t é cada atividade em tasks
        if t.id == id:
            task = t

    # Se a tarefa não for encontrada
    if task == None:
        return jsonify({'message': 'Tarefa não encontrada'}), 404

    # Remove a tarefa da lista
    tasks.remove(task)

    return jsonify({'message': 'Tarefa deletada com sucesso'})

# Inicia o servidor Flask se este arquivo for executado diretamente
if __name__ == "__main__": 
    app.run(debug=True)