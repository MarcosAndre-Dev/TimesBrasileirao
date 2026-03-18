from sqlalchemy import Column, Integer, String, int
from app.src.infra.database import Base

class times(Base):
    __tablename__ = "times"
    id    = Column(Integer, primary_key=True, index=True)
    nomeTime  = Column(String)
    titulos = Column(int)