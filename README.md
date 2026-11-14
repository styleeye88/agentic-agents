# Agency Agents

Multi-agent collaboration framework — autonomous Agent system based on Claude/GPT

## Features

- **Multi-Agent Orchestration** — Modular agent design with task decomposition and result aggregation
- **Tool Registry** — Unified tool management, agents call external tools dynamically
- **Orchestrator** — OrchestratorRunner coordinates parallel/serial execution across agents
- **Test Coverage** — pytest + ruff linting, CI auto-validates on every push

## Quick Start

`ash
git clone https://github.com/styleeye88/agentic-agents.git
cd agentic-agents
pip install -e ".[dev]"
pytest -v
`

## Project Structure

`
agentic-agents/
├── agents/            # Core agent implementations
│   ├── __init__.py
│   └── base.py        # BaseAgent abstract class
├── tools/             # Tool registry and implementations
│   ├── __init__.py
│   └── registry.py    # ToolRegistry
├── orchestrator/      # Multi-agent scheduler
│   ├── __init__.py
│   └── runner.py      # OrchestratorRunner
├── tests/             # Unit tests
├── .github/workflows/ # GitHub Actions CI
├── pyproject.toml     # Project config
├── requirements.txt   # Dependencies
└── README.md
`

## CI / CD

GitHub Actions runs automatically on every push to main or PR:
- Multi-Python testing (3.10 / 3.11 / 3.12)
- Ruff linting
- pytest test suite

## License

MIT
