"""工具注册表 —— 集中管理可用工具集。"""
from typing import Callable, Dict, Optional


class ToolRegistry:
    def __init__(self):
        self._tools: Dict[str, Callable] = {}

    def register(self, name: str, func: Callable) -> None:
        self._tools[name] = func

    def get(self, name: str) -> Optional[Callable]:
        return self._tools.get(name)

    def list_tools(self) -> list:
        return list(self._tools.keys())
