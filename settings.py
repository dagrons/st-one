import platform
from pathlib import Path
from typing import List

if platform.system() == "Darwin":
    DATA_BASE_PATH = Path.home().resolve() / 'data' / 'one'
    LOCAL_LLM_MODEL_BASE_PATH = Path.home()
    LOCAL_EMB_MODEL_BASE_PATH = Path.home()
elif platform.system() == 'Windows':
    DATA_BASE_PATH = Path.home() / 'data' / 'one'
    LOCAL_LLM_MODEL_BASE_PATH = Path("D:")
    LOCAL_EMB_MODEL_BASE_PATH = Path("D:")
if not DATA_BASE_PATH.exists():
    DATA_BASE_PATH.mkdir(parents=True)

PERSISTENT_DIRECTORY = DATA_BASE_PATH / 'vectordb'
KG_DATA_PATH = DATA_BASE_PATH / 'kg_data'
KG_PROCESSED_DATA_PATH = DATA_BASE_PATH / 'kg_processed_data'

SUPPORTED_MODELS: List[str] = ["qwen:0.5b"]
SUPPORTED_EMBEDDINGS: List[str] = ["m3e-base"]
LOCAL_EMBEDDINGS = {
    'm3e-base': LOCAL_EMB_MODEL_BASE_PATH / 'm3e-base'
}
LOCAL_MODELS = {
}
