import logging
from typing import Annotated

import uvicorn
from fastapi import File, HTTPException, Depends, Form, Body
from fastapi.exceptions import ValidationException
from fastapi_offline import FastAPIOffline
from sqlalchemy.orm import Session

from func.llm_chatbot.server import crud, schema
from func.llm_chatbot.server.crud import InvalidFileFormatException
from func.llm_chatbot.server.database import SessionLocal

app = FastAPIOffline()

logger = logging.getLogger(__name__)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Checker:
    def __init__(self, model):
        self.model = model

    def __call__(self, item: str = Form()):
        try:
            return self.model.model_validate_json(item)
        except ValidationException:
            raise HTTPException(
                status_code=412,
                detail="failed to get KGDBCreate"
            )


@app.post("/kg_db/")
async def create_kg_db(db: Annotated[Session, Depends(get_db)],
                       kg_db_tarfile: Annotated[bytes, File()],
                       item: Annotated[schema.KGDBCreate, Depends(Checker(schema.KGDBCreate))],
                       ):
    try:
        crud.create_kg_db(db, kg_db_tarfile, item)
    except InvalidFileFormatException as e:
        logger.error(f"failed to create kg_db, e={e}")
        raise HTTPException(404, detail=e.msg)
    except Exception as e:
        logger.error(f"failed to create kg_db, e={e}")
        raise HTTPException(404, detail="unknown error")


@app.get("/kg_db/", response_model=list[schema.KGDB])
async def read_kg_dbs(db: Annotated[Session, Depends(get_db)]):
    try:
        return crud.read_kg_dbs(db)
    except Exception as e:
        logger.error(f"failed to read kg_dbs, e={e}")
        raise HTTPException(404, detail=e.msg)


@app.put("/kg_db/")
async def update_kg_dbs(db: Annotated[Session, Depends(get_db)],
                        mappings: Annotated[list[dict[str, str | bool]], Body()]):
    try:
        crud.update_kg_dbs(db, mappings)
    except Exception as e:
        logger.error(f"failed to update kg_dbs, e={e}")
        raise HTTPException(404, detail=e.msg)


@app.delete('/kg_db/{kg_name}')
async def delete_kg_db(db: Annotated[Session, Depends(get_db)], kg_name: str):
    try:
        crud.delete_kg_db(db, kg_name)
    except Exception as e:
        logger.error(f"failed to delete kg_db, e={e}")
        raise HTTPException(404, detail=e.msg)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
