import datetime
import uuid
from dataclasses import dataclass, field

@dataclass
class logEntry:
    message: str
    tags: list[str]
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime.datetime = field(default_factory=datetime.datetime.now)