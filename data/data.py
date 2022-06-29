from dataclasses import dataclass


@dataclass
class Person:
    data: str = None
    email: str = None
    password: str = None
