from pathlib import Path
from typing import Optional
from dataclasses import dataclass
from functools import cached_property

@dataclass
class CommandResult:
    return_code: int
    stdout: str
    stderr: str
    cmdlist: list[str]

    @cached_property
    def output(self):
        return self.stdout + self.stderr

    @cached_property
    def program(self):
        return Path(self.cmdlist[0].strip("'")).name

    def __repr__(self) -> str:
        return f"CommandResult(program={self.program}, return_code={self.return_code})"

class ExtractResult:
    def __init__(self, command_result: Optional[CommandResult] = None, program: Optional[str] = None, extract_dir: Optional[str] = None):
        self.command_result = command_result
        self.program = command_result.program if command_result else program
        self.extract_dir = extract_dir
