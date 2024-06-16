from flask import Flask, jsonify
from flask_cors import CORS
from common.util import run_all_scrapers

app = Flask(__name__)
CORS(app)


@app.route('/scrape_all', methods=['GET'])
def scrape_all():
    jobs = run_all_scrapers()
    jobs_data = [job.to_dict() for job in jobs]

    response = jsonify({'jobs': jobs_data})
    response.headers['Content-Type'] = 'application/json; charset=utf-8'

    return response


if __name__ == '__main__':
    app.run()
