from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.src.models.produto import Produto
from app.src.schemas.produto import SchemaProduct
from app.api.routes.dependencies import get_db

times= APIRouter(tags=["times"])

@times.post("/")
async def enviarBancoDados(data: SchemaProduct, db: Session = Depends(get_db)):
    time = Produto(nome=data.produto, preco=data.preco)
    db.add(time)
    db.commit()
    return "Message: Produto salvo com sucesso!"

@times.get("/api/times")
def listarProdutos(db: Session = Depends(get_db)):
    return db.query(Produto).order_by(Produto.preco.asc()).all()

@times.get("/api/times/{id}")
def buscarProduto(id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado!")
    return produto

@times.put("/api/times/{id}")
def editarProduto(id: int, data: SchemaProduct, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado!")
    produto.nome = data.produto
    produto.preco = data.preco
    db.commit()
    return "Message: Produto atualizado com sucesso!"

@times.delete("/api/times/{id}")
def deletarItens(id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Time não encontrado!")
    db.delete(produto)
    db.commit()
    return "Message: Time deletado com sucesso!"