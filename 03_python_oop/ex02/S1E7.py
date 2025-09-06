from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Baratheon character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Kill the Baratheon character."""
        self.is_alive = False

    def __str__(self):
        """Return string representation of Baratheon character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return detailed string representation of Baratheon character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Lannister character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Kill the Lannister character."""
        self.is_alive = False

    def __str__(self):
        """Return string representation of Lannister character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return detailed string representation of Lannister character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Create a Lannister character from Lannister class."""
        return cls(first_name, is_alive)
