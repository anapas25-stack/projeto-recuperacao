from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class CursoBase(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=100, description="Título do curso")
    categoria: str = Field(..., min_length=3, max_length=50, description="Categoria do curso")
    carga_horaria: int = Field(..., gt=0, description="Carga horária em horas (maior que zero)")
    preco: float = Field(..., gt=0, description="Preço em reais (maior que zero)")
    ativo: bool = True
    email_instrutor: EmailStr = Field(..., description="E-mail do instrutor")
    telefone: str = Field(..., min_length=11, max_length=11, pattern=r"^\d{11}$",
                          description="DDD + número, somente dígitos (11 dígitos)")

    @field_validator("titulo", "categoria", mode="before")
    @classmethod
    def nao_pode_ser_vazio(cls, valor, info):
        if isinstance(valor, str):
            if not valor.strip():
                raise ValueError(f"O campo {info.field_name} é obrigatório e não pode ficar em branco.")
            return valor.strip()
        return valor


class CursoCreate(CursoBase):
    pass


class CursoResponse(CursoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)