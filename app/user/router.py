from fastapi import APIRouter

router = APIRouter(
    prefix="/user/manage"
)


@router.get("/buy/{offer_id}")
async def buy_product(offer_id: int):
    # TODO
    return


@router.get("/sell/{offer_id}")
async def sell_product(offer_id: int):
    # TODO
    return
