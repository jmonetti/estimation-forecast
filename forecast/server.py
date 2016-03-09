from forecast.data_access.data_access import DataAccess
import os
import json

import flask


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


@app.route('/projects', methods=['GET'])
def projects():
    return flask.jsonify(
        {
            'projects': DataAccess().get_projects()
        }
    );

if __name__ == "__main__":
    app.run(debug=True)
