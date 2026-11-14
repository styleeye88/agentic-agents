"""Tests for BaseAgent."""
import pytest
from agents.base import BaseAgent


class DummyAgent(BaseAgent):
    def run(self, input_data: dict) -> dict:
        return {"status": "ok", "input": input_data}


def test_agent_repr():
    agent = DummyAgent("test")
    assert "Agent" in repr(agent)


def test_agent_run():
    agent = DummyAgent("test")
    result = agent.run({"query": "hello"})
    assert result["status"] == "ok"
    assert result["input"]["query"] == "hello"


def test_agent_context():
    agent = DummyAgent("test")
    agent.update_context("key", "value")
    assert agent.get_context("key") == "value"
    assert agent.get_context("missing", "default") == "default"
