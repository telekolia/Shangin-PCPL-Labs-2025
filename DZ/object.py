from abc import ABC, abstractmethod

class StaticObject(ABC):
    @property
    @abstractmethod
    def type(self):
        return self.type

    @abstractmethod
    def draw(self, window):
        pass


class ActiveObject(StaticObject):
    @property
    @abstractmethod
    def type(self):
        return self.type

    @abstractmethod
    def update(self, world):
        pass

    @abstractmethod
    def draw(self, window):
        pass
