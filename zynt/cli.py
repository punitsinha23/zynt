import argparse
from .repository import Repository
from .utils import get_working_files

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    subparsers.add_parser('init')
    subparsers.add_parser('status')
    subparsers.add_parser('log')
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("files", nargs="*")
    add_parser.add_argument("--all", action="store_true")

    commit_parser = subparsers.add_parser("commit")
    commit_parser.add_argument("message")
    args = parser.parse_args()


    repo = Repository()

    if args.command == 'init':
        repo.init()
    elif args.command == 'status':
        repo.status()
    elif args.command == 'add':
        if args.all:
            repo.add(get_working_files())
        else:
            repo.add(args.files)
    elif args.command == 'log':
        repo.log()
    elif args.command == 'commit':
        repo.commit(args.message)
