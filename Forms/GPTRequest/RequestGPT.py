import requests
import json

async def prompt(promt):
    prompt = {
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
    
    return str(jsoned["result"]['alternatives'][0]["message"]["text"]).replace(".","\.").replace("-","\-")
