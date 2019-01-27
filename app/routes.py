from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
@app.route('/index_test')
def index():
	return render_template('index_test.html')

@app.route('/TruckTest')
def TruckTest():
	return render_template('TruckTest.html')