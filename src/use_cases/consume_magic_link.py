from src.core.ports.magic_link_repository import MagicLinkRepository
from src.core.exceptions import MagicLinkNotFound, MagicLinkAlreadyUsed

class ConsumeMagicLink:
    def __init__(self, repository: MagicLinkRepository):
        self.repository = repository

    def execute(self, token: str) -> str:
        magic_link = self.repository.get_by_token(token)
        if not magic_link:
            raise MagicLinkNotFound("Invalid token")

        if magic_link.is_used:
            raise MagicLinkAlreadyUsed("This link has already been used")

        magic_link.mark_as_used()
        self.repository.save(magic_link)

        return magic_link.first_name
