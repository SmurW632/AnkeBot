import requests
import json

async def prompt(promt, FIO, date_b, date_d):
    '''prompt = {
        "modelUri": "gpt://b1g5og37bgh1ghh2s2qc/yandexgpt-lite/latest",
        "completionOptions": {
            "stream": False,
            "temperature": 0.8,
            "maxTokens": "220"
        },
        "messages": [
            {
                "role": "system",
                "text": f"{promt}",
            },
            
        ]
    }


    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVN1J4sCxYR98rj-tVppyp6gXQthbdmYvmgtO7a"
    }

    response =   requests.post(url, headers=headers, json=prompt)
    
    jsoned = json.loads(response.text)
    
    return str(jsoned["result"]['alternatives'][0]["message"]["text"])#.replace(".","\.").replace("-","\-")'''

    prompt = {
        "modelUri": "gpt://b1g5og37bgh1ghh2s2qc/yandexgpt/latest",
        "completionOptions": {
            "stream": False,
            "temperature": 0.8,
            "maxTokens": "30000"
        },
        
        "messages": [


            {
                "role": "system",
                "text": F"Сгенерируй большую, огромную, нереальных размеров эпитафию про {FIO} по заданным данным. Избегай 'Здесь покоится'",
            },
            {
                "role": "system",
                "text": "Не пиши текст который не относится к запросу пользователя",
            },
            {
                "role": "system",
                "text": "Текст для эпитафии НЕ МЕНЕЕ 50 но не более 100",
            },
            {
                "role": "user",
                "text": f""" :
                ФИО:{FIO}
                ДАТА РОЖДЕНИЯ: {date_b}
                ДАТА СМЕРТИ: {date_d}
                Основной текст: {promt}
                """
            },
            
            
        ]
    }


    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVN1J4sCxYR98rj-tVppyp6gXQthbdmYvmgtO7a"
    }
    response =   requests.post(url, headers=headers, json=prompt)
    
    jsoned = json.loads(response.text)
    
    return str(jsoned["result"]['alternatives'][0]["message"]["text"])#.replace(".","\.").replace("-","\-"

