from __future__ import annotations

from typing import Any, Dict


def action(name: str, **kwargs: Any) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"action": name}
    payload.update(kwargs)
    return payload


def identify(name: str = "cider-ws", author: str = "unknown", description: str = "Python SDK", version: str = "0.1.0") -> Dict[str, Any]:
    return action("identify", name=name, author=author, description=description, version=version)


def playpause() -> Dict[str, Any]:
    return action("playpause")


def play() -> Dict[str, Any]:
    return action("play")


def pause() -> Dict[str, Any]:
    return action("pause")


def next_track() -> Dict[str, Any]:
    return action("next")


def previous_track() -> Dict[str, Any]:
    return action("previous")


def seek(seconds: float) -> Dict[str, Any]:
    return action("seek", time=float(seconds))


def set_volume(value: float) -> Dict[str, Any]:
    return action("volume", volume=float(value))


def get_status() -> Dict[str, Any]:
    return action("get-status")


def get_current_media_item() -> Dict[str, Any]:
    return action("get-currentmediaitem")


def get_queue() -> Dict[str, Any]:
    return action("get-queue")


def search(term: str, limit: int = 10) -> Dict[str, Any]:
    return action("search", term=term, limit=int(limit))


def search_library(term: str, limit: int = 10) -> Dict[str, Any]:
    return action("library-search", term=term, limit=int(limit))


def play_media_item(item_id: str, kind: str = "song") -> Dict[str, Any]:
    return action("play-mediaitem", id=item_id, kind=kind)


def play_next(item_type: str, item_id: str) -> Dict[str, Any]:
    return action("play-next", type=item_type, id=item_id)


def play_later(item_type: str, item_id: str) -> Dict[str, Any]:
    return action("play-later", type=item_type, id=item_id)


def library_status(item_type: str, item_id: str) -> Dict[str, Any]:
    return action("library-status", type=item_type, id=item_id)


def rate(item_type: str, item_id: str, rating: int) -> Dict[str, Any]:
    return action("rating", type=item_type, id=item_id, rating=int(rating))


def change_library(item_type: str, item_id: str, add: bool) -> Dict[str, Any]:
    return action("change-library", type=item_type, id=item_id, add=bool(add))
