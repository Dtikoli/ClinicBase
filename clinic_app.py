#!/usr/bin/python3
""" Flask Application """

from dashboards import create_app
from models import storage

app = create_app()


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
