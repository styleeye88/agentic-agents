# Agency Agents

Multi-agent collaboration framework — autonomous Agent system built on LLM APIs.

## Features

- **BaseAgent** — Abstract base with shared context management
- **SearchAgent** — Information retrieval with scored results
- **CoderAgent** — Code generation + code review
- **AnalystAgent** — Statistical analysis (sum / mean)
- **ToolRegistry** — Centralized tool registration and lookup
- **OrchestratorRunner** — Parallel/serial multi-agent execution
- **GitHub Actions CI** — Tests on Python 3.10/3.11/3.12 + ruff linting
- **Codecov coverage** — Tracks test coverage per PR

## Quick Start

```bash
git clone https://github.com/styleeye88/agentic-agents.git
cd agentic-agents
pip install -e ".[dev]"
pytest -v
python examples/example.py
```

## Project Structure

```
agentic-agents/
├── agents/                 # Core agent implementations
│   ├── __init__.py
│   ├── base.py             # BaseAgent abstract class
│   ├── search_agent.py     # Search & retrieval agent
│   ├── coder_agent.py      # Code generation & review
│   └── analyst_agent.py    # Statistical analysis
├── tools/                  # Tool registry
│   ├── __init__.py
│   └── registry.py
├── orchestrator/           # Multi-agent scheduler
│   ├── __init__.py
│   └── runner.py
├── examples/               # Usage examples
│   ├── __init__.py
│   └── example.py
├── tests/                  # Unit tests (7 passing)
├── .github/workflows/      # GitHub Actions (CI + Coverage)
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Running Locally

```bash
# Install
pip install -e ".[dev]"

# Run tests
pytest -v

# Run linter
ruff check .

# Run example
python examples/example.py
```

## License

MIT
