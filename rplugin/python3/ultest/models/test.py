import json
from dataclasses import asdict, dataclass


@dataclass(repr=False)
class Test:

    id: str
    name: str
    file: str
    line: int
    col: int
    running: int

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        props = self.dict()
        props["name"] = [int(char) for char in self.name.encode()]
        return json.dumps(props)

    def dict(self):
        return asdict(self)
