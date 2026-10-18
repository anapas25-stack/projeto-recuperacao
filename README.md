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
| categoria | texto | obrigatório, de 3 a 50 caracteres |
| carga_horaria | inteiro | obrigatório, maior que 0 |
| preco | decimal | obrigatório, maior que 0 |
| ativo | booleano | padrão: true |
| email_instrutor | texto | obrigatório, e-mail válido |
| telefone | texto | obrigatório, 11 dígitos (DDD + número) |

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
  "titulo": "Python do Zero",
  "categoria": "Programação",
  "carga_horaria": 40,
  "preco": 199.90,
  "ativo": true,
  "email_instrutor": "maria@email.com",
  "telefone": "11999998888"
}
```
## Regras de validação

Os dados de entrada são validados pelos schemas Pydantic (`schemas.py`).

| Campo | Regra |
|---|---|
| titulo | 3 a 100 caracteres, não pode ser vazio |
| categoria | 3 a 50 caracteres, não pode ser vazio |
| carga_horaria | número maior que zero |
| preco | número maior que zero |
| email_instrutor | e-mail válido (nome@dominio.com) |
| telefone | exatamente 11 dígitos (DDD + número), somente números |

## Mensagens de erro

Quando uma validação falha, a API responde **422** com mensagens amigáveis em JSON:

```json
{
  "detail": "Dados inválidos. Corrija os campos abaixo.",
  "erros": [
    {
      "campo": "telefone",
      "mensagem": "O telefone deve conter 11 dígitos com o DDD, apenas números."
    }
  ]
}
```