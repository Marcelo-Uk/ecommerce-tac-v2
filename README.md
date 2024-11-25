# Meu E-commerce Django

Este é um projeto Django para um e-commerce simples.

## Requisitos

- Python 3.8 ou superior
- Git
- Virtualenv (opcional, mas recomendado)

## Como Rodar o Projeto

1. Clone o repositório:

   ``git clone https://github.com/seu-usuario/seu-repositorio.git``

2. Acesse o diretório do projeto:

    ``cd nome-do-repositorio``

3. Crie um ambiente virtual (opcional, mas recomendado):

    ``python3 -m venv venv``
    ``source venv/bin/activate  # Linux/macOS``
    ``venv\Scripts\activate     # Windows``

4. Instale as dependências:

    ``pip install -r requirements.txt``

5. Configure o banco de dados:

    ``python manage.py migrate``

6. Crie um superusuário (opcional):

    ``python manage.py createsuperuser``

7. Inicie o servidor:

    ``python manage.py runserver``

Acesse o projeto em: http://127.0.0.1:8000.
