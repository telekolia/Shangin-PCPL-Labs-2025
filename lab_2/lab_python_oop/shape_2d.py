from abc import ABC, abstractmethod

class Shape2D(ABC):
    @property
    @abstractmethod
    def shape_type(self):
        pass

    @property
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    # @abstractmethod
    # def draw():
    #     pass
