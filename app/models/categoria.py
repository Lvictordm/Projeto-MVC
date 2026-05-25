# Tabela de categorias

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(String, unique=True, nullable=False)
    ativo = Column(Boolean, default=True)

    # Relacionamento
    # lazy = carrega os produtos apenas quando acessados
    produtos = relationship("Produto", back_populates="categoria", lazy="select")