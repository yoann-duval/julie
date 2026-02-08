from src.core.entities.magic_link import MagicLink
from src.core.ports.magic_link_repository import MagicLinkRepository

class GenerateMagicLink:
    def __init__(self, repository: MagicLinkRepository):
        self.repository = repository

    def execute(self, first_name: str) -> str:
        magic_link = MagicLink(first_name=first_name)
        self.repository.save(magic_link)
        return magic_link.token
