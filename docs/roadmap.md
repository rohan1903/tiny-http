# TinyHTTP — Development Roadmap

## Project Goal

Build an educational HTTP/1.1 server and minimal web framework from scratch using Python's standard library.

The project prioritizes understanding networking, protocol design, software architecture, testing, and concurrency over production deployment.

## Phase 0 — Project Setup

- [x] Initialize Git repository
- [x] Initialize Python library using uv
- [x] Configure development dependencies
- [x] Configure Ruff, pytest, and basedpyright
- [ ] Complete initial documentation
- [ ] Create initial Git commit

**Completion criteria:** The development environment is reproducible, static checks pass, and the repository documents its intended architecture.

## Phase 1 — Networking and HTTP Fundamentals

Learn clients and servers, IP addresses, ports, TCP, sockets, HTTP methods, request and response structure, and byte encoding.

**Deliverable:** Small networking experiments and a written explanation of the HTTP request-response lifecycle.

## Phase 2 — First Working HTTP Server

Implement a basic TCP listener that accepts connections, reads a request, and sends a valid HTTP/1.1 response.

**Deliverable:** A browser can request a page from the local server.

## Phase 3 — HTTP Request Parsing

Implement request-line parsing, headers, message framing, request bodies, validation, and size limits.

**Deliverable:** Raw HTTP requests can be converted into structured Python objects with tests for malformed input.

## Phase 4 — Routing and Responses

Implement route registration, request handlers, response objects, status codes, text responses, and JSON serialization.

**Deliverable:** A developer can build a small API using TinyHTTP.

## Phase 5 — Reliability and Concurrency

Explore blocking I/O, multiple connections, timeouts, resource cleanup, error handling, and concurrency models.

**Deliverable:** A more reliable educational HTTP server with documented limitations.

## Phase 6 — Testing, Packaging, and Documentation

Add integration tests, example applications, packaging verification, API documentation, and a final project review.

**Deliverable:** A documented, installable Python package suitable for demonstration and technical discussion.

## Engineering Principles

1. Understand each concept before implementing it.
2. Prefer the Python standard library for HTTP functionality.
3. Write focused, testable components.
4. Treat network input as untrusted.
5. Keep the implementation understandable rather than unnecessarily abstract.
6. Document architectural decisions and limitations.
7. Complete each phase with verification, documentation, and a Git commit.
