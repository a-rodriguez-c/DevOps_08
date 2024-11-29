from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)

class BaseCommand(ABC):
    @abstractmethod
    def execute(self): # pragma: no cover
        logger.error("Please implement in subclass")
        raise NotImplementedError("Please implement in subclass")