import aiohttp
from aiogram.types import Message

# URL для обновления страницы памяти
UPDATE_MEMORY_PAGE_URL = "https://mc.dev.rand.agency/api/page/23647620"
# Токен авторизации для доступа к API
AUTH_TOKEN = "190|bwn9iJVmi42enrFNmQOigWDCqWUWBgDHCXsp2QXZ"

    # Функция для обновления страницы памяти
async def update_memory_page(message: Message):
    async with aiohttp.ClientSession() as session:
        # Загрузка данных запроса из файла request.json
        with open("/doc/simple/updatePage/request.json", "r") as file:
            data = file.read()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": AUTH_TOKEN
        }
        async with session.put(UPDATE_MEMORY_PAGE_URL, data=data, headers=headers) as response:
            if response.status == 200:
                await message.answer("Страница памяти успешно обновлена!")
            else:
                await message.answer(f"Произошла ошибка при обновлении страницы памяти. Статус: {response.status}")
                
    # Запрос на получение access token (авторизация)
async def get_access_token(email, password, device):
    url = 'https://mc.dev.rand.agency/api/v1/get-access-token'
    data = {
        "email": email,
        "password": password,
        "device": device
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            if response.status == 200:
                json_response = await response.json()
                access_token = json_response.get('access_token')
                return access_token
            else:
                return None

    # Поиск СП для связывания
async def search_sp():
    url = "https://mc.dev.rand.agency/api/page/search"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "Bearer 190|bwn9iJVmi42enrFNmQOigWDCqWUWBgDHCXsp2QXZ"
    }
    data = {
        "name": "",
        "slug": "83050987",
        "birthday_at": "",
        "died_at": "",
        "slugs": ["23647620"],
        "published_page": 1,
        "page": {"isTrusted": True}
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, headers=headers) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                return None
            
    # Отправка предложения на связывание владельцу указанной СП
async def bind_relative():
    url = "https://mc.dev.rand.agency/api/page/relative"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "Bearer 190|bwn9iJVmi42enrFNmQOigWDCqWUWBgDHCXsp2QXZ"
    }
    data = {
        "parentId": 148,
        "relation": 19673642,
        "kinship": 5
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, headers=headers) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                return None


    # Получение индивидуальных СП
async def get_individual_pages():
    url = "https://mc.dev.rand.agency/api/cabinet/individual-pages"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "Bearer 1336|fJs9nV5xKbQ3aSssDO7pehgxS5G6vJa6TdBS9eIM"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                return None

    # Загрузка фотографии на ресурс
async def upload_photo(file_path):
    url = "https://mc.dev.rand.agency/api/media/upload"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "ru,en;q=0.9",
        "Connection": "keep-alive"
    }
    data = aiohttp.FormData()
    data.add_field('file', open(file_path, 'rb'))

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                return None

    # Добавление комментария к СП
async def add_comment(comment_data):
    url = "https://mc.dev.rand.agency/api/comment"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=comment_data) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                return None