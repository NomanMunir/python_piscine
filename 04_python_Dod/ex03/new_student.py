import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Student dataclass with auto-generated login and id.

    Args:
        name: Student's name
        surname: Student's surname
        active: Whether student is active (default True)
        login: Auto-generated from name (not initializable)
        id: Auto-generated random ID (not initializable)
    """

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Generate login and id after initialization."""
        self.login = self.name.capitalize()
        self.id = generate_id()


def main():
    """Main function for testing."""
    # Test the dataclass as shown in the example
    student = Student(name="Edward", surname="agle")
    print(student)

    # Test that login and id are not initializable
    try:
        student2 = Student(name="Edward", surname="agle", id="toto")
        print(student2)
    except TypeError as e:
        print(f"TypeError: {e}")


if __name__ == "__main__":
    main()
