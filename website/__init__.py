from flask import Flask, render_template, request
from get_geocode import get_geocode

app = Flask(__name__)

@app.route('/')
def index():
    address = request.args.get('address')
    address = address if address else ''
    geocode = get_geocode(address) if address else {}
    return render_template('index.html', address=address, geocode=geocode)