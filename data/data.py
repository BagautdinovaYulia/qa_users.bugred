from dataclasses import dataclass


@dataclass
class Person:
    name: str = None
    email: str = None

@dataclass
class Password:
    password: str = None
