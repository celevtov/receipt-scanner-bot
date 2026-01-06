from openai import AsyncOpenAI
from config import config as cfg
from typing import Any, Dict, List
from .promt import TEXT

ClientOpenAi = AsyncOpenAI(api_key = cfg.OPENAI_API_KEY)


async def generate_json(user_data: dict[str, Any]) -> dict[str, Any]:
    content_obj: List[Dict[str, Any]] = [{"type": "input_text","text":TEXT}]

    if 'caption' in user_data:
        content_obj.append(user_data['caption'])
    content_obj.extend(user_data['list_files'])

    resp = await ClientOpenAi.responses.create(
        model = cfg.OPENAI_MODEL,
        input = [{
            "role":"user"
            ,"content":content_obj
        }]
    )
    return resp.output_text
