***Обязательные поля для заполнения страницы памяти***
```
1. ФИО
2. Дата рождения
3. Дата смерти (не может быть меньше даты рождения)
4. Краткая эпитафия
```
> json
```

 {
    "name": "Иванов Иван Иванович",
    "start": {
        "day": "02",
        "month": "01",
        "year": 1700
    },
    "end": {
        "day": "03",
        "month": "01",
        "year": 2024
    },
    "epitaph": "КРАТКАЯ ЭПИТАФИЯ",
    "author_epitaph": "АВТОР ЭПИТАФИИ",
    "page_type_id": "1"
}
```


***Авторизация***
> Запрос
```
POST https://mc.dev.rand.agency/api/v1/get-access-token
Accept: application/json
Content-Type: application/json;charset=UTF-8

{
  "email": "admin@admin.ru",
  "password": "admin",
  "device": "bot-v0.0.1"
}
```
> Ответ (code: 200)
```
{
  "access_token": "190|bwn9iJVmi42enrFNmQOigWDCqWUWBgDHCXsp2QXZ"
}
```

***Поиск СП для связывания***
> Запрос
```
POST https://mc.dev.rand.agency/api/page/search
Accept: application/json
Content-Type: application/json;charset=UTF-8
Authorization: Bearer 190|bwn9iJVmi42enrFNmQOigWDCqWUWBgDHCXsp2QXZ

{
  "name":"", // Наименование страницы которую хотим привязать
  "slug":"83050987", // Slug страницы которую хотим привязать
  "birthday_at":"", // Рождение страницы которую хотим привязать
  "died_at":"", // Смерть страницы которую хотим привязать
  "slugs":["23647620"], //Slug текущей страницы
  "published_page":1, // Опубликованная страница памяти
  "page":{"isTrusted":true} // Включая удаленные
}
```
> Ответ (code: 200)
> В теле ответа список СП обернутых в пагинацию
> Пример ответа тут /simple/search/response.json

***Отправка предложения на связывание владельцу указанной СП***
> Запрос
```
POST https://mc.dev.rand.agency/api/page/relative
Accept: application/json
Content-Type: application/json;charset=UTF-8
Authorization: Bearer 190|bwn9iJVmi42enrFNmQOigWDCqWUWBgDHCXsp2QXZ

{
    "parentId":148, // Id текущей страницы
    "relation":19673642, // Slug связываемой страницы
    "kinship":5 // Родственная связь
}
```
> Ответ (code: 200)
```
{success: true}
```
> Родственная связь:
> 
| Название | Значение |
|------|----------|
| Мать     | 1        |
|    Отец  | 2        |
|   Дочь   | 3        |
|   Сын   | 4        |
|   Дедушка   | 5        |
|  Бабушка    | 6        |
|    Внук  | 7        |
|    Внучка  | 8        |
|   Брат   | 9        |
|   Сестра   | 10       |
|   Дядя   | 11       |
|   Тетя   | 12       |
|   Племянник   | 13       |
|   Племянница   | 14       |

***Получение индивидуальных СП**
> Запрос
```
GET https://mc.dev.rand.agency/api/cabinet/individual-pages
Accept: application/json
Content-Type: application/json;charset=UTF-8
Authorization: Bearer 1336|fJs9nV5xKbQ3aSssDO7pehgxS5G6vJa6TdBS9eIM
```
> Ответ (code:200)
```
// Тело ответа тут: /doc/simple/individualPages/response.json
```

***Обновление СП***
> Запрос
```
PUT https://mc.dev.rand.agency/api/page/23647620
Accept: application/json
Content-Type: application/json;charset=UTF-8
Authorization: Bearer 190|bwn9iJVmi42enrFNmQOigWDCqWUWBgDHCXsp2QXZ

// Тело запроса тут: /doc/simple/updatePage/request.json
// В данном примере приведено полное заполнение страницы памяти
// Особенность с фотографиями, есть 2 варианта добавления фотографий
// первый прямвм указанеим в теле (base64) и предварительной загрузкой api/media/upload
```
> Ответ (code: 200)
```
// Тело ответа тут: /doc/simple/updatePage/response.json
```

***Загрузка фотографии на ресурс***
> Запрос
```
POST https://mc.dev.rand.agency/api/media/upload
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: ru,en;q=0.9
Connection: keep-alive
Content-Type: multipart/form-data;

file: (binary)
```
> Ответ
```
{
    "id": 66,
    "url": "https:\/\/src.mc.dev.rand.agency\/storage\/test\/66\/1712092161.jpg",
    "name": "media-librarys0UDAC"
}
```

***Добавление комментария к СП***
> Запрос
```
POST https://mc.dev.rand.agency/api/comment
Accept: application/json
Content-Type: application/json;charset=UTF-8

// Тело запроса тут: /doc/simple/addComment/request.json
```
> Ответ (code: 200)
```
// Тело ответа тут: /doc/simple/addComment/response.json
```