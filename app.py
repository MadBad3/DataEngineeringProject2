from flask import Flask, request, render_template
import json
import json2html
from json2html import *
import pandas as pd
import Pipeline as pp
import time
#from multiprocessing.pool import ThreadPool

from prometheus_client import start_http_server
from prometheus_client import Counter
from prometheus_client import Gauge
from prometheus_client import Summary

REQUESTS = Counter('flask_app_requests_total', 'How many times the app has been accessed')
EXCEPTIONS = Counter('flask_app_exceptions_total', 'How many times the app issued an exception')

INPROGRESS = Gauge('flask_app_inprogress_gauge', 'How many requests to the app are currently in progress')
LAST = Gauge('flask_app_last_accessed_gauge', 'When was the app last access')

LATENCY = Summary('flask_app_latency_seconds','time needed for a request')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	
	REQUESTS.inc()
	
	EXCEPTIONS.count_exceptions()

	LAST.set(time.time())
	INPROGRESS.inc()
	start = time.time()
	if request.method == 'POST':
		details = request.form
		if details['form_type'] == 'search_tweets':
			key_words = request.form.values()
			sentence = pd.Series(key_words)
			predicted = pp.pipeline(sentence[0])
			data = json.dumps(predicted)
			data2 = json2html.convert(json = data)
			INPROGRESS.dec()
			return data2
	INPROGRESS.dec()
	LATENCY.observe(time.time() - start)
	return render_template('index.html')


if __name__ == '__main__':
	#pool = ThreadPool(1)
	#pool.apply_async(start_http_server, (8010, ))
	start_http_server(8010)
	app.run(host='0.0.0.0')