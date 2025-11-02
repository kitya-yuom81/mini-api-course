from typing import List, Tuple, TypeVar

T = TypeVar("T")

def paginate(items: List[T], page: int | None, limit: int | None) -> Tuple[List[T], int]:
    if page is None or page < 1:
        page = 1
    if limit is None or limit < 1 or limit > 100:
        limit = 10
    start = (page - 1) * limit
    end = start + limit
    total = len(items)
    return items[start:end], total
