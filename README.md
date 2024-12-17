# HBS To do App
## Instructions
### Run the app locally

1. Clone the repository
2. Create a virtual environment using python version from runtime.txt
3. Install requirements using `pip install -r requirements.txt`'
4. Create a postgres database and update the DATABASE_URL in settings.py
5. Set the following environment variables:
    - `DJANGO_SECRET_KEY`
    - `DJANGO_DEBUG`
    - `POSTGRES_USER`
    - `POSTGRES_PASSWORD`
    - `POSTGRES_HOST`
    - `POSTGRES_PORT`
6. Run the migrations using `python manage.py migrate`
7. Run the server using `python manage.py runserver`

### Run React Frontend

Find instructions [here](https://github.com/paolobejarano)

## API Docs

### Get all tasks

`GET /api/tasks`

### Create a task

`POST /api/tasks`

### Get a task

`GET /api/tasks/:id`

### Update a task

`PUT /api/tasks/:id`

### Delete a task

`DELETE /api/tasks/:id`

