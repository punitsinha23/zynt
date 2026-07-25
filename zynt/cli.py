import argparse
from .repository import Repository

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    subparsers.add_parser('init')
    subparsers.add_parser('status')
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("file")

    commit_parser = subparsers.add_parser("commit")
    commit_parser.add_argument("message")
    args = parser.parse_args()


    repo = Repository()

    if args.command == 'init':
        repo.init()
    elif args.command == 'status':
        repo.status()
    elif args.command == 'add':
        repo.add(args.file)
    elif args.command == 'commit':
        repo.commit(args.message)
