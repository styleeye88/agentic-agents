"""调度器 —— 编排多 Agent 协同执行任务。"""
from typing import Any, Dict, List

from agents.base import BaseAgent


class OrchestratorRunner:
    def __init__(self, agents: List[BaseAgent]):
        self.agents = agents
        self.shared_context: Dict[str, Any] = {}

    def update_shared(self, key: str, value: Any) -> None:
        self.shared_context[key] = value

    def run(self, task: dict) -> Dict[str, Any]:
        results = {}
        for agent in self.agents:
            result = agent.run(task)
            results[agent.name] = result
            if isinstance(result, dict):
                self.shared_context.update(result)
        return results
