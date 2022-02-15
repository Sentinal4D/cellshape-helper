from pathlib import Path


def create_dir_if_not_exist(path):
    p = Path(path)
    if not p.exists():
        p.mkdir(parents=True, exist_ok=True)
