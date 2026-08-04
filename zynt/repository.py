from pathlib import Path
from .utils import (create_directory, create_file, read_file, read_json, 
                    find_repository, write_file, write_json, 
                    get_working_files, hash_file, get_untracked_files
                    )

from .utils import get_modified_files, get_latest_commit, is_branch, get_current_branch
from .constants import (ZYNT_DIR, OBJECTS_DIR, REFS_DIR, 
                        HEAD_FILE, HEADS_DIR, INDEX_FILE, 
                        CONFIG_FILE, MAIN_BRANCH, REPOSITORY_VERSION)
import json
import datetime
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
        branch = MAIN_BRANCH
        if repo_path.exists():
            print(f"{Fore.RED}Repository already exists.{Style.RESET_ALL}")
            return
        
        index = {}
        config = {'repository_version': REPOSITORY_VERSION, 'default_branch' : MAIN_BRANCH}
        branch_file = f"{HEADS_DIR}/{branch}"
        create_directory(ZYNT_DIR)
        create_directory(OBJECTS_DIR)
        create_directory(REFS_DIR)
        create_directory(HEADS_DIR)
        create_file(HEAD_FILE, f"ref: refs/heads/{branch}")
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

        

    
    def add(self , files):
        repo = find_repository()

        if repo is None:
            print("No repository found. Run 'zynt init' first.")
            return
        
        index = read_json(INDEX_FILE)

        for file in files:
            content = read_file(file)
            content_hash = hash_file(content)
            index[str(file)] = content_hash
            
        
            write_file(f"{OBJECTS_DIR}/{content_hash}", content)
        write_json(INDEX_FILE, index)
        print(f"{Fore.GREEN}Added {len(files)} files to the staging area.{Style.RESET_ALL}")

    def commit(self , message ):
        branch = get_current_branch()
        index = read_json(INDEX_FILE)
        if not index:
            print(f"{Fore.RED}Nothing to commit.{Style.RESET_ALL}")
            return

        current_parent = read_file(f"{HEADS_DIR}/{branch}")
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
        write_file(f"{HEADS_DIR}/{branch}", commit_hash)
        print(f"{Fore.GREEN}[{branch} {commit_hash[:7]}] {message}{Style.RESET_ALL}")

    def log(self):
        branch = get_current_branch()
        latest_hash = read_file(f"{HEADS_DIR}/{branch}")

        while latest_hash:
            latest_commit = read_json(f"{OBJECTS_DIR}/{latest_hash}")

            formatted_time = datetime.datetime.fromtimestamp(
                latest_commit["timestamp"]
            ).strftime("%d %b %Y %I:%M:%S %p")

            print(f"{HASH}commit {latest_hash}")
            print(f"{DATE}Date: {formatted_time}")
            print()
            print(f"    {MESSAGE}{latest_commit['message']}")
            print(f"{SEPARATOR}{'-' * 50}")
            print()

            latest_hash = latest_commit["parent"]

    def checkout(self, target):
        branch = is_branch(target)

        if branch:
            commit_hash = read_file(f"{HEADS_DIR}/{target}")
        else:
            commit_hash = target

        commit_path = Path(OBJECTS_DIR) / commit_hash
        if not commit_path.exists():
            print("Commit not found.")
            return

        commit = read_json(f"{OBJECTS_DIR}/{commit_hash}")
        files = commit["files"]

        # Restore working tree
        for file_path, blob_hash in files.items():
            blob = read_file(f"{OBJECTS_DIR}/{blob_hash}")
            write_file(file_path, blob)
    
        write_json(INDEX_FILE, files)

        if branch:
            write_file(HEAD_FILE, f"ref: refs/heads/{target}")
            print(f"Switched to branch '{target}'")
        else:
            current_branch = get_current_branch()
            write_file(f"{HEADS_DIR}/{current_branch}", commit_hash)
            print(f"Checked out commit {commit_hash[:7]}")


    def branch(self, branch_name ):
        branch_path = Path(HEADS_DIR) / branch_name
        branch = get_current_branch()
        if branch_path.exists():
            print(f"Branch '{branch_name}' already exists.")
            return
        
        current_hash = read_file(f"{HEADS_DIR}/{branch}")
        create_file(f"{HEADS_DIR}/{branch_name}")  
        write_file(f"{HEADS_DIR}/{branch_name}", current_hash)
