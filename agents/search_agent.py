"""搜索 Agent — 负责信息检索与知识库查询。"""
from typing import Any, Dict, List

from .base import BaseAgent


class SearchAgent(BaseAgent):
    def __init__(self, api_key: str = '') -> None:
        super().__init__('search_agent')
        self.api_key = api_key

    def run(self, input_data: dict) -> Dict[str, Any]:
        query: str = input_data.get('query', '')
        max_results: int = input_data.get('max_results', 5)
        results: List[Dict[str, str]] = []
        for i in range(min(max_results, 3)):
            results.append({'title': f'result_{i+1}_for_{query}', 'score': round(0.9 - i * 0.15, 2)})
        self.update_context('last_query', query)
        return {'status': 'ok', 'results': results, 'count': len(results)}
