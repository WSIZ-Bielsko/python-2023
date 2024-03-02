from dataclasses import dataclass


@dataclass
class A:
    a: int
    b: int


a = A(a=10, b=12)
print(a)
