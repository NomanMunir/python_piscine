from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class representing a character.

    This class defines the basic structure and behavior that all characters
    must implement. It cannot be instantiated directly.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a character with a first name and alive status.

        Args:
            first_name (str): The character's first name
            is_alive (bool): Whether the character is alive (default: True)
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method to handle character death.

        This method must be implemented by all subclasses to define how a
        character dies and changes their alive status.
        """
        pass


class Stark(Character):
    """A concrete Character implementation representing a House Stark member.

    This class inherits from Character and implements the required abstract
    methods. Stark characters can die, changing their alive status to False.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Stark character.

        Args:
            first_name (str): The Stark character's first name
            is_alive (bool): Whether the character is alive (default: True)
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """Kill the Stark character by setting their alive status to False.

        This method implements the abstract die method from the Character
        class, defining how a Stark character dies.
        """
        self.is_alive = False
