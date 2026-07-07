# Zynt

> A lightweight version control system built from scratch in Python to understand how Git works internally.

---

# Vision

Zynt is **not** a Git clone.

The goal is to build a modern, beginner-friendly version control system inspired by Git while learning the computer science concepts behind it.

Every feature should prioritize:

- 📖 Readability
- 🧠 Learning
- ⚡ Simplicity
- 🏗 Clean architecture

The project should be something a developer can read from top to bottom and understand how a version control system works.

---

# Goals

- Learn how version control works internally.
- Build a complete CLI application.
- Understand Git's architecture.
- Practice object-oriented programming.
- Learn hashing and content-addressable storage.
- Understand trees and graphs.
- Practice file system manipulation.
- Build a polished open-source project.

---

# Philosophy

Unlike Git, Zynt should:

- Have beginner-friendly commands.
- Produce clear error messages.
- Be easy to read and contribute to.
- Be heavily documented.
- Favor clarity over clever optimizations.

This project is educational first, production second.

---

# Core Concepts

By the end of this project, Zynt should implement:

- Content-addressable storage
- Commit history
- Branches
- Merging
- Staging Area
- Working Directory
- Repository
- References
- Trees
- Blob Objects
- Commit Objects
- Directed Acyclic Graph (DAG)

---

# Features

## Phase 1 — Repository

### Commands

```bash
zynt init
```

### Tasks

- [ ] Create `.zynt/`
- [ ] Create object database
- [ ] Create HEAD
- [ ] Create refs
- [ ] Create config
- [ ] Create index

---

## Phase 2 — Staging Area

### Commands

```bash
zynt add file.txt
zynt status
```

### Tasks

- [ ] Hash files
- [ ] Store blobs
- [ ] Maintain index
- [ ] Detect modified files
- [ ] Detect deleted files

---

## Phase 3 — Commits

### Commands

```bash
zynt commit "Initial commit"
```

### Tasks

- [ ] Commit object
- [ ] Parent reference
- [ ] Timestamp
- [ ] Commit message
- [ ] Update HEAD

---

## Phase 4 — History

### Commands

```bash
zynt log
```

### Tasks

- [ ] Traverse commits
- [ ] Pretty output
- [ ] Short hashes

---

## Phase 5 — Branches

### Commands

```bash
zynt branch feature
zynt checkout feature
```

### Tasks

- [ ] Branch references
- [ ] HEAD switching
- [ ] Detached HEAD support

---

## Phase 6 — Merge

### Commands

```bash
zynt merge feature
```

### Tasks

- [ ] Merge commits
- [ ] Conflict detection
- [ ] Three-way merge

---

## Phase 7 — Restore

### Commands

```bash
zynt restore file.txt
zynt undo
```

### Tasks

- [ ] Restore files
- [ ] Undo commits
- [ ] Safe recovery

---

## Phase 8 — Nice-to-have Features

- [ ] Tags
- [ ] Ignore files
- [ ] Diff viewer
- [ ] Interactive log
- [ ] Colored terminal output
- [ ] Repository statistics
- [ ] Remote repositories

---

# Repository Structure

```
zynt/
│
├── zynt/
│   ├── __init__.py
│   ├── cli.py
│   ├── repository.py
│   ├── objects.py
│   ├── index.py
│   ├── commit.py
│   ├── branch.py
│   ├── merge.py
│   ├── status.py
│   ├── log.py
│   └── utils.py
│
├── tests/
│
├── docs/
│
├── README.md
├── PLAN.md
├── LICENSE
└── pyproject.toml
```

---

# Internal Repository Layout

After running:

```bash
zynt init
```

A project becomes:

```
project/
│
├── .zynt/
│   ├── HEAD
│   ├── config
│   ├── index
│   ├── objects/
│   └── refs/
│       └── heads/
│           └── main
│
├── README.md
└── src/
```

---

# Computer Science Topics Covered

- File Systems
- SHA-256 Hashing
- Object Serialization
- Trees
- Directed Acyclic Graphs
- Linked Lists
- References
- Recursion
- Compression
- CLI Design
- Object-Oriented Programming

---

# Development Rules

## Code Style

- Follow PEP 8.
- Use type hints.
- Keep modules focused.
- Write docstrings.
- Avoid unnecessary dependencies.

---

## Testing

Every feature should include tests.

```
tests/
```

should mirror

```
zynt/
```

---

## Documentation

Every module should explain:

- What problem it solves
- Why it exists
- How it works

The project should be understandable to someone learning version control for the first time.

---

# Long-Term Goal

Build a version control system that is:

- Easy to read
- Fun to build
- Educational
- Open source
- Portfolio-worthy

By the end of the project, a reader should understand not only *how to use* Git, but *how a version control system works under the hood*.

---

# Motto

> "Learn by building. Understand by simplifying."