from pathlib import Path
from utils import create_directory, create_file
from constants import ZYNT_DIR, OBJECTS_DIR, REFS_DIR, HEAD_FILE, HEADS_DIR, INDEX_FILE, CONFIG_FILE, MAIN_BRANCH


class Repository: 
    def __init__(self):
            self.path = Path.cwd()
    
    def init(self):
        repo_path = self.path/ ZYNT_DIR

        if repo_path.exists():
            print("Repository already exists.")
            return
        
        create_directory(ZYNT_DIR)
        create_directory(OBJECTS_DIR)
        create_directory(REFS_DIR)
        create_directory(HEADS_DIR)
        create_file(HEAD_FILE, "ref: refs/head/main")
        create_file(INDEX_FILE, {})
        create_file(CONFIG_FILE, {'repository_ver': 1, 'default_branch' : 'main'})
          
          
    

    
    

