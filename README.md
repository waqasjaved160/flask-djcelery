# flask-djcelery
An example project for configuring Djcelery with Flask application and dynamically adding tasks
 - REST API
 - Django admin


Quick Setup
-----------

#### Django Admin

1. Clone this repository.
2. Create a virtualenv and install the requirements.
3. Create database using command: `PYTHONPATH=. django-admin.py migrate --settings=celeryconfig`
4. Start the django server using command: `PYTHONPATH=. django-admin.py runserver --settings=celeryconfig`
5. Open second terminal window and start local Redis server using command: `./run-redis.sh`.
6. Start celery worker in another terminal window: `env/bin/celery worker -A app.celery --loglevel=INFO`.
6. Start celery beat in another terminal window: `PYTHONPATH=. django-admin.py celerybeat --settings=celeryconfig`.
7. Django Admin can be checked by visiting `http://localhost:8000/` and celery tasks can be added/removed
8. Flask application can be started as: `python app.py`


#### REST API

1. Follow all the above steps
2. `GET /interval_schedules/` will list all the schedule intervals
3. `POST /interval_schedules/` will add a schedule interval
    
    ##### POST Data (Example)
    - every: 90
    - period: seconds
4. `GET /periodic_tasks/` will list all the periodic tasks
5. `POST /periodic_tasks/` will add a new task 
    
    ##### POST Data (Example)
    - name: 'API Task'
    - task: 'app.add'
    - enabled: True
    - args: '[5,5]'
    - interval: 1 (would need to be created first using API)
6. Similarly `PUT /interval_schedules/1/` will change the interval for tasks on the run
    - every: 100
    - period: seconds
