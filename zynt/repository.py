from pathlib import Path
from .utils import (create_directory, create_file, read_file, read_json, 
                    find_repository, write_file, write_json, 
                    get_working_files, hash_file, get_untracked_files
                    )

from .utils import get_modified_files, get_latest_commit
from .constants import (ZYNT_DIR, OBJECTS_DIR, REFS_DIR, 
                        HEAD_FILE, HEADS_DIR, INDEX_FILE, 
                        CONFIG_FILE, MAIN_BRANCH, REPOSITORY_VERSION)
import json
import hashlib
import datetime
import json
from colorama import Fore, Style, init

init()

HASH = Fore.GREEN
DATE = Fore.CYAN
MESSAGE = Style.BRIGHT
SEPARATOR = Fore.LIGHTBLACK_EX



class Repository: 
    def __init__(self):
            self.path = Path.cwd()
    
    def init(self):
        repo_path = self.path/ ZYNT_DIR

        if repo_path.exists():
            print(f"{Fore.RED}Repository already exists.{Style.RESET_ALL}")
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
        print(f"{Fore.GREEN}Initialized empty Zynt repository at {repo_path}{Style.RESET_ALL}")
          
    
    def status(self):
        repository = find_repository()
        if repository is None:
            print(f"{Fore.RED}No Repository created yet. Run zynt init to make one.{Style.RESET_ALL}")
            return

        
        untracked_files = get_untracked_files()
        print(f"\n{Fore.RED}Untrakced Files:{Style.RESET_ALL}\n")
        for file in untracked_files:
            print(f" {Fore.RED}{file}{Style.RESET_ALL}")
        
        modified_files = get_modified_files()
        print(f"\n{Fore.GREEN}Modified Files:{Style.RESET_ALL}\n")
        for file in modified_files:
            print(f" {Fore.GREEN}{file}{Style.RESET_ALL}")

        

    
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
            print(f"{Fore.RED}Nothing to commit.{Style.RESET_ALL}")
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
        print(f"{Fore.GREEN}[{MAIN_BRANCH} {commit_hash[:7]}] {message}{Style.RESET_ALL}")

    def log(self):
        latest_hash = read_file(f"{HEADS_DIR}/{MAIN_BRANCH}")

        while latest_hash:
            latest_commit = read_json(f"{OBJECTS_DIR}/{latest_hash}")

            formatted_time = datetime.datetime.fromtimestamp(
                latest_commit["timestamp"]
            ).strftime("%d %b %Y %I:%M:%S %p")

            print(f"{HASH}commit {latest_hash[:7]}")
            print(f"{DATE}Date: {formatted_time}")
            print()
            print(f"    {MESSAGE}{latest_commit['message']}")
            print(f"{SEPARATOR}{'-' * 50}")
            print()

            latest_hash = latest_commit["parent"]
            
                
            



        
                
             

        
        

          
    

    
    

