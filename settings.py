from pathlib import Path

PERSISTENT_DIRECTORY = Path('D:') / 'vectordb'
EMBEDDING_PATH = Path("D:") / 'paraphrase-MiniLM-L6-v2'
KG_DATA_PATH = Path('D:') / 'kg_data'
MODEL_PATH = {
    'chatglm3-6b': Path("D:").resolve() / 'chatglm3-6b',
    'minicpm-2b-dpo-fp16': Path("D:").resolve() / 'MiniCPM-2B-dpo-fp16',
    'Qwen1.5-7b-chat': Path("D:").resolve() / 'Qwen1.5-7B-Chat',
}

