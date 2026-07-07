from pathlib import Path

def create_directory(relative_path):
    path = Path.cwd()
    directory = path / relative_path
    directory.mkdir(parents=True, exist_ok=True)

def create_file(path, content=""):
    path.touch()
    if content:
        path.write_text(content)

def write_file():
    pass

def read_file():
    pass

def read_json():
    pass

def write_json():
    pass

    