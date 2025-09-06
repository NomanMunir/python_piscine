from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A king that inherits from both Baratheon and Lannister houses."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a King character."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """Set the eye color of the king."""
        self.eyes = color

    def set_hairs(self, color):
        """Set the hair color of the king."""
        self.hairs = color

    def get_eyes(self):
        """Get the eye color of the king."""
        return self.eyes

    def get_hairs(self):
        """Get the hair color of the king."""
        return self.hairs

k = King("Robert")
print(k)