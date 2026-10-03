from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db

router = APIRouter(prefix="/cursos", tags=["Cursos"])


# CREATE
@router.post("/", response_model=schemas.CursoResponse,
             status_code=status.HTTP_201_CREATED)
def criar_curso(curso: schemas.CursoCreate, db: Session = Depends(get_db)):
    novo = models.Curso(**curso.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


# READ ALL (com filtro)
@router.get("/", response_model=List[schemas.CursoResponse])
def listar_cursos(categoria: Optional[str] = None,
                  db: Session = Depends(get_db)):
    consulta = db.query(models.Curso)
    if categoria:
        consulta = consulta.filter(models.Curso.categoria == categoria)
    return consulta.all()


# UPDATE
@router.put("/{curso_id}", response_model=schemas.CursoResponse)
def atualizar_curso(curso_id: int, dados: schemas.CursoCreate,
                    db: Session = Depends(get_db)):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    for campo, valor in dados.model_dump().items():
        setattr(curso, campo, valor)
    db.commit()
    db.refresh(curso)
    return curso


# DELETE
@router.delete("/{curso_id}")
def deletar_curso(curso_id: int, db: Session = Depends(get_db)):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    db.delete(curso)
    db.commit()
    return {"mensagem": "Curso removido com sucesso"}