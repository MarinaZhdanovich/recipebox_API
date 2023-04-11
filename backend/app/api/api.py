from fastapi import APIRouter

from .endpoints import ingredient


api_router = APIRouter()

api_router.include_router(
    ingredient.ingredient_router)

# api_router.include_router(
#     order.order_router
# )
#
#
# api_router.include_router(
#     book.book_router, prefix='/books'
# )