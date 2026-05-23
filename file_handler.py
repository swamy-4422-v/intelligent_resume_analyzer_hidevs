import json
import os
from datetime import datetime

def save_to_json(data, filepath: str) -> str:
    dirpath = os.path.dirname(os.path.abspath(filepath))
    os.makedirs(dirpath, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=4, ensure_ascii=False)
    return os.path.abspath(filepath)

def load_from_json(filepath: str):
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    with open(filepath, "r", encoding="utf-8") as fh:
        return json.load(fh)

def generate_timestamped_path(directory: str, prefix: str = "result", ext: str = "json") -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prefix}_{timestamp}.{ext}"
    return os.path.join(directory, filename)
