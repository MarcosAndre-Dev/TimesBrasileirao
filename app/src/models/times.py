from sqlalchemy import Column, Integer, String
from app.src.infra.database import Base

class Times(Base):
    __tablename__ = "Times"
    id    = Column(Integer, primary_key=True, index=True)
    nome  = Column(String)
    titulos = Column(Integer)