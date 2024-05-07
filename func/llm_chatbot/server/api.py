from typing import List, Tuple, Iterator

from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
async def root():
    return {'message': 'Hello, World!'}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id < 1:
        raise HTTPException(status_code=404, detail="Item not found")


@app.get("/stream_chat")
async def stream_chat(model: str,
                      kg_name: str,
                      chat_history: List[Tuple[str, str]],
                      enable_rag: bool
                    ) -> Iterator[str | List[str]]:
    pass




