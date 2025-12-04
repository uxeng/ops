from typing import List, Optional

class App:
    def __init__(self, arg1: str, arg2: str, level: int, tags: Optional[List[str]] = None):
        self.arg1: str = arg1
        self.arg2: str = arg2
        self.level: int = level
        self.tags: List[str] = tags if tags is not None else []

    def add_tag(self, tag: str) -> None:
        self.tags.append(tag)

    def summary(self) -> str:
        return f"{self.arg1} {self.arg2}, {self.level}"

    def has_tag(self, tag: str) -> bool:
        return tag in self.tags

