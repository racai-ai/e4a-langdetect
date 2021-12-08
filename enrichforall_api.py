from http import HTTPStatus
from flask import Flask, request
from flask_restful import Api, Resource
from enrichforall import E4ALangDetect

class E4ARestApi(Resource):
    """REST API for the Enrich4All language detection service."""
    
    def get(self):
        """Handles GET requests with `text` field filled in with the text
        whose language is to be identified."""

        if 'text' in request.args:
            text = request.args['text']
            detected_language = E4ALangDetect(text).lang_id()
            return ({'language': detected_language}, HTTPStatus.OK)
        else:
            return ({'error': 'No /langid?text=... field has been supplied.'}, int(HTTPStatus.BAD_REQUEST))


app = Flask(__name__)
app.config['RESTFUL_JSON'] = {
    'default': lambda x: x.__dict__,
    'ensure_ascii': False,
    'sort_keys': True,
    'indent': 2
}
api = Api(app)
api.add_resource(E4ARestApi, '/langid')
# Debug
# app.run(host='0.0.0.0', port=5000)
