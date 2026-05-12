from __future__ import annotations

import json
from typing import Any, AsyncGenerator, Dict, Optional

from websockets.client import WebSocketClientProtocol, connect

from . import commands
from .models import CiderEvent


class CiderWsClient:
    def __init__(
        self,
        host: str = "127.0.0.1",
        port: int = 26369,
        client_name: str = "cider-ws",
        client_author: str = "unknown",
        client_description: str = "Python SDK",
        client_version: str = "0.1.0",
    ) -> None:
        self.host = host
        self.port = port
        self.client_name = client_name
        self.client_author = client_author
        self.client_description = client_description
        self.client_version = client_version
        self._ws: Optional[WebSocketClientProtocol] = None

    @property
    def url(self) -> str:
        return f"ws://{self.host}:{self.port}"

    async def connect(self, identify: bool = True) -> None:
        self._ws = await connect(self.url)
        if identify:
            await self.request(
                commands.identify(
                    name=self.client_name,
                    author=self.client_author,
                    description=self.client_description,
                    version=self.client_version,
                )
            )

    async def close(self) -> None:
        if self._ws is not None:
            await self._ws.close()
            self._ws = None

    async def __aenter__(self) -> "CiderWsClient":
        await self.connect()
        return self

    async def __aexit__(self, *_exc_info: object) -> None:
        await self.close()

    def _require_ws(self) -> WebSocketClientProtocol:
        if self._ws is None:
            raise RuntimeError("Client is not connected")
        return self._ws

    async def send(self, payload: Dict[str, Any]) -> None:
        ws = self._require_ws()
        await ws.send(json.dumps(payload))

    async def recv(self) -> CiderEvent:
        ws = self._require_ws()
        raw_msg = await ws.recv()
        data = json.loads(raw_msg)
        if not isinstance(data, dict):
            raise ValueError("Unexpected non-object WS message")
        return CiderEvent.from_raw(data)

    async def request(self, payload: Dict[str, Any]) -> CiderEvent:
        await self.send(payload)
        return await self.recv()

    async def events(self) -> AsyncGenerator[CiderEvent, None]:
        while True:
            yield await self.recv()

    async def status(self) -> CiderEvent:
        return await self.request(commands.get_status())

    async def playpause(self) -> CiderEvent:
        return await self.request(commands.playpause())

    async def play(self) -> CiderEvent:
        return await self.request(commands.play())

    async def pause(self) -> CiderEvent:
        return await self.request(commands.pause())

    async def next(self) -> CiderEvent:
        return await self.request(commands.next_track())

    async def previous(self) -> CiderEvent:
        return await self.request(commands.previous_track())

    async def seek(self, seconds: float) -> CiderEvent:
        return await self.request(commands.seek(seconds))

    async def volume(self, value: float) -> CiderEvent:
        return await self.request(commands.set_volume(value))

    async def current_media_item(self) -> CiderEvent:
        return await self.request(commands.get_current_media_item())

    async def queue(self) -> CiderEvent:
        return await self.request(commands.get_queue())

    async def search(self, term: str, limit: int = 10) -> CiderEvent:
        return await self.request(commands.search(term, limit=limit))

    async def search_library(self, term: str, limit: int = 10) -> CiderEvent:
        return await self.request(commands.search_library(term, limit=limit))

    async def play_media_item(self, item_id: str, kind: str = "song") -> CiderEvent:
        return await self.request(commands.play_media_item(item_id=item_id, kind=kind))

    async def library_status(self, item_type: str, item_id: str) -> CiderEvent:
        return await self.request(commands.library_status(item_type=item_type, item_id=item_id))

    async def rate(self, item_type: str, item_id: str, rating: int) -> CiderEvent:
        return await self.request(commands.rate(item_type=item_type, item_id=item_id, rating=rating))

    async def change_library(self, item_type: str, item_id: str, add: bool) -> CiderEvent:
        return await self.request(commands.change_library(item_type=item_type, item_id=item_id, add=add))
