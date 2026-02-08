from typing import Dict, Optional
from src.core.entities.magic_link import MagicLink
from src.core.ports.magic_link_repository import MagicLinkRepository

class InMemoryMagicLinkRepository(MagicLinkRepository):
    def __init__(self):
        self._storage: Dict[str, MagicLink] = {}

    def save(self, magic_link: MagicLink) -> None:
        self._storage[magic_link.token] = magic_link

    def get_by_token(self, token: str) -> Optional[MagicLink]:
        return self._storage.get(token)
