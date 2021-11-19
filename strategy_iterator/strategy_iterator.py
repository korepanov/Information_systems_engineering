from abc import ABC, abstractmethod


# Стратегия + итератор
class Strategy(ABC):
    @abstractmethod
    def make_bread(self, number: int):
        pass


# Стратегия
class Context:
    def __init__(self, strategy: Strategy, limit) -> None:
        self.strategy = strategy
        # Лимит и текущее количество хлеба (итератор)
        self.limit = limit
        self.counter = 0

    @property
    def strategy(self) -> Strategy:
        return self.strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def make_bread(self, number: int) -> None:
        result = self._strategy.make_bread(self, number)
        return result

    # Итератор
    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.make_bread(self.counter)
        else:
            raise StopIteration


class MakeBlackBread(Strategy):
    def make_bread(self, number: int):
        return "+1 black bread, " + str(number) + " bread(s) is(are) ready!"


class MakeWhiteBread(Strategy):
    def make_bread(self, number: int):
        return "+1 white bread, " + str(number) + " bread(s) is(are) ready!"
