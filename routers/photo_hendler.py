from aiogram import Router, F, types
from aiogram_media_group import media_group_handler
from typing import List
from services.files_service import generate_data_for_request
from services.llm_service import generate_json


router = Router(name = __name__)

@router.message(F.media_group_id)
@media_group_handler
async def album_handler(messages: List[types.Message]):
    user_data = await generate_data_for_request(messages)
    response_from_openai = await generate_json(user_data)
    print(response_from_openai)

@router.message(F.photo|F.document)
async def photo_handler(messages: types.Message):
    user_data = await generate_data_for_request([messages])
    response_from_openai = await generate_json(user_data)
    print(response_from_openai)





