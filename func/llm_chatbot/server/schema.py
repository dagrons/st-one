from pydantic import BaseModel


class LLMBase(BaseModel):
    llm_name: str
    llm_type: str
    data: str
    valid: bool


class LLM(LLMBase):
    class Config:
        orm_mode = True


class LLMCreate(LLMBase):
    pass


class KGDBBase(BaseModel):
    kg_name: str


class KGDB(KGDBBase):
    kg_type: str
    valid: bool

    class Config:
        orm_mode = True


class KGDBCreate(KGDBBase):
    kg_type: str
    valid: bool

