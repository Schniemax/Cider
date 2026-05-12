from __future__ import annotations

import argparse
import asyncio
import json
from typing import Optional

from .client import CiderWsClient


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="cider-ws", description="Cider WebSocket CLI")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=26369)

    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status")
    sub.add_parser("playpause")
    sub.add_parser("next")
    sub.add_parser("previous")

    volume = sub.add_parser("volume")
    volume.add_argument("--value", type=float, required=True)

    search = sub.add_parser("search")
    search.add_argument("--term", required=True)
    search.add_argument("--limit", type=int, default=10)

    return parser


async def _run(args: argparse.Namespace) -> int:
    async with CiderWsClient(host=args.host, port=args.port) as client:
        if args.command == "status":
            event = await client.status()
        elif args.command == "playpause":
            event = await client.playpause()
        elif args.command == "next":
            event = await client.next()
        elif args.command == "previous":
            event = await client.previous()
        elif args.command == "volume":
            event = await client.volume(args.value)
        elif args.command == "search":
            event = await client.search(term=args.term, limit=args.limit)
        else:
            raise ValueError(f"Unsupported command: {args.command}")

    print(json.dumps(event.raw, indent=2, sort_keys=True))
    return 0


def main(argv: Optional[list[str]] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    return asyncio.run(_run(args))


if __name__ == "__main__":
    raise SystemExit(main())
