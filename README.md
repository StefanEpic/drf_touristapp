## 🌄 API TouristApp
![Django REST framework](https://img.shields.io/badge/Django%20REST%20framework-3.14-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14-blue)
![coverage](https://img.shields.io/badge/coverage-97%25-green)

АPI for placing and getting information about mountain passes

## 📨 Usage
A tourist, using a mobile application, can send JSON data of the following form, for example:

```
{
    "title": "Ural",
    "user": {
        "first_name": "Ivan",
        "second_name": "Ivanovich",
        "last_name": "Ivanov",
        "email": "example@mail.com",
        "phone": "+77777777777"
    },
    "coords": {
        "latitude": 45.456,
        "longitude": 65.876,
        "height": 560
    },
    "level": {
        "winter": "",
        "summer": "1А",
        "autumn": "1А",
        "spring": ""
    },
    "images": [
        {"data": "https://...", "title": "Start"},
        {"data": "https://...", "title": "End"}
    ]
}
```
*Note: If the database already contains the user's mail, then the existing user data is used to create the field*

### Method result: JSON

`{"status": 500, "message": "Error connecting to database", "id": None}`

`{"status": 400, "message": "Bad request", "id": None}`

`{"status": 200, "message": "The record was successfully added to the database", "id": 42}`

## 💻 API methods
Returns a list of all mountain passes: `GET /submitdata/`

Email filter: `GET /submitdata/?user__email=<email>`

Add mountain pass: `POST /submitdata/`

Get data for a particular mountain pass: `GET /submitdata/<id>`

Allows changing a mountain pass attribute values: `PATCH /submitdata/<id>`

*Note:* 
- *Сan change all fields except "user". Also for changing, the "status" field should be "NEW"*
- *To change images, you need to pass their "id". If "id" is not passed, a new image will be created. To clear the list of images, send an empty list "[]"*


### Method result: JSON
`{"state": 1, "message": "The record was successfully updated"}`

`{"state": 0, "message": serializer.errors}`

## 📊 Testing
```
Name                                   Stmts   Miss  Cover
----------------------------------------------------------
manage.py                                 12      2    83%
mountains/__init__.py                      0      0   100%
mountains/admin.py                         7      0   100%
mountains/apps.py                          4      0   100%
mountains/migrations/0001_initial.py       6      0   100%
mountains/migrations/__init__.py           0      0   100%
mountains/models.py                       35      0   100%
mountains/serializers.py                  74      0   100%
mountains/tests/__init__.py                0      0   100%
mountains/tests/test_api.py              111      0   100%
mountains/urls.py                          6      0   100%
mountains/views.py                        25      0   100%
touristapp/__init__.py                     0      0   100%
touristapp/asgi.py                         4      4     0%
touristapp/settings.py                    19      0   100%
touristapp/urls.py                         5      0   100%
touristapp/wsgi.py                         4      4     0%
touristapp/yasg.py                         6      0   100%
----------------------------------------------------------
TOTAL                                    318     10    97%
```

API can be tested on pythonanywhere.com:
[https://stefanepic.pythonanywhere.com/swagger/](https://stefanepic.pythonanywhere.com/swagger/)
