from pathlib import Path


def create_directory(relative_path):
    path = Path.cwd()
    directory = path / relative_path
    directory.mkdir(parents=True, exist_ok=True)

def create_file(relative_path, content=""):
    path = Path.cwd()
    file_path = path / relative_path
    file_path.touch(exist_ok=True)
    if content:
        file_path.write_text(content)

def write_file():
    pass

def read_file():
    pass

def read_json():
    pass

def write_json():
    pass

    