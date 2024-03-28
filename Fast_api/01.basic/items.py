from fastapi import APIRouter  # DRF, DRF-Spectacular ... -> X

router = APIRouter()


@router.get(
    "/api/v1/items/{item_id}",
    status_code=200,
    tags=["item", "payment"],
    summary="Bring a certificate item",
    description="Item model에서 item_id 값을 가지고 특정 아이템 조회",
)
def get_item(item_id: int):
    return {"items": item_id}


# router 생성하고 main.py에서 등록.
