from flask import Flask
from celery import Celery


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret!'

celery = Celery(app.name)
celery.config_from_object('celeryconfig')


@celery.task
def add(x, y):
    return x + y


@celery.task
def remove(x, y):
    return y - x

if __name__ == '__main__':
    app.run(debug=True)
