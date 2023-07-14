import abc
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


class ILogger(abc.ABC):

    @abc.abstractmethod
    def info(self, msg, *args, **kwargs): ...

    @abc.abstractmethod
    def error(self, msg, *args, **kwargs): ...

    @abc.abstractmethod
    def warning(self, msg, *args, **kwargs): ...

    @abc.abstractmethod
    def error(self, msg, *args, **kwargs): ...

    @abc.abstractmethod
    def debug(self, msg, *args, **kwargs): ...
