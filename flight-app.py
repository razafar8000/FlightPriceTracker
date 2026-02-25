from flask import Flask, render_template, request, jsonify
from database import get_flights_by_budget

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    budget = float(data.get('budget', 0))
    results = get_flights_by_budget(budget)
    return jsonify({'flights': results, 'count': len(results)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)