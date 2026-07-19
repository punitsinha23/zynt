from pathlib import Path
import json


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

def find_repository():
    current_path = Path.cwd()

    while True:
        repo_path = current_path/".zynt"


        if repo_path.is_dir():
            return current_path
        
        if current_path == current_path.parent:
            return None
    
        current_path = current_path.parent

def get_working_files():
    root_path = Path.cwd()
    exclude = ['.git', '.zynt']
    working_files = []
    for file in root_path.rglob("*"):
        if file.is_file():
            file_part = Path(file).parts
            if  not any(item in file_part for item in exclude):
                working_files.append(file.relative_to(root_path))
    
    return working_files
            


def write_file(relative_path, content):
    file_path = Path.cwd() / relative_path
    file_path.write_text(content)


def read_file(relative_path):
    file_path = Path.cwd() / relative_path
    return file_path.read_text()


def read_json(relative_path):
    content = read_file(relative_path)
    return json.loads(content)

def write_json(relative_path, content):
    write_file( relative_path , json.dumps(content, indent=4))
    

    