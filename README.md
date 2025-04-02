# API de Lista de Tarefas
Este é um projeto de API RESTful retirado do [Roadmap.sh](https://roadmap.sh/projects/todo-list-api) para gerenciar listas de tarefas, construído usando o Flask e SQLAlchemy. A API permite que os usuários registrem-se, façam login, criem, atualizem, excluam e visualizem tarefas. A autenticação de usuários é feita com JWT (JSON Web Tokens).

## Tecnologias Utilizadas
  
* Python 3
* Flask
* Flask-RESTful
* Flask-SQLAlchemy
* Flask-JWT-Extended
* bcrypt para hashing de senhas
* SQLite (pode ser substituído por outros bancos de dados como PostgreSQL, MySQL, etc.)    


## Funcionalidades
* Registro de usuário (POST /register)
* Login de usuário (POST /login)
* CRUD para tarefas (GET /tasks, POST /tasks, PUT /tasks/<id>, DELETE /tasks/<id>)
* Paginação e filtragem de tarefas
* Autenticação com JWT (JSON Web Token)  

### Requisitos
Certifique-se de ter o Python 3.x instalado na sua máquina. Você pode verificar isso executando:

    bash

    python --version
    Instalando Dependências  

Clone o repositório:

    bash
    git clone https://github.com/bruunovsanttos/APIToDoList
    

Crie um ambiente virtual (opcional, mas recomendado):

    bash

    python -m venv venv
Para ativar o ambiente virtual:

No Windows:

    bash

    venv\Scripts\activate
No macOS/Linux:

    bash
    
    source venv/bin/activate
    Instale as dependências:

Instale todas as dependências necessárias com o comando:

    bash

    pip install -r requirements.txt
Caso o arquivo requirements.txt ainda não esteja presente, você pode gerar um com:

    bash

    pip freeze > requirements.txt