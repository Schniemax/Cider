from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass(slots=True)
class CiderEvent:
    status: Optional[int]
    message: Optional[str]
    data: Any
    type: str
    raw: Dict[str, Any]

    @classmethod
    def from_raw(cls, payload: Dict[str, Any]) -> "CiderEvent":
        event_type = str(payload.get("type", "generic"))
        status = payload.get("status")
        message = payload.get("message")
        data = payload.get("data")
        return cls(status=status, message=message, data=data, type=event_type, raw=payload)

    @property
    def is_playback_update(self) -> bool:
        return self.type == "playbackStateUpdate"

    @property
    def is_queue(self) -> bool:
        return self.type == "queue"

    @property
    def is_lyrics(self) -> bool:
        return self.type == "lyrics"

    @property
    def is_search_results(self) -> bool:
        return self.type in {"searchResults", "searchResultsLibrary"}

    @property
    def is_library_status(self) -> bool:
        return self.type == "libraryStatus"
