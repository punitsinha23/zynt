from pathlib import Path
from .utils import create_directory, create_file
from .constants import ZYNT_DIR, OBJECTS_DIR, REFS_DIR, HEAD_FILE, HEADS_DIR, INDEX_FILE, CONFIG_FILE, MAIN_BRANCH, REPOSITORY_VERSION
import json


class Repository: 
    def __init__(self):
            self.path = Path.cwd()
    
    def init(self):
        repo_path = self.path/ ZYNT_DIR

        if repo_path.exists():
            print("Repository already exists.")
            return
        
        index = {}
        config = {'repository_version': REPOSITORY_VERSION, 'default_branch' : MAIN_BRANCH}
        branch_file = f"{HEADS_DIR}/{MAIN_BRANCH}"
        create_directory(ZYNT_DIR)
        create_directory(OBJECTS_DIR)
        create_directory(REFS_DIR)
        create_directory(HEADS_DIR)
        create_file(HEAD_FILE, f"ref: refs/heads/{MAIN_BRANCH}")
        create_file(INDEX_FILE, json.dumps(index, indent=4))
        create_file(CONFIG_FILE, json.dumps(config, indent=4) )
        create_file(branch_file)
        print(f"Initialized empty Zynt repository at {repo_path}")
          
          
    

    
    

