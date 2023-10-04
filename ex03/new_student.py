import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        try:
            if not isinstance(self.name, str) or \
               not isinstance(self.surname, str):
                raise TypeError("Name and surname must be valid strings.")
            self.login = self.name[0] + self.surname

        except TypeError as e:
            self.login = ""
            print(e)

        self.id = generate_id()
