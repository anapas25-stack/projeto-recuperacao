from pydantic import BaseModel, Field, ConfigDict


class CursoBase(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=100)
    categoria: str = Field(..., min_length=2, max_length=50)
    carga_horaria: int = Field(..., gt=0)
    preco: float = Field(..., ge=0)
    ativo: bool = True


class CursoCreate(CursoBase):
    pass


class CursoResponse(CursoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)