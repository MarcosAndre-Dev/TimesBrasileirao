from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.src.models.times import Times          
from app.src.schemas.times import SchemaProduct
from app.src.infra.dependencies import get_db

router = APIRouter(tags=["times"])             

@router.post("/api/times")
async def enviarBancoDados(data: SchemaProduct, db: Session = Depends(get_db)):
    time = Times(nome=data.time, titulos=data.titulos)  
    db.add(time)
    db.commit()
    return {"message": "time salvo com sucesso!"}

@router.get("/api/times")
def listarTimes(db: Session = Depends(get_db)):
    return db.query(Times).order_by(Times.titulos.desc()).all()  

@router.get("/api/times/{id}")
def buscarTimes(id: int, db: Session = Depends(get_db)):
    time = db.query(Times).filter(Times.id == id).first()  
    if not time:
        raise HTTPException(status_code=404, detail="time não encontrado!")
    return time

@router.put("/api/times/{id}")
def editarTime(id: int, data: SchemaProduct, db: Session = Depends(get_db)):
    time = db.query(Times).filter(Times.id == id).first()  
    if not time:
        raise HTTPException(status_code=404, detail="time não encontrado!")
    time.nome = data.time       
    time.titulos = data.titulos  
    db.commit()
    return {"message": "time atualizado com sucesso!"}

@router.delete("/api/times/{id}")
def deletarTimes(id: int, db: Session = Depends(get_db)):
    time = db.query(Times).filter(Times.id == id).first()  
    if not time:
        raise HTTPException(status_code=404, detail="Time não encontrado!")
    db.delete(time)
    db.commit()
    return {"message": "Time deletado com sucesso!"}