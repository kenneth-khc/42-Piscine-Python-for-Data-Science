from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing a King."""

    def __init__(self, first_name, is_alive=True):
        """Initializes an instance of a King."""

        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """Get eye color of a King"""

        return self.eyes

    def get_hairs(self):
        """Get hair color of a King"""

        return self.hairs

    def set_eyes(self, new_color):
        """Set new eye color for a King"""

        self.eyes = new_color

    def set_hairs(self, new_color):
        """Set new hair color for a King"""

        self.hairs = new_color
