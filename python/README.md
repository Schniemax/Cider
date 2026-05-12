# Cider Python WebSocket SDK

A standalone Python SDK/CLI for Cider v1's WebSocket API (`ws://127.0.0.1:26369`).

## What it covers

- Core actions: identify, play/pause/next/previous, seek, volume
- Queue/search actions: get queue, search, library search, play media item
- Library actions: status, rating, add/remove library
- Typed event parsing for common broadcast responses:
  - `playbackStateUpdate`
  - `queue`
  - `lyrics`
  - `searchResults`
  - `searchResultsLibrary`
  - `libraryStatus`
  - `rate`
  - `change-library`

## Quick start

```bash
cd /home/runner/work/Cider/Cider/python
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## CLI examples

```bash
cider-ws status
cider-ws playpause
cider-ws next
cider-ws previous
cider-ws volume --value 0.5
cider-ws search --term "Daft Punk" --limit 5
```

## SDK example

See: `/home/runner/work/Cider/Cider/python/examples/basic_usage.py`

## Tests

```bash
cd /home/runner/work/Cider/Cider/python
python -m unittest discover -s tests -v
```

Optional integration test against a running Cider instance:

```bash
CIDER_WS_INTEGRATION=1 python -m unittest -v tests.test_integration_optional
```

## Extension points

- Add convenience methods in `cider_ws/client.py`
- Add new action payload builders in `cider_ws/commands.py`
- Extend event type handling in `cider_ws/models.py`
