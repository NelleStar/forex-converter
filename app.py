from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.secret_key = '_secret_key_'

@app.route('/', methods=['GET'])
def index():
    return render_template('base.html')


@app.route('/', methods=['POST'])
def convert():
    base_currency = request.form['base_currency']
    target_currency = request.form['target_currency']
    amount = float(request.form['amount'])

    symbols = request.form.get('target_currency')  
    places = float(request.form.get('places', 2))

    # Prepare the API URL with the above parameters
    api_url = f'https://api.exchangerate.host/convert?from={base_currency}&to={target_currency}&amount={amount}'

    # Add 'symbols' and 'places' parameters
    if symbols:
        api_url += f'&symbols={symbols}'
    if places:
        api_url += f'&places={places}'

    try:
        # HTTP GET request
        response = requests.get(api_url)
        response_data = response.json()
        print (response_data)

        # success/error
        if response_data['result']:
            converted_amount = response_data['result']
        else:
            converted_amount = None  
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        converted_amount = None  # Handle the case when there's an error with the API call

    return render_template('result.html', result=converted_amount)
