# Plataforma de Cursos Online - API

API RESTful desenvolvida com FastAPI, Pydantic e SQLAlchemy, com persistência em SQLite.

## Tecnologias
- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite

## Como rodar
1. Criar o ambiente virtual: `python -m venv .venv`
2. Ativar o ambiente virtual: `.venv\Scripts\Activate.ps1` (Windows)
3. Instalar as dependências: `pip install "fastapi[standard]" sqlalchemy`
4. Iniciar a API: `fastapi dev main.py`
5. Abrir a documentação interativa: http://127.0.0.1:8000/docs

## Estrutura do projeto
- `database.py`: configuração da conexão com o SQLite (engine, SessionLocal, Base, get_db)
- `models.py`: modelo SQLAlchemy da tabela `cursos`
- `schemas.py`: schemas Pydantic para validação de entrada e resposta
- `routers/cursos.py`: rotas do CRUD de cursos
- `main.py`: aplicação FastAPI, criação das tabelas e inclusão do router

## Campos do Curso
| Campo | Tipo | Regra |
|---|---|---|
| id | inteiro | gerado automaticamente |
| titulo | texto | obrigatório, de 3 a 100 caracteres |
| categoria | texto | obrigatório, de 2 a 50 caracteres |
| carga_horaria | inteiro | obrigatório, maior que 0 |
| preco | decimal | obrigatório, maior ou igual a 0 |
| ativo | booleano | padrão: true |

## Rotas
| Método | Rota | Descrição | Sucesso | Erros |
|---|---|---|---|---|
| POST | /cursos/ | Cadastra um novo curso | 201 Created | 422 |
| GET | /cursos/ | Lista todos os cursos | 200 | - |
| GET | /cursos/?categoria=Office | Lista filtrando por categoria | 200 | - |
| PUT | /cursos/{id} | Atualiza todos os campos de um curso | 200 | 404, 422 |
| DELETE | /cursos/{id} | Remove um curso | 200 | 404 |

## Exemplo de corpo (POST e PUT)
```json
{
  "titulo": "Python para Iniciantes",
  "categoria": "Programação",
  "carga_horaria": 40,
  "preco": 199.9,
  "ativo": true
}
```