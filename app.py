from flask import Flask, request, render_template
import json
import json2html
from json2html import *
import pandas as pd
import Pipeline as pp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	status = 'success'
	if request.method == 'POST':
		details = request.form
		if details['form_type'] == 'search_tweets':
			key_words = request.form.values()
			sentence = pd.Series(key_words)
			predicted = pp.pipeline(sentence[0])
			data = json.dumps(predicted)
			data2 = json2html.convert(json = data)
			return data2
	return render_template('index.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)