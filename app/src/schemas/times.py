from pydantic import BaseModel

class SchemaProduct(BaseModel):
    time: str
    titulos: float