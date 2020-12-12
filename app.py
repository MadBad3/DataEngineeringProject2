from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	status = 'success'
	if request.method == 'POST':
		details = request.form
		if details['form_type'] == 'search_tweets':
			return status
	return render_template('index.html')



if __name__ == '__main__':
	app.run(host='0.0.0.0')
