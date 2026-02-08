from abc import ABC, abstractmethod
from typing import Optional
from src.core.entities.magic_link import MagicLink

class MagicLinkRepository(ABC):
    @abstractmethod
    def save(self, magic_link: MagicLink) -> None:
        pass

    @abstractmethod
    def get_by_token(self, token: str) -> Optional[MagicLink]:
        pass
