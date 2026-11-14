"""基础 Agent 类——所有子 Agent 的基类。"""
from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseAgent(ABC):
    def __init__(self, name: str, system_prompt: str = ''):
        self.name = name
        self.system_prompt = system_prompt
        self.context: Dict[str, Any] = {}

    @abstractmethod
    def run(self, input_data: dict) -> dict:
        raise NotImplementedError

    def update_context(self, key: str, value: Any) -> None:
        self.context[key] = value

    def get_context(self, key: str, default: Any = None) -> Any:
        return self.context.get(key, default)

    def __repr__(self) -> str:
        return f'Agent({self.name})'
