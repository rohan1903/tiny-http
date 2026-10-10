# TinyHTTP

An educational HTTP/1.1 server and minimal web framework built from scratch in Python.

## About

TinyHTTP explores how web servers work beneath frameworks such as FastAPI and Flask.

The project is being developed incrementally to study TCP sockets, HTTP message parsing, routing, response generation, concurrency, and software engineering practices.

**Status:** Early development. The HTTP server is not yet implemented.

## Requirements

- Python 3.12+
- uv

## Development Setup

```bash
uv sync
```

## Development Checks

```bash
uv run ruff check .
uv run ruff format --check .
uv run basedpyright
uv run pytest
```

## Documentation

- [Development Roadmap](docs/roadmap.md)
- [Architecture](docs/architecture.md)
- [Project Progress](docs/progress.md)

## Scope

TinyHTTP is a learning project, not a production-ready HTTP server.

## License

Not yet selected.
