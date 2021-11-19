from abc import ABC, abstractmethod

# Стратегия 
class Strategy(ABC):
    @abstractmethod 
    def make_bread(self, number: int):
        pass
    
class Context():
    def __init__(self, strategy: Strategy) -> None: 
        self.strategy = strategy
        
    @property
    def strategy(self) -> Strategy:
        return self.strategy
    
    @strategy.setter
    def strategy(self, strategy: Strategy) -> None: 
        self._strategy = strategy 
    
    def make_bread(self, number: int) -> None: 
        print("Now I am baking bread (not sure, how I'll do it)")
        result = self._strategy.make_bread(self, number)
        print(result)
        
    

    
class MakeBlackBread(Strategy):
    def make_bread(self, number: int):
        return str(number) + " black bread(s) is(are) ready!"
        
class MakeWhiteBread(Strategy):
    def make_bread(self, number: int):
        return str(number) + " white bread(s) is(are) ready!"
