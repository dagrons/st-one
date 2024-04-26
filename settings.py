from pathlib import Path

DATA_BASE_PATH = Path.home().resolve() / 'data' / 'one'
if not DATA_BASE_PATH.exists():
    DATA_BASE_PATH.mkdir(parents=True)
MODEL_BASE_PATH = Path.home().resolve()

PERSISTENT_DIRECTORY = DATA_BASE_PATH / 'vectordb'
EMBEDDING_PATH = MODEL_BASE_PATH / 'm3e-base'
KG_DATA_PATH = DATA_BASE_PATH / 'kg_data'
KG_PROCESSED_DATA_PATH = DATA_BASE_PATH / 'kg_processed_data'
MODEL_PATH = {
    'Qwen1.5-0.5b-chat': MODEL_BASE_PATH.resolve() / 'Qwen1.5-0.5B-Chat',
    'Qwen1.5-1.8b-chat': MODEL_BASE_PATH.resolve() / 'Qwen1.5-1.8B-Chat',
    'Qwen1.5-7b-chat': MODEL_BASE_PATH.resolve() / 'Qwen1.5-7B-Chat',
    'Qwen1.5-14b-chat': MODEL_BASE_PATH.resolve() / 'Qwen1.5-14B-Chat',
    'minicpm-2b-dpo-fp16': MODEL_BASE_PATH.resolve() / 'MiniCPM-2B-dpo-fp16',
    'chatglm3-6b': MODEL_BASE_PATH.resolve() / 'chatglm3-6b',
}


