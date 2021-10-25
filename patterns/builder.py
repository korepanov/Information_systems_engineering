from abc import ABC, abstractmethod
from typing import Any 

class Bread():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}")

class Builder(ABC):
    @property 
    @abstractmethod
    def bread(self) -> None:
        pass

    @abstractmethod
    def produce_solt(self) -> None:
        pass

    @abstractmethod
    def produce_flour(self) -> None:
        pass
    
class ConcreteBuilder(Builder):
    def __init__(self) -> None:
        self.reset()
        
    def reset(self) -> None:
        self._bread = Bread()
        
    @property
    def bread(self) -> Bread:
        bread = self._bread
        self.reset()
        return bread
        
    def produce_solt(self) -> None:
        self._bread.add("Solt")

    def produce_flour(self) -> None:
        self._bread.add("Flour")
