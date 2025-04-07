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

### ⚙️Requisitos
Certifique-se de ter o Python 3.x instalado na sua máquina. Você pode verificar isso executando:

    bash

    python --version
    

## 🧰 Instalação

1. Clone o repositório:

    bash
    git clone https://github.com/bruunovsanttos/APIToDoList
    

2. Crie um ambiente virtual (opcional, mas recomendado):

    bash

    python -m venv venv


* Windows:  

        bash
        venv\Scripts\activate  

* macOS/Linux:    

        bash
        source venv/bin/activate
4. Instale as dependências:

Instale todas as dependências necessárias com o comando:

    bash
    pip install -r requirements.txt

* Caso o arquivo requirements.txt ainda não esteja presente, você pode gerar um com:

        bash
        pip freeze > requirements.txt


## 🔄 Como Usar
Execute a aplicação:

    bash
    python app.py

A API estará disponível em:

    http://localhost:5000  


Use ferramentas como Postman ou Insomnia para testar as rotas.

## 🔐 Segurança
Senhas com hash usando [bcrypt](https://pypi.org/project/bcrypt/)

Autenticação e autorização com [JWT](https://pyjwt.readthedocs.io/en/stable/)

Blacklist de tokens para logout seguro  

## 📁 Organização do Projeto
    bash

    APIToDoList/
    ├── app.py                # Arquivo principal
    ├── models/               # Modelos do banco de dados
    ├── resources/            # Endpoints da API
    ├── blacklist.py          # Blacklist de JWTs
    ├── extensions.py         # Configurações
    └── requirements.txt      # Dependências


## 👨‍💻 Contribuindo
Contribuições são bem-vindas!

Você pode:

* Abrir uma issue

* Criar um fork

* Enviar um pull request  


## 📄 Licença
Este projeto está sob a licença MIT.
Veja o arquivo LICENSE para mais detalhes.

## 👤 Autor
Feito com 💻 e ☕ por Bruno V. Santos

  
