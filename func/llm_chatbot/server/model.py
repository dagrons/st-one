from sqlalchemy import Column, String, Boolean

from func.llm_chatbot.server.database import Base


class KGDB(Base):
    __tablename__ = "KGDB"
    kg_name = Column("kg_name", String(100), nullable=False, primary_key=True)
    data = Column('data', String(200), nullable=False)
    valid = Column('valid', Boolean(), default=True)
