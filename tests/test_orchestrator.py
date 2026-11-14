"""Tests for OrchestratorRunner."""
from orchestrator.runner import OrchestratorRunner
from agents.base import BaseAgent


class EchoAgent(BaseAgent):
    def run(self, input_data: dict) -> dict:
        return {"agent": self.name, "echo": input_data.get("task")}


def test_runner_runs_agents():
    runner = OrchestratorRunner([EchoAgent("agent_a"), EchoAgent("agent_b")])
    results = runner.run({"task": "hello"})
    assert "agent_a" in results
    assert "agent_b" in results
    assert results["agent_a"]["echo"] == "hello"


def test_runner_shares_context():
    runner = OrchestratorRunner([EchoAgent("agent_a")])
    runner.update_shared("shared_key", "shared_value")
    runner.run({"task": "data"})
    assert runner.shared_context["shared_key"] == "shared_value"
