from abc import abstractmethod
from abc import ABCMeta

class ModalityComponent(metaclass=ABCMeta):
    @abstractmethod
    def input_mc(self):
        pass

    @abstractmethod
    def output(self):
        pass