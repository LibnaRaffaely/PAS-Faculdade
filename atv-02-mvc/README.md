# Alunos

Líbna Raffaely de Jesus Costa - 202302617
Lucas Moreira Iglesias - 202400421

# Aplicação Cadastro de Alunos - MVC

Este é um projeto acadêmico de uma aplicação simples de cadastro de alunos utilizando a arquitetura **MVC (Model-View-Controller)**, desenvolvida em Python e Flask.

## Estrutura do Projeto

O código está isolado em pastas baseadas nos princípios do MVC:

- **`models/`**: Contém as classes que gerenciam os dados (`student.py`). Foi adicionada persistência de dados utilizando o banco de dados **SQLite** (`students.db`).
- **`views/`**: Contém os arquivos visuais (HTML) consumidos pelo usuário.
- **`controllers/`**: Contém as funções que intermediam requisições de usuário, leitura do Model e envio de dados para a View (`student_controller.py`).
- **`app.py`**: É o Router de entrada, responsável apenas por inicializar a aplicação Flask e rotear as URLs.

## Como Executar

É recomendado utilizar um ambiente virtual (`venv`) para isolar as dependências do projeto. Siga os passos abaixo no terminal:

### 1. Criar o Ambiente Virtual
Na raiz do projeto, rode:
```bash
python -m venv venv
```

### 2. Ativar o Ambiente Virtual
No Windows (PowerShell ou CMD), ative o ambiente recém-criado:
```bash
venv\Scripts\activate
```
*(Se estiver em Linux/Mac, o comando seria `source venv/bin/activate`)*

### 3. Instalar Dependências
Instale o framework Flask e outras dependências usando o arquivo de requisitos:
```bash
pip install -r requirements.txt
```

### 4. Rodar o Servidor
Execute o arquivo principal do projeto:
```bash
python app.py
```

### 5. Acessar a Aplicação
Abra o seu navegador e acesse a URL local gerada pelo Flask, que normalmente será:
[http://127.0.0.1:5000](http://127.0.0.1:5000)
