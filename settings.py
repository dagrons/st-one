from pathlib import Path
from typing import List, Dict

from sqlalchemy import create_engine

KG_DB_BASE_PATH = Path("D:") / 'kg_db'

HUGGINGFACE_MODEL_BASE_PATH = Path("D:") / 'huggingface_model'

SUPPORTED_MODELS: Dict[str, List[str]]= {
    'ollama': [
        'wizardlm2',
        'llama3:7b'
    ],
    'huggingface': [
        'chatglm3-6b',
        'MiniCPM-2B-dpo-fp16',
        'Qwen1.5-1.8B-Chat',
        'Qwen1.5-7B-Chat',
        'Qwen1.5-14B-Chat'
    ]
}


