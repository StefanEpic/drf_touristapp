## 🌄 API TouristApp
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
        {"data"="https://...", "title"="Start"},
        {"data"="https://...", "title"="End"}
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


API can be tested on pythonanywhere.com:
[https://stefanepic.pythonanywhere.com/swagger/](https://stefanepic.pythonanywhere.com/swagger/)
