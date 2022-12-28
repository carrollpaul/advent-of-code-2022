from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import accumulate
from pathlib import Path

from rich import print

# This solution is essentially copied from u/4HbQ's solution on Reddit
# Such an elegant way to use accumulate()
dirs = defaultdict(int)
curr = []
with open("input.txt") as f:
    for line in f.readlines():
        match line.split():
            case "$", "ls":
                pass
            case "dir", _:
                pass
            case "$", "cd", "/":
                curr.append("/")
            case "$", "cd", "..":
                curr.pop()
            case "$", "cd", name:
                curr.append(f"{name}/")
            case size, _:
                for path in accumulate(curr):
                    dirs[path] += int(size)

# Part 1
print(sum(amount for amount in dirs.values() if amount <= 100_000))

# Part 2
total = 70_000_000
required = 30_000_000
occupied = total - dirs["/"]
to_be_freed = required - occupied
print(min(amount for amount in dirs.values() if amount >= to_be_freed))

# Below is my original attempt at solving this day's puzzle...
@dataclass
class File:

    name: str
    size: int

    def __repr__(self) -> str:
        return self.name


class Directory:
    def __init__(
        self,
        name: str,
        parent: Directory | None = None,
        children: dict[str, Directory] | None = None,
        files: list[File] | None = None,
    ) -> None:
        self.name = name
        self.parent = parent
        self.children = children if children else {}
        self.files = files if files else []

    def __repr__(self) -> str:
        if not self.parent:
            parent_name = "None"
        else:
            parent_name = self.parent.name
        return f"Name: {self.name}, Parent: {parent_name}, Children: {list(self.children.keys())}, Files: {self.files}"

    def size(self, curr_total: int = 0) -> int:
        # Get size of files in diretory and subdirectory
        for file in self.files:
            curr_total += file.size

        for child in self.children.values():
            curr_total += child.size(curr_total)

        return curr_total


def find_root(dir: Directory) -> Directory:
    while True:
        if dir.parent == None:
            return dir
        dir = dir.parent


def get_total(dir: Directory, total: int = 0) -> int:
    if dir.size() <= 100_000:
        total += dir.size()
    for child in dir.children.values():
        total += get_total(child, total)

    return total


dir = Directory(name="/")

input_file = Path().home() / "code" / "advent-of-code-2022" / "day7" / "input.txt"
with open(input_file) as f:
    for line in f.readlines():
        if "$ cd" in line:
            if "/" in line:
                continue

            if ".." in line:
                dir = dir.parent  # type: ignore
                continue

            else:
                _, _, dir_name = line.split()
                dir = dir.children[dir_name]  # type: ignore
                continue

        if "$ ls" in line:
            continue

        if line.startswith("dir"):
            _, name = line.split()
            dir.children[name] = Directory(name=name, parent=dir)  # type: ignore

        else:
            size, name = line.split()
            dir.files.append(File(name, int(size)))
