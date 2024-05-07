import enum

from sqlalchemy import Column, String, Boolean, Enum
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class LLMType(enum.Enum):
    ollama = 1
    huggingface = 2


class KGType(enum.Enum):
    chromadb = 1


class LLM(Base):
    __tablename__ = "LLM"
    llm_name = Column('llm_name', String(100), nullable=False, primary_key=True)
    llm_type = Column('model_type', Enum(LLMType), nullable=False)
    data = Column('data', String(200), nullable=False)
    valid = Column('valid', Boolean(), default=True)


class KGDB(Base):
    __tablename__ = "KGDB"
    kg_name = Column("kg_name", String(100), nullable=False, primary_key=True)
    kg_type = Column('kg_type', String(100), nullable=False)
    data = Column('data', String(200), nullable=False)
    valid = Column('valid', Boolean(), default=True)


