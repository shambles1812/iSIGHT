from flask import Flask, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo
from datetime import datetime
import requests
import random
import string
import json
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'supersecretkey'

app.config['MONGO_URI'] = 'mongodb://localhost:27017/school_updates'
mongo = PyMongo(app)

API_KEY = 'your_weatherapi_key'
CITY = 'Makati'
COUNTRY = 'Philippines'
WEATHER_URL = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY},{COUNTRY}&aqi=no'

def generate_passcode(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def fetch_weather_data():
    response = requests.get(WEATHER_URL)
    data = response.json()
    weather_data = {
        'condition': data['current']['condition']['text'],
        'temperature': data['current']['temp_c'],
        'humidity': data['current']['humidity']
    }
    return weather_data

@app.route('/bulletin-board')
def index():
    today = datetime.now().strftime('%Y-%m-%d')
    updates = mongo.db.updates.find_one({'date': today})
    weather_data = fetch_weather_data()
    return render_template('index.html', date=today, updates=updates, weather_data=weather_data)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'admin' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        today = datetime.now().strftime('%Y-%m-%d')
        classes = request.form.get('classes')
        offices = request.form.get('offices')
        update_data = {
            'date': today,
            'classes': classes,
            'offices': offices
        }
        mongo.db.updates.update_one({'date': today}, {'$set': update_data}, upsert=True)
        return redirect(url_for('index'))

    return render_template('admin.html')

@app.route('/generate_passcode', methods=['GET', 'POST'])
def generate_passcode_page():
    if request.method == 'POST':
        passcode = generate_passcode()
        mongo.db.passcodes.insert_one({'code': passcode})
    
    passcodes = list(mongo.db.passcodes.find())
    return render_template('generate_passcode.html', passcodes=passcodes)

@app.route('/delete_passcode/<passcode_id>', methods=['POST'])
def delete_passcode(passcode_id):
    mongo.db.passcodes.delete_one({'_id': ObjectId(passcode_id)})
    return redirect(url_for('generate_passcode_page'))

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        passcode = request.form.get('passcode')
        stored_passcode = mongo.db.passcodes.find_one({'code': passcode})
        if stored_passcode:
            session['admin'] = True
            mongo.db.passcodes.delete_one({'code': passcode})
            return redirect(url_for('admin'))
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
