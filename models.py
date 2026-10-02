from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base


class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    carga_horaria = Column(Integer, nullable=False)
    preco = Column(Float, nullable=False)
    ativo = Column(Boolean, default=True)