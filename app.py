from flask import Flask

app = Flask(__name__)

# CRUD 
# Create, Read, Update, Delete = Criar, Ler, Atualizar, Deletar
# Tabela: Tarefas

if __name__ == "__main__":
    app.run(debug=True)