from pydantic import BaseModel


class KGDBBase(BaseModel):
    kg_name: str


class KGDB(KGDBBase):
    valid: bool

    class Config:
        orm_mode = True


class KGDBCreate(KGDBBase):
    valid: bool
