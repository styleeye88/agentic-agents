"""分析 Agent — 负责数据分析与报告生成。"""
from typing import Any, Dict, List

from .base import BaseAgent


class AnalystAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__('analyst_agent')

    def run(self, input_data: dict) -> Dict[str, Any]:
        data: list = input_data.get('data', [])
        metric: str = input_data.get('metric', 'sum')
        result: float = sum(data) if metric == 'sum' else (sum(data) / len(data) if data else 0)
        self.update_context('last_metric', metric)
        return {'status': 'ok', 'result': result, 'samples': len(data)}
