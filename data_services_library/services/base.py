import abc

class DataServiceBase(object):
    """Base class for data services plugins
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.register()


    @abc.abstractmethod
    def register(self):
        """Register plugin by setting service name, source and uid 
        """