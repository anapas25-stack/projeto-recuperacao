from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from database import engine, Base
from routers import cursos

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Plataforma de Cursos Online")


NOMES_CAMPOS = {
    "titulo": "título",
    "categoria": "categoria",
    "carga_horaria": "carga horária",
    "preco": "preço",
    "ativo": "ativo",
    "email_instrutor": "e-mail",
    "telefone": "telefone",
}


def traduzir_erro(erro: dict, campo: str) -> str:
    tipo = erro["type"]
    ctx = erro.get("ctx", {})
    nome = NOMES_CAMPOS.get(campo, campo)

    if tipo == "missing":
        return f"O campo {nome} é obrigatório."
    if campo == "telefone" and tipo in ("string_too_short", "string_too_long", "string_pattern_mismatch"):
        return "O telefone deve conter 11 dígitos com o DDD, apenas números."
    if campo == "email_instrutor":
        return "Insira um e-mail válido no formato nome@dominio.com."
    if tipo == "string_too_short":
        return f"O campo {nome} deve ter no mínimo {ctx.get('min_length')} caracteres."
    if tipo == "string_too_long":
        return f"O campo {nome} deve ter no máximo {ctx.get('max_length')} caracteres."
    if tipo in ("greater_than", "int_parsing", "float_parsing"):
        return f"O campo {nome} deve ser um número maior que zero."
    if tipo == "value_error":
        return str(erro["msg"]).replace("Value error, ", "")
    return erro["msg"]


@app.exception_handler(RequestValidationError)
async def tratar_erro_validacao(request: Request, exc: RequestValidationError):
    erros = []
    for erro in exc.errors():
        campo = str(erro["loc"][-1])
        erros.append({"campo": campo, "mensagem": traduzir_erro(erro, campo)})
    return JSONResponse(
        status_code=422,
        content={"detail": "Dados inválidos. Corrija os campos abaixo.", "erros": erros},
    )


app.include_router(cursos.router)