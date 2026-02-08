from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid

@dataclass
class MagicLink:
    first_name: str
    token: str = field(default_factory=lambda: str(uuid.uuid4()))
    is_used: bool = False
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def mark_as_used(self):
        self.is_used = True
