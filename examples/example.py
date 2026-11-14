#!/usr/bin/env python3
"""
Agency Agents - Quick Start Example.
"""
from orchestrator.runner import OrchestratorRunner
from agents.search_agent import SearchAgent
from agents.coder_agent import CoderAgent
from agents.analyst_agent import AnalystAgent


def main() -> None:
    agents = [SearchAgent(), CoderAgent(language="python"), AnalystAgent()]
    runner = OrchestratorRunner(agents)
    task = {
        "query": "Python asyncio best practices",
        "code_task": "Write an async HTTP client",
        "data": [12, 19, 7, 23, 15],
    }
    results = runner.run(task)
    for name, result in results.items():
        print(f"[{name}] {result}")
    print(f"Shared context: {runner.shared_context}")


if __name__ == "__main__":
    main()
