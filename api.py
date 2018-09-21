from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='*')
api = Api(app)

ENVELOPES = []

class Envelope(Resource):
    def get(self, envelope_name):
        return [x for x in ENVELOPES if x["name"] == envelope_name][0]

    def put(self, envelope_name):
        ENVELOPES.append({
            'name': envelope_name,
            'amount': request.get_json()['amount']
        })
        return ENVELOPES[-1]

class EnvelopeList(Resource):
    def get(self):
        return ENVELOPES

api.add_resource(EnvelopeList, '/envelopes')
api.add_resource(Envelope, '/<string:envelope_name>')

if __name__ == '__main__':
    app.run(debug=True)
