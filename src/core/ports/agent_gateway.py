from abc import ABC, abstractmethod
from typing import AsyncGenerator
from src.core.entities.message import Message

class AgentGateway(ABC):
    @abstractmethod
    async def chat(self, message: Message) -> AsyncGenerator[str, None]:
        """
        Sends a message to the agent and yields chunks of the response.
        """
        pass
