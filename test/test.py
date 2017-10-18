import requests
from requests.exceptions import ConnectionError
import os
import sys
topdir = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(topdir)
from config import send_mail, config

try:
    payload = '{}'
    r = requests.post('http://localhost:5003/datasets/count', data=payload)
    assert r.status_code == 200
    print r.text
except ConnectionError:
    print 'ConnectionError'
    send_mail(config['mail']['to_addr'], 'ConnectionError', 'ConnectionError')
except AssertionError:
    print 'AssertionError'
    send_mail(config['mail']['to_addr'], 'AssertionError', str(r.status_code))

try:
    payload = '{\"2017-09-28-12-18-13\":\"\"}'
    r = requests.post('http://localhost:5003/datasets/get', data=payload)
    assert r.status_code == 200
    print r.text
except ConnectionError:
    print 'ConnectionError'
    send_mail(config['mail']['to_addr'], 'ConnectionError', 'ConnectionError')
except AssertionError:
    print 'AssertionError'
    send_mail(config['mail']['to_addr'], 'AssertionError', str(r.status_code))
