import unittest
import os
import requests
import grequests
import time

class FlaskTests(unittest.TestCase):
	def setUp(self):
		os.environ['NO_PROXY'] = '0.0.0.0'
		pass

	def tearDown(self):
		pass

	def test_index(self):
	    CONST = 1000
	    urls = []

	    for i in range(CONST):
	        urls.append('http://127.0.0.1:5000')

	    rs = (grequests.get(u) for u in urls)

	    start = time.time()
	    a = grequests.map(rs)
	    end = time.time()

	    for i in range(CONST):
		self.assertEqual(a[i].status_code, 200)

	    print "The",CONST, "requests took:",end-start, "s"


if __name__ == '__main__':
	unittest.main()
