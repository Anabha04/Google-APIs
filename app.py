from flask import Flask, render_template, jsonify, request
import http.client
import json
from urllib.parse import urlencode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/recipes', methods=['GET'])
def get_recipes():
    search_query = request.args.get('query', '')
    
    # Set up the HTTP connection
    conn = http.client.HTTPSConnection("tasty.p.rapidapi.com")
    
    # Prepare the request parameters
    querystring = {"from": "0", "size": "20", "q": search_query}
    headers = {
        "x-rapidapi-key": "340b1bd18cmsh25e8126896fe0b0p10e044jsn3ad1269e6dbf",  # Replace with your API key
        "x-rapidapi-host": "tasty.p.rapidapi.com"
    }
    
    # Format the query string
    query = urlencode(querystring)
    
    # Send the GET request
    conn.request("GET", f"/recipes/list?{query}", headers=headers)
    
    # Get the response
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    
    # Close the connection
    conn.close()
    
    # Parse the JSON response
    recipes = json.loads(data)
    
    return jsonify(recipes)

if __name__ == '__main__':
    app.run(debug=True)
