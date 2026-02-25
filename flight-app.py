"""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Manual flight data - 10 entries
FLIGHTS = [
    {
        "id": 1,
        "airline": "Delta Airlines",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Delta_logo.svg/200px-Delta_logo.svg.png",
        "origin": "New York (JFK)",
        "destination": "Los Angeles (LAX)",
        "departure": "06:00 AM",
        "arrival": "09:30 AM",
        "duration": "5h 30m",
        "price": 189,
        "class": "Economy"
    },
    {
        "id": 2,
        "airline": "American Airlines",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/American_Airlines_logo_2013.svg/200px-American_Airlines_logo_2013.svg.png",
        "origin": "Chicago (ORD)",
        "destination": "Miami (MIA)",
        "departure": "08:15 AM",
        "arrival": "12:45 PM",
        "duration": "2h 30m",
        "price": 134,
        "class": "Economy"
    },
    {
        "id": 3,
        "airline": "United Airlines",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/United_Airlines_Logo.svg/200px-United_Airlines_Logo.svg.png",
        "origin": "San Francisco (SFO)",
        "destination": "Seattle (SEA)",
        "departure": "07:00 AM",
        "arrival": "09:10 AM",
        "duration": "2h 10m",
        "price": 98,
        "class": "Economy"
    },
    {
        "id": 4,
        "airline": "Southwest Airlines",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Southwest_Airlines_logo_2014.svg/200px-Southwest_Airlines_logo_2014.svg.png",
        "origin": "Dallas (DAL)",
        "destination": "Denver (DEN)",
        "departure": "10:30 AM",
        "arrival": "12:00 PM",
        "duration": "1h 30m",
        "price": 79,
        "class": "Economy"
    },
    {
        "id": 5,
        "airline": "JetBlue",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/JetBlue_Airways_logo.svg/200px-JetBlue_Airways_logo.svg.png",
        "origin": "Boston (BOS)",
        "destination": "Orlando (MCO)",
        "departure": "11:00 AM",
        "arrival": "2:30 PM",
        "duration": "3h 30m",
        "price": 115,
        "class": "Economy"
    },
    {
        "id": 6,
        "airline": "Delta Airlines",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Delta_logo.svg/200px-Delta_logo.svg.png",
        "origin": "Atlanta (ATL)",
        "destination": "New York (JFK)",
        "departure": "2:00 PM",
        "arrival": "5:30 PM",
        "duration": "2h 10m",
        "price": 210,
        "class": "Business"
    },
    {
        "id": 7,
        "airline": "Spirit Airlines",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Spirit_Airlines_logo.svg/200px-Spirit_Airlines_logo.svg.png",
        "origin": "Las Vegas (LAS)",
        "destination": "Phoenix (PHX)",
        "departure": "3:45 PM",
        "arrival": "4:55 PM",
        "duration": "1h 10m",
        "price": 49,
        "class": "Economy"
    },
    {
        "id": 8,
        "airline": "American Airlines",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/American_Airlines_logo_2013.svg/200px-American_Airlines_logo_2013.svg.png",
        "origin": "New York (JFK)",
        "destination": "London (LHR)",
        "departure": "9:00 PM",
        "arrival": "9:00 AM+1",
        "duration": "7h 00m",
        "price": 549,
        "class": "Economy"
    },
    {
        "id": 9,
        "airline": "United Airlines",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/United_Airlines_Logo.svg/200px-United_Airlines_Logo.svg.png",
        "origin": "Houston (IAH)",
        "destination": "Cancun (CUN)",
        "departure": "7:30 AM",
        "arrival": "10:00 AM",
        "duration": "2h 30m",
        "price": 167,
        "class": "Economy"
    },
    {
        "id": 10,
        "airline": "Alaska Airlines",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Alaska_Airlines_logo.svg/200px-Alaska_Airlines_logo.svg.png",
        "origin": "Portland (PDX)",
        "destination": "Honolulu (HNL)",
        "departure": "8:00 AM",
        "arrival": "12:30 PM",
        "duration": "5h 30m",
        "price": 289,
        "class": "Economy"
    }
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    budget = float(data.get('budget', 0))
    results = [f for f in FLIGHTS if f['price'] <= budget]
    results = sorted(results, key=lambda x: x['price'])
    return jsonify({'flights': results, 'count': len(results)})


if __name__ == '__main__':
    app.run(debug=True)
"""

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
    app.run(debug=True)