import unittest
import os
import requests

class FlaskTests(unittest.TestCase):
	def setUp(self):
		os.environ['NO_PROXY'] = '0.0.0.0'
		pass

	def tearDown(self):
		pass

	def test_a_index(self):
		response = requests.get('http://localhost:5000')
		self.assertEqual(response.status_code, 200)

	def test_b_index(self):	
		params = {
			'word': 'Bad Hillary!',
			'form_type': "search_tweets"
		}
		response = requests.post('http://localhost:5000', data=params)
		self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
	unittest.main()
