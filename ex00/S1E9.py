from abc import ABC, abstractmethod


class Character(ABC):
    """A character"""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Initialize an instance of a character."""

        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Unalive a character."""

        if self.is_alive:
            self.is_alive = False


class Stark(Character):
    """Representing the Stark family."""

    def __init__(self, first_name, is_alive=True):
        """Initialize an instance of a Stark."""

        super().__init__(first_name, is_alive)

    # def die(self):
    #     """Kill a Stark"""

    #     if self.is_alive:
    #         self.is_alive = False
