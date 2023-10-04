from abc import ABC, abstractmethod


class Character(ABC):
    """A character."""

    def __init__(self, first_name, is_alive=True):
        """Instantiate a Character."""

        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Unalive a character."""

        ...


class Stark(Character):
    """Representing the Stark family."""

    def __init__(self, first_name, is_alive=True):
        """Instantiate a Stark."""

        super().__init__(first_name, is_alive)

    def die(self):
        """Unalive a Stark."""

        if self.is_alive:
            self.is_alive = False
