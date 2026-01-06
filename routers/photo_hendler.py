from aiogram import Router, F, types
from aiogram_media_group import media_group_handler
from typing import List
from services.files_service import generate_data_for_request


router = Router(name = __name__)
media_group= {}

@router.message(F.media_group_id)
@media_group_handler
async def album_handler(messages: List[types.Message]):
    result = await generate_data_for_request(messages)
    print(result)

@router.message(F.photo|F.document)
async def photo_handler(messages: types.Message):
    result = await generate_data_for_request([messages])
    print(result)





