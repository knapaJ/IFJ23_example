import sys
from typing import IO


class EndOfFile:
    def __eq__(self, other):
        if type(self) is type(other):
            return True
        return False


EOF = EndOfFile()


class InStream:
    """Peekovatelný stream znaků ze souboru"""
    def __init__(self, file: IO[str]):
        self._file = file
        self.current_char: str = ""
        self.read_next_char()

    def read_next_char(self):
        self.current_char = self._file.read(1)
        if self.current_char == "":
            self.current_char = EOF

    def __bool__(self):
        if self.current_char == EOF:
            return False
        return True


if __name__ == "__main__":
    stream = InStream(sys.stdin)
    while stream:
        print(f"Got character: {stream.current_char}")
        stream.read_next_char()
    print("Ended.")
