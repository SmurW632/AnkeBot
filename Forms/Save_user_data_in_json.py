import json

async def save_user_data(user_data):
    file_name = "JSON/users.json"

    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(user_data, file, ensure_ascii=False, indent=4)
        
    print(f"данные сохранены в файл!")  