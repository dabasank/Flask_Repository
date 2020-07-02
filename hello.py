#!/usr/bin/env python

from flask import Flask 
app = Flask(__name__)
@app.route('/hi')
def hello_world():
	return 'Hello to the World of Docker!'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5050)
