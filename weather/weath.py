from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/weather', methods=['POST'])
def weather():
    api_key = "33f35d575c3e20acbd49a63387832fc5"  # Replace with your OpenWeatherMap API key
    city = request.form['city']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            "city": city,
            "temperature": data['main']['temp'],
            "description": data['weather'][0]['description'],
            "icon": data['weather'][0]['icon']
        }
        return render_template('result.html', weather=weather_data)
    else:
        return jsonify({"error": "City not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
