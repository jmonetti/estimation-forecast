import os
import json
import flask

from forecast.data_access.data_access import DataAccess


app = flask.Flask(__name__)

CURRENT_DIRECTORY = os.path.dirname(__file__)
with open(os.path.join(CURRENT_DIRECTORY, 'version.json')) as f:
    version_info = json.load(f)


@app.route("/")
def index():
    return flask.jsonify(
        {
            'name': 'forecast-service',
            'links': {
                'version': '/version',
                'projects': '/projects'
            }
        }
    )


@app.route('/version', methods=['GET'])
def version():
    return flask.jsonify(version_info)


@app.route('/projects', methods=['GET', 'POST', 'PUT'])
def projects():

    if flask.request.method == 'POST':
        DataAccess().add_project(json.loads(flask.request.form.keys()[0]))
        return flask.jsonify(**DataAccess().get_projects()[0]), 201
    elif flask.request.method == 'PUT':
        updated_project = DataAccess().update_project(json.loads(flask.request.form.keys()[0]))
        return flask.jsonify(updated_project)

    return flask.jsonify(
        {
            'projects': DataAccess().get_projects()
        }
    ), 200

if __name__ == "__main__":
    # Listening to all public IPs
    app.run(host="0.0.0.0", debug=True)
