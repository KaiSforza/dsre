import unittest
import requests
import requests_mock

session = requests.Session()
adapter = requests_mock.Adapter()
session.mount('mock', adapter)

adapter.register_uri('GET', 'mock://localhost', text='data')
resp = session.get('mock://localhost')
print(resp.status_code, resp.text)
