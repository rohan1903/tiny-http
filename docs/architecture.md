# TinyHTTP — Architecture

## Status

Design proposal. No HTTP server functionality has been implemented yet.

## Intended Request Lifecycle

1. A client establishes a TCP connection.
2. The server receives bytes from the connection.
3. The HTTP parser interprets the request.
4. The router identifies the appropriate handler.
5. The handler executes application logic.
6. The response component constructs an HTTP response.
7. The server transmits the response bytes.

## Planned Components

### TCP Server
Manages listening sockets, connections, network I/O, and connection lifecycle.

### HTTP Request Parser
Converts incoming HTTP/1.1 messages into structured request objects. Responsible for message framing, validation, and rejecting malformed requests.

### Router
Maps HTTP methods and request paths to Python handler functions.

### Request and Response Models
Provide structured representations of HTTP requests and responses.

### Application Interface
Offers a minimal API for registering handlers and starting the server.

## Design Constraints

- Python 3.12 or later
- HTTP/1.1 as the initial protocol target
- Python standard library for core server functionality
- Localhost development initially
- No production-readiness claims
- Explicit resource limits and input validation
- Automated unit and integration testing

## Architectural Decisions

No implementation decisions have been finalized.

As each phase progresses, record important decisions here, including alternatives considered, trade-offs, and known limitations.
