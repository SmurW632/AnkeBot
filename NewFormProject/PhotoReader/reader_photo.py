from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from PIL import Image
from io import BytesIO
import pytesseract
from pathlib import Path
import aiofiles
import requests
import json
from aiogram.enums import ParseMode
from Classes.BotClasses import StepsBots

# Configuration for tesseract command
TESSERACT_CMD = r'D:\projecs programms\python\tesseract\tesseract.exe'
TEXT_DIR = Path('AnkeBot/NewFormProject/reading_photo/text_from_photo')

router_reader_photo = Router()

#@router.message(F.photo)
@router_reader_photo.message(StepsBots.READER_PHOTO)
async def handle_photo(message: Message):
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD
    photo = message.photo[-1]
    bot = message.bot
    user_id = message.from_user.id

    file_info = await bot.get_file(photo.file_id)
    photo_data = await bot.download_file(file_info.file_path)
    with Image.open(BytesIO(photo_data.read())).convert("RGB") as image:
        image = image.convert('L').point(lambda x: 0 if x < 128 else 255)
        text = pytesseract.image_to_string(image, lang='rus+eng')

    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    file_path = f'{TEXT_DIR}/text_from_{user_id}.txt'
    async with aiofiles.open(file_path, 'w', encoding='utf-8') as file:
        await file.write(text)

    prompt = {
        "modelUri": "gpt://b1g5og37bgh1ghh2s2qc/yandexgpt/latest",
        "completionOptions": {
        "stream": False,
        "temperature": 1,
        "maxTokens": "3000"
        },
        "messages": [
            {
                    "role": "system",
                    "text": f'Ты занимаешься созданием страницы памяти для умерших людей и ты опытный копирайтер. Исправь явные ошибки в тексте,замени непонятные слова на известные тебе, проверь текст на орфографические,синтаксические ошибки. Найди в тексте ФИО, Дата Рождения, Дата Смерти, Место рождения и Смерти. Оформи красиво. В первой строчке напиши ОБЯЗАТЕЛЬНО ТОЛЬКО ФИО и ничего больше. Во второй строчке ТОЛЬКО Дата рождения и место рождения. В третьей строчке ТОЛЬКО Дата смерти и место смерти. В четвертой строчке ОБЯЗАТЕЛЬНО ТОЛЬКО краткую биографию. В пятой строчке ОБЯЗАТЕЛЬНО напиши ТОЛЬКО краткую и красивую эпитафию. Вот текст: {text}'
            },
            
        ]
        }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVN1J4sCxYR98rj-tVppyp6gXQthbdmYvmgtO7a"
        }
    def escape_markdown_v2(text):
        escape_chars = '_*[]()~`>#+-=|{}.!'
        return ''.join('\\' + char if char in escape_chars else char for char in text)
    
    response = requests.post(url, headers=headers, json=prompt)
    jsoned = json.loads(response.text)
    escaped_text = escape_markdown_v2(jsoned["result"]['alternatives'][0]["message"]["text"])
    await message.answer(escaped_text, parse_mode=ParseMode.MARKDOWN_V2)
