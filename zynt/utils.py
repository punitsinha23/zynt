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

def find_repository():
    current_path = Path.cwd()

    while True:
        repo_path = current_path/".zynt"


        if repo_path.is_dir():
            return current_path
        
        if current_path == current_path.parent:
            return None
    
        current_path = current_path.parent

    
        

    


    

find_repository()

def write_file():
    pass

def read_file():
    pass

def read_json():
    pass

def write_json():
    pass

    