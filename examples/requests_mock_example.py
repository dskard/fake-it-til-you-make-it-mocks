import requests
import requests_mock

session = requests.Session()
adapter = requests_mock.Adapter()
session.mount('http://', adapter)

adapter.register_uri('GET', 'http://test.com', text='data')
resp = session.get('http://test.com')
print(resp.status_code, resp.text)
