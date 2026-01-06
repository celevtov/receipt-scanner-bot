from aiogram import Router
from .common_commands import router as common_router
from .photo_hendler import router as photo_router
__all__= 'root_router'

root_router = Router(name="root")
root_router.include_routers(common_router,photo_router)