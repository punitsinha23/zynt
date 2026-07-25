from pathlib import Path
from .utils import (create_directory, create_file, read_file, read_json, 
                    find_repository, write_file, write_json, 
                    get_working_files, hash_file, get_untracked_files
                    )

from .utils import get_modified_files, get_latest_commit
from .constants import ZYNT_DIR, OBJECTS_DIR, REFS_DIR, HEAD_FILE, HEADS_DIR, INDEX_FILE, CONFIG_FILE, MAIN_BRANCH, REPOSITORY_VERSION
import json
import hashlib
import datetime 
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
          
    
    def status(self):
        repository = find_repository()
        if repository is None:
            print("No Repository created yet. Run zynt init to make one.")
            return

        
        untracked_files = get_untracked_files()
        print("\nUntrakced Files:\n")
        for file in untracked_files:
            print(f"    {file}")
        
        modified_files = get_modified_files()
        print("\nModified Files:\n")
        for file in modified_files:
            print(f"    {file}")

        

    
    def add(self , file_path):
        content = read_file(file_path)
        content_hash = hash_file(content)

        index = read_json(INDEX_FILE)
        index[str(file_path)] = content_hash
        write_json(INDEX_FILE, index)
        
        write_file(f".zynt/objects/{content_hash}" , content)

    def commit(self , message ):
        index = read_json(INDEX_FILE)
        if not index:
            print("Nothing to commit.")
            return

        current_parent = read_file(f"{HEADS_DIR}/{MAIN_BRANCH}")
        parent = current_parent or None
            
        date_time = datetime.datetime.now()
        commit = {
            'message' : message,
            'parent' : parent,
            'timestamp': date_time.timestamp(),
            'files' : index 
        }

        commit_json = json.dumps(commit, indent=4)
        commit_hash = hash_file(commit_json)
        write_file( f"{OBJECTS_DIR}/{commit_hash}", commit_json)
        write_file(f"{HEADS_DIR}/{MAIN_BRANCH}", commit_hash)
        write_json(INDEX_FILE, {})
        print(f"[{MAIN_BRANCH} {commit_hash[:7]}] {message}")
        
    
        
      



        
                
             

        
        

          
    

    
    

