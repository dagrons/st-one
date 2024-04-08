from pathlib import Path

TODOCSV_PATH = Path.home() / 'todolist.csv'
PERSISTENT_DIRECTORY = Path('').parent / 'db'
EMBEDDING_PATH = Path("D:") / 'paraphrase-MiniLM-L6-v2'
DATA_PATH = Path.home() / 'data'
LOG_PATH = r"C:\Users\dagrons\Desktop\DigitialTwinProject\XXXX目录组成.xlsx"
TABLE_PATH = Path.home() / 'Desktop' / 'test.csv'
MODEL_PATH = {
    'chatglm3-6b': Path("D:").resolve() / 'chatglm3-6b',
    'minicpm-2b-dpo-fp16': Path("D:").resolve() / 'MiniCPM-2B-dpo-fp16',
    'Qwen1.5-7b-chat': Path("D:").resolve() / 'Qwen1.5-7B-Chat',
}

