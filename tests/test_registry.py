"""Tests for ToolRegistry."""
from tools.registry import ToolRegistry


def test_register_and_get():
    registry = ToolRegistry()
    registry.register("echo", lambda x: x)
    assert registry.get("echo") is not None
    assert registry.get("missing") is None


def test_list_tools():
    registry = ToolRegistry()
    registry.register("tool_a", lambda: None)
    registry.register("tool_b", lambda: None)
    assert sorted(registry.list_tools()) == ["tool_a", "tool_b"]
