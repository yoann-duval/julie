# AI Agent Project

This project implements an AI agent using Clean Architecture and LangGraph.

## Structure

- `src/core`: Domain entities and interfaces (Ports).
- `src/use_cases`: Application business logic.
- `src/adapters`: Implementations of interfaces (Adapters).
    - `api`: FastAPI web server.
    - `llm`: LangGraph integration.
    - `persistence`: Database access.
    - `external`: External API clients.
- `tests`: Unit and integration tests.

## Installation

```bash
pip install -r requirements.txt
```

## Running the app

```bash
uvicorn src.main:app --reload
```
