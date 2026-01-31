from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Literal

@dataclass
class Message:
    content: str
    role: Literal["user", "ai", "system"]
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
