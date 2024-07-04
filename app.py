from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'dcfb9de72342526de2b378112e83182d'

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Ed')

    client_ip = request.remote_addr

    ipinfo_response = requests.get(f'http://ipinfo.io/{client_ip}/json')
    ipinfo_data = ipinfo_response.json()
    city = ipinfo_data.get('city', 'Unknown')

    weather_response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')
    weather_data = weather_response.json()
    temperature = weather_data['main']['temp'] if 'main' in weather_data else 'Unknown'

    response = {
        "client_ip": client_ip,
        "location": city,
        "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

