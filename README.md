# LP24 Test Project

## Ресурс users [CRUD]

Создать словарь

```python
user_storage = {
    "e7b3d405ac9a45758109f3daee0adfae": {"uid": "e7b3d405ac9a45758109f3daee0adfae", "username": "vppuzakov"},
    "3074db5ea6064b75b5c8e13d0415a4e3": {"uid": "3074db5ea6064b75b5c8e13d0415a4e3", "username": "ivanov"},
}
```

а возвращать список.

Получить всех пользователей:

```http
GET http://localhost:8000/api/users/
200 OK
[
    {
        "uid": e7b3d405ac9a45758109f3daee0adfae, 
        "username": "vppuzakov",
    },
    {
        "uid": 3074db5ea6064b75b5c8e13d0415a4e3, 
        "username": "ivanov",
    },
]
```

flask:

```python
from flask import Flask, jsonify, request

app = Flask()  # ...

@app.get('/api/users/')
def get_users():
    ...
    return jsonify([{...}, {...}])

    # 200 OK []
```

Получить ид. пользователя:

```http
GET http://localhost:8000/api/users/e7b3d405ac9a45758109f3daee0adfae
Content-Type: application/json
200 OK
{
    "uid": e7b3d405ac9a45758109f3daee0adfae, 
    "username": "vppuzakov",
}
```

А что если пользователя нет:

```http
GET http://localhost:8000/api/users/32498234324
404 NOT FOUND
```

```python
@app.get('/api/users/<uid>')
def get_by_id(uid):
    ...
    if uid not in users:
        return {'message': 'user not found'}, 404

    return {...}  # 200 OK {}
```

Создать пользователя:

```python
from flask import request
from uuid import uuid4

@app.post('/api/users/')
def add_user():
    user = request.json
    # TODO: validate user body, if not return 404

    user['uid'] = uuid4().hex
    user_storage[user['uid']] = user
    return user, 201
```

```http
POST http://localhost:8000/api/users/
{
    "username": "sidorov",
}

{
    "uid: "d2713b3ae1a14276b69249426af8f1ec",
    "username": "sidorov",
}
```

```python
from http import HTTPStatus

@app.put('/api/users/<uid>')
def update_user(uid):
    if uid not in user_storage:
        return {"message": "user not found"}, HTTPStatus.NOT_FOUND

    user = request.json
    # TODO: validation skipped

    user_storage[uid] = user
    return user, HTTPStatus.OK
```

```http
PUT http://localhost:8000/api/users/d2713b3ae1a14276b69249426af8f1ec
{
    "uid": "d2713b3ae1a14276b69249426af8f1ec",
    "username": "michailov"
}
```

```python
@app.delete('/api/users/<uid>')
def delete_user(uid):
    if uid not in user_storage:
        return {"message": "user not found"}, 404

    user_storage.pop(uid)
    return {}, 204
```

```http
DELETE http://localhost:8000/api/users/d2713b3ae1a14276b69249426af8f1ec
204 NO CONTENT
```

If not found:

```http
DELETE http://localhost:8000/api/users/d2713b3ae1a14276b69249426af8f1ec
404 NOT FOUND
```

HTTP Methods:

- GET (получить)
- POST (сделать, создать)
- DELETE (удалить)
- PUT (заменить)
- PATCH (обновить)

HTTP status codes:

```text
2xx - OK
200 - OK
201 - resource created
204 - no content

3xx - redirect

4xx - client errors
400 - BAD REQUEST
401 - UNAUTHORIZED
403 - PROHIBITED (ACCESS DENIED)
404 - NOT FOUND
405 - METHOD NOT ALLOWED
409 - CONFLICT

5xx - server errors
500 - INTERNAL SERVER ERROR
502, 503, 504 - timeouts, bad gateway
```

`.vscode/launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "backend",
            "type": "python",
            "request": "launch",
            "module": "backend",
            "console": "internalConsole",
        }
    ]
}
```
