import os
import json

import flask
app = flask.Flask(__name__)

CURRENT_DIRECTORY = os.path.dirname(__file__)
with open(os.path.join(CURRENT_DIRECTORY, 'version.json')) as f:
    version_info = json.load(f)


@app.route("/")
def index():
    print "Test"
    return flask.jsonify(
        {
            'name': 'forecast-service',
            'links': {
                'version': '/version'
            }
        }
    )


@app.route('/version')
def version():
    return flask.jsonify(version_info)

if __name__ == "__main__":
    app.run()
