from typing import Any

from repository import ArticleRepository


def create_article(author: str, body: str) -> dict[str, Any]:
    return ArticleRepository.create_article(author, body)
