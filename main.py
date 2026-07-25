from zynt import repository


def main():
    repo = repository.Repository()

    repo.add("main.py")
    repo.add("test2.txt")
    repo.commit("second commit.")
    # Show repository status
    repo.status()


if __name__ == "__main__":
    main()