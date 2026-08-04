from pathlib import Path
import json
import hashlib
from .constants import INDEX_FILE, HEADS_DIR, HEAD_FILE

exclude_dirs = {
    ".git",
    ".zynt",
    "__pycache__",
    "zynt.egg-info",
    ".venv",
    "venv",
    ".idea",
    ".vscode",
}

exclude_extensions = {
    ".pyc",
    ".pyo",
}

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
    working_files = []
    for file in root_path.rglob("*"):
        if file.is_file():

            if any(part in exclude_dirs for part in file.parts):
                continue

            if file.suffix in exclude_extensions:
                continue

            working_files.append(file.relative_to(root_path))
    
    return working_files
            


def write_file(relative_path, content):
    file_path = Path.cwd() / relative_path
    file_path.write_text(content)


def read_file(relative_path):
    file_path = Path.cwd() / relative_path
    return file_path.read_text(encoding="utf-8")


def read_json(relative_path):
    content = read_file(relative_path)
    return json.loads(content)

def write_json(relative_path, content):
    write_file( relative_path , json.dumps(content, indent=4))

def hash_file(content):
    sha1_hash = hashlib.sha1(content.encode('utf-8'))
    return sha1_hash.hexdigest()

def get_untracked_files():
    untracked_files = []
    repository = find_repository()
    index = read_json(INDEX_FILE)
    if not repository:
        print("No repository exists.")
        return
    
    latest_commit = get_latest_commit()
    if latest_commit:
        latest_commit_files = latest_commit.get("files")
    else:
        latest_commit_files = {}

    working_files = get_working_files()

    for files in working_files:
        file_path = str(files)
        if file_path not in latest_commit_files and file_path not in index:
            untracked_files.append(file_path)

    return untracked_files

def get_modified_files():
    modified_files = []
    index = read_json(INDEX_FILE)

        

    for file_path, stored_hash in index.items():
        content = read_file(file_path)
        new_hash = hash_file(content)
        
        if new_hash != stored_hash:
            modified_files.append(file_path)
            
    return modified_files

def get_latest_commit():
    commit_hash = read_file(".zynt/refs/heads/main")
    if not commit_hash:
        return
    
    commit_file = read_json(f".zynt/objects/{commit_hash}")
    return commit_file

def is_branch(name):
    branch_path = Path.cwd() / HEADS_DIR / name
    return branch_path.exists()

def get_current_branch():
    head = read_file(f"{HEAD_FILE}")
    branch = head.split("/")[-1]
    return branch
 


    

    