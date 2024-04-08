from pathlib import Path

PERSISTENT_DIRECTORY = Path('D:') / 'vectordb'
EMBEDDING_PATH = Path("D:") / 'paraphrase-MiniLM-L6-v2'
KG_DATA_PATH = Path('D:') / 'kg_data'
KG_PROCESSED_DATA_PATH = Path("D:") / 'kg_processed_data'
MODEL_PATH = {
    'Qwen1.5-1.8b-chat': Path("D:").resolve() / 'Qwen1.5-1.8B-Chat',
    'chatglm3-6b': Path("D:").resolve() / 'chatglm3-6b',
    'minicpm-2b-dpo-fp16': Path("D:").resolve() / 'MiniCPM-2B-dpo-fp16',
    'Qwen1.5-7b-chat': Path("D:").resolve() / 'Qwen1.5-7B-Chat',
}
LOG_PATH = Path("D:") / 'demo_log.csv'
TABLE_PATH = Path("D:") / 'demo_table.csv'
TODOCSV_PATH = Path("D:") / 'demo_todolist.csv'



