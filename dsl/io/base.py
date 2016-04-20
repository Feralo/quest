"""Base Class for I/O plugins


"""
from builtins import object
import abc
from future.utils import with_metaclass

class IoBase(with_metaclass(abc.ABCMeta, object)):
    """Base class for I/O for different file formats
    """

    def __init__(self):
        self.register()


    @abc.abstractmethod
    def register(self):
        """Register plugin by setting description and io type
        """

    @abc.abstractmethod
    def read(self):
        """Write data to format
        """

    @abc.abstractmethod
    def write(self):
        """Write data to format
        """
