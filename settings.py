from pathlib import Path
from typing import List

DATA_BASE_PATH = Path("D:").resolve() / 'data' / 'one'
if not DATA_BASE_PATH.exists():
    DATA_BASE_PATH.mkdir(parents=True)
MODEL_BASE_PATH = Path("D:").resolve()

PERSISTENT_DIRECTORY = DATA_BASE_PATH / 'vectordb'
KG_DATA_PATH = DATA_BASE_PATH / 'kg_data'
KG_PROCESSED_DATA_PATH = DATA_BASE_PATH / 'kg_processed_data'

SUPPORTED_MODELS:List[str] = ["qwen:0.5b"]
SUPPORTED_EMBEDDINGS:List[str] = ["m3e-base"]
LOCAL_EMBEDDINGS = {
    'm3e-base': Path('D:') / 'm3e-base'
}
LOCAL_MODELS = {
}