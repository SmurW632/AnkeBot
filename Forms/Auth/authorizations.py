import aiohttp
from aiogram.types import Message

# URL для обновления страницы памяти
UPDATE_MEMORY_PAGE_URL = "https://mc.dev.rand.agency/api/page/23647620"
# Токен авторизации для доступа к API
AUTH_TOKEN = "Bearer 190|bwn9iJVmi42enrFNmQOigWDCqWUWBgDHCXsp2QXZ"

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
            