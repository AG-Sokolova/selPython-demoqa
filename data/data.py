from dataclasses import dataclass

@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    middle_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
    age: str = None
    salary: str = None
    department: str = None
