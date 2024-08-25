from dotenv import load_dotenv
import os

def env_load() -> dict:
    load_dotenv()
    input_path = os.getenv('INPUT_PATH')
    if not input_path:
        raise Exception("ENV: Input path not found.")
    exclude_dirs = os.getenv('EXCLUDE_DIRS')
    if not exclude_dirs:
        raise Exception("ENV: Exclude dirs not found.")
    
    return {
        "INPUT_PATH": input_path,
        "EXCLUDE_DIRS": exclude_dirs.split(",")
    }
    
env = env_load()