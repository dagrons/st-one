import logging.config
from pathlib import Path
from typing import List, Dict, Tuple, Union

DATA_BASE_PATH = Path("D:")

KG_DB_BASE_PATH = DATA_BASE_PATH / 'kg_db'

SUPPORTED_MODELS: Dict[str, List[Union[str, Tuple[str, str]]]]= {
    'ollama': [
        'wizardlm2',
        'llama3:7b'
    ],
    'huggingface': [
        ('chatglm3-6b', ''),
        ('MiniCPM-2B-dpo-fp16', ''),
        ('Qwen1.5-1.8B-Chat', ''),
        ('Qwen1.5-7B-Chat', ''),
        ('Qwen1.5-14B-Chat', '')
    ]
}

SUPPORTED_MODEL_NAMES = SUPPORTED_MODELS['ollama'] + [a for (a, b) in SUPPORTED_MODELS['huggingface']]

logging.config.fileConfig(str(Path('')/'conf'/'logging.conf'))
