# Flask Api

Tech Used:

(Flask) [https://flask.palletsprojects.com/en/1.1.x/]

## Available Endpoints

### To get all users

`/GET /users`

### To get a specific user

`/GET /users/:user_id`

### To insert a user

`/POST /users`

### To delete a user

`/DELETE /users/:user_id`

### To update a user

`/PATCH /users/:user_id`

## Directory layout

```
.
├── project/                   <-- Application components and source code
│     ├── users/               <-- Api Folders
│     │    ├── __init__.py     <-- Init Python
│     │    ├── controller.py   <-- Users Controller
│     │    ├── routes.py       <-- Users Routes
│     ├── app.py               <-- Flask app to run
│     ├── settings.py          <-- Flask configuration variables
├── app.py                     <-- Run this file to load the app
├── requirements.txt           <-- Requirements to run the app
├── README.md
```
