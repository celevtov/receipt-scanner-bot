from aiogram.types import Message
import base64
from typing import List


# function for download
async def extract_file_bite(message: Message,file_id:str)-> bytes:
    file = await message.bot.get_file(file_id)
    stream = await message.bot.download_file(file.file_path)
    return stream.read()




# Function for converting

async def to_data_url(img_bytes: bytes, mime: str = "image/jpeg") -> str:
    b64 = base64.b64encode(img_bytes).decode("ascii")
    return f"data:{mime};base64,{b64}"


# function for prepare data for OpenAI

async def generate_data_for_request(messages:List[Message]):
    user_data = {'list_files':[]}
    row_dict ={'type':'input_image','image_url':''}
    for message in messages:
        if message.photo:
            file_id = message.photo[-1].file_id
        elif message.document:
            file_id = message.document.file_id
        else:
            raise ValueError("Unsupported message type")

        file_bytes = await extract_file_bite(message,file_id)
        row_dict['image_url'] = await to_data_url(file_bytes)
        user_data['list_files'].append(row_dict)

    if messages[-1].caption:
        user_text = messages[-1].caption
        user_data['caption']={"type": "input_text",'text': user_text}

    return user_data
